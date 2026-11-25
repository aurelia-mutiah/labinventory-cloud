
"""Penyimpanan data inventaris menggunakan Amazon S3."""

import json

from src.storage import StorageError


class S3Storage:
    """Mengelola penyimpanan JSON pada Amazon S3."""

    def __init__(
        self,
        bucket_name,
        object_key="inventory.json",
        s3_client=None,
    ):
        if not bucket_name:
            raise StorageError(
                "Nama bucket S3 belum dikonfigurasi."
            )

        self.bucket_name = bucket_name
        self.object_key = object_key

        if s3_client is None:
            import boto3

            s3_client = boto3.client("s3")

        self.s3_client = s3_client

    def load(self):
        """Membaca data inventaris dari Amazon S3."""

        from botocore.exceptions import (
            ClientError,
            BotoCoreError,
        )

        try:
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=self.object_key,
            )

            content = response["Body"].read()
            data = json.loads(content.decode("utf-8"))

            if not isinstance(data, list):
                raise StorageError(
                    "Format penyimpanan harus berupa list."
                )

            return data

        except ClientError as error:
            error_code = error.response.get(
                "Error", {}
            ).get("Code", "")

            if error_code == "NoSuchKey":
                return []

            raise StorageError(
                "Gagal membaca data dari Amazon S3."
            ) from error

        except BotoCoreError as error:
            raise StorageError(
                "Gagal terhubung dengan Amazon S3."
            ) from error

        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            raise StorageError(
                "Data pada Amazon S3 bukan JSON yang valid."
            ) from error

    def save(self, data):
        """Menyimpan data inventaris ke Amazon S3."""

        from botocore.exceptions import (
            ClientError,
            BotoCoreError,
        )

        if not isinstance(data, list):
            raise StorageError(
                "Data yang disimpan harus berupa list."
            )

        try:
            content = json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ).encode("utf-8")

            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=self.object_key,
                Body=content,
                ContentType="application/json",
            )

        except (ClientError, BotoCoreError) as error:
            raise StorageError(
                "Gagal menyimpan data ke Amazon S3."
            ) from error

        except (TypeError, ValueError) as error:
            raise StorageError(
                "Data inventaris tidak dapat dikonversi ke JSON."
            ) from error
