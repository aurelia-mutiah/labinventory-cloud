
"""Pengujian integrasi AWS LabInventory secara lokal."""

import io
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import boto3
from botocore.stub import Stubber
from botocore.response import StreamingBody

from src.s3_storage import S3Storage
from src.storage import JsonStorage, StorageError
from src.lambda_function import lambda_handler


class TestS3Storage(unittest.TestCase):
    """Pengujian penyimpanan S3 menggunakan Stubber."""

    def setUp(self):
        self.bucket_name = "labinventory-test"
        self.object_key = "inventory.json"

        self.client = boto3.client(
            "s3",
            region_name="us-east-1",
            aws_access_key_id="testing",
            aws_secret_access_key="testing",
        )

        self.stubber = Stubber(self.client)
        self.stubber.activate()

        self.addCleanup(self.stubber.deactivate)
        self.addCleanup(
            self.stubber.assert_no_pending_responses
        )

        self.storage = S3Storage(
            bucket_name=self.bucket_name,
            object_key=self.object_key,
            s3_client=self.client,
        )

        self.sample_data = [
            {
                "id_barang": "BRG001",
                "nama_barang": "Arduino Uno",
                "kategori": "Mikrokontroler",
                "jumlah": 15,
                "kondisi": "Baik",
            }
        ]

    def test_01_load_data_from_s3(self):
        content = json.dumps(
            self.sample_data
        ).encode("utf-8")

        body = StreamingBody(
            io.BytesIO(content),
            len(content),
        )

        self.stubber.add_response(
            "get_object",
            {"Body": body},
            {
                "Bucket": self.bucket_name,
                "Key": self.object_key,
            },
        )

        result = self.storage.load()

        self.assertEqual(result, self.sample_data)

    def test_02_save_data_to_s3(self):
        content = json.dumps(
            self.sample_data,
            indent=4,
            ensure_ascii=False,
        ).encode("utf-8")

        self.stubber.add_response(
            "put_object",
            {},
            {
                "Bucket": self.bucket_name,
                "Key": self.object_key,
                "Body": content,
                "ContentType": "application/json",
            },
        )

        self.storage.save(self.sample_data)

    def test_03_missing_s3_object(self):
        self.stubber.add_client_error(
            "get_object",
            service_error_code="NoSuchKey",
            http_status_code=404,
            expected_params={
                "Bucket": self.bucket_name,
                "Key": self.object_key,
            },
        )

        self.assertEqual(self.storage.load(), [])

    def test_04_s3_access_denied(self):
        self.stubber.add_client_error(
            "get_object",
            service_error_code="AccessDenied",
            http_status_code=403,
            expected_params={
                "Bucket": self.bucket_name,
                "Key": self.object_key,
            },
        )

        with self.assertRaises(StorageError):
            self.storage.load()

    def test_05_invalid_s3_json(self):
        content = b"invalid json"

        body = StreamingBody(
            io.BytesIO(content),
            len(content),
        )

        self.stubber.add_response(
            "get_object",
            {"Body": body},
            {
                "Bucket": self.bucket_name,
                "Key": self.object_key,
            },
        )

        with self.assertRaises(StorageError):
            self.storage.load()


class TestLambdaHandler(unittest.TestCase):
    """Pengujian Lambda handler tanpa koneksi AWS."""

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        file_path = (
            Path(self.temp_dir.name)
            / "inventory.json"
        )

        self.storage = JsonStorage(file_path)

        self.storage_patcher = patch(
            "src.lambda_function.S3Storage",
            return_value=self.storage,
        )

        self.storage_patcher.start()
        self.addCleanup(
            self.storage_patcher.stop
        )

        self.env_patcher = patch.dict(
            "os.environ",
            {
                "BUCKET_NAME": "labinventory-test",
                "OBJECT_KEY": "inventory.json",
            },
        )

        self.env_patcher.start()
        self.addCleanup(self.env_patcher.stop)

        self.sample_barang = {
            "nama_barang": "Arduino Uno",
            "kategori": "Mikrokontroler",
            "jumlah": 15,
            "kondisi": "Baik",
        }

    def request(self, method, path, data=None):
        event = {
            "httpMethod": method,
            "path": path,
        }

        if data is not None:
            event["body"] = json.dumps(data)

        response = lambda_handler(event, None)

        return (
            response["statusCode"],
            json.loads(response["body"]),
        )

    def test_06_create_barang(self):
        status, body = self.request(
            "POST",
            "/barang",
            self.sample_barang,
        )

        self.assertEqual(status, 201)
        self.assertIn("id_barang", body["data"])

    def test_07_get_all_barang(self):
        self.request(
            "POST",
            "/barang",
            self.sample_barang,
        )

        status, body = self.request(
            "GET",
            "/barang",
        )

        self.assertEqual(status, 200)
        self.assertEqual(body["total"], 1)

    def test_08_update_barang(self):
        _, created = self.request(
            "POST",
            "/barang",
            self.sample_barang,
        )

        id_barang = created["data"]["id_barang"]

        updated_data = {
            **self.sample_barang,
            "jumlah": 20,
        }

        status, body = self.request(
            "PUT",
            f"/barang/{id_barang}",
            updated_data,
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            body["data"]["jumlah"], 20
        )
        self.assertEqual(
            body["data"]["id_barang"], id_barang
        )

    def test_09_delete_barang(self):
        _, created = self.request(
            "POST",
            "/barang",
            self.sample_barang,
        )

        id_barang = created["data"]["id_barang"]

        status, _ = self.request(
            "DELETE",
            f"/barang/{id_barang}",
        )

        self.assertEqual(status, 200)

        _, body = self.request(
            "GET",
            "/barang",
        )

        self.assertEqual(body["total"], 0)

    def test_10_invalid_request(self):
        data = {
            **self.sample_barang,
            "jumlah": -5,
        }

        status, _ = self.request(
            "POST",
            "/barang",
            data,
        )

        self.assertEqual(status, 400)

    def test_11_barang_not_found(self):
        status, _ = self.request(
            "DELETE",
            "/barang/BRG999",
        )

        self.assertEqual(status, 404)

    def test_12_invalid_endpoint(self):
        status, _ = self.request(
            "GET",
            "/unknown",
        )

        self.assertEqual(status, 404)

    def test_13_invalid_http_method(self):
        status, _ = self.request(
            "PATCH",
            "/barang",
        )

        self.assertEqual(status, 405)

    def test_14_http_api_v2_event(self):
        event = {
            "version": "2.0",
            "rawPath": "/barang",
            "requestContext": {
                "http": {
                    "method": "GET",
                    "path": "/barang",
                }
            },
        }

        response = lambda_handler(event, None)

        self.assertEqual(
            response["statusCode"], 200
        )

    def test_15_storage_error(self):
        with patch.object(
            self.storage,
            "load",
            side_effect=StorageError(
                "Simulated storage error"
            ),
        ):
            with self.assertLogs(
                "src.lambda_function",
                level="ERROR",
            ):
                status, _ = self.request(
                    "GET",
                    "/barang",
                )

        self.assertEqual(status, 500)


if __name__ == "__main__":
    unittest.main()
