
"""AWS Lambda handler untuk aplikasi LabInventory."""

import base64
import json
import logging
import os

from src.inventory import (
    InventoryService,
    ValidationError,
    BarangNotFoundError,
)
from src.storage import StorageError
from src.s3_storage import S3Storage


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_response(status_code, data):
    """Membentuk respons HTTP dalam format JSON."""

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": json.dumps(
            data,
            ensure_ascii=False,
        ),
    }


def parse_body(event):
    """Membaca dan memvalidasi request body."""

    body = event.get("body")

    if body is None:
        raise ValidationError(
            "Request body wajib diisi."
        )

    try:
        if event.get("isBase64Encoded"):
            body = base64.b64decode(
                body, validate=True
            ).decode("utf-8")

        if isinstance(body, str):
            body = json.loads(body)

        if not isinstance(body, dict):
            raise ValidationError(
                "Request body harus berupa objek JSON."
            )

        return body

    except (ValueError, TypeError) as error:
        raise ValidationError(
            "Request body bukan JSON yang valid."
        ) from error


def get_request_details(event):
    """Membaca metode HTTP dan path permintaan."""

    request_context = event.get(
        "requestContext", {}
    )

    http_context = request_context.get(
        "http", {}
    )

    method = (
        event.get("httpMethod")
        or http_context.get("method")
        or ""
    ).upper()

    path = (
        event.get("rawPath")
        or event.get("path")
        or http_context.get("path")
        or "/"
    )

    path = path.rstrip("/") or "/"

    return method, path


def lambda_handler(event, context):
    """Entry point aplikasi pada AWS Lambda."""

    try:
        method, path = get_request_details(event)

        logger.info(
            "Request: %s %s",
            method,
            path,
        )

        parts = path.strip("/").split("/")

        if (
            parts[0] != "barang"
            or len(parts) > 2
            or (len(parts) == 2 and not parts[1])
        ):
            return create_response(
                404,
                {"message": "Endpoint tidak ditemukan."},
            )

        id_barang = (
            parts[1] if len(parts) == 2 else None
        )

        if id_barang is None:
            allowed_methods = ("GET", "POST")
        else:
            allowed_methods = ("PUT", "DELETE")

        if method not in allowed_methods:
            return create_response(
                405,
                {"message": "Metode HTTP tidak diizinkan."},
            )

        bucket_name = os.environ.get(
            "BUCKET_NAME"
        )

        object_key = os.environ.get(
            "OBJECT_KEY",
            "inventory.json",
        )

        storage = S3Storage(
            bucket_name=bucket_name,
            object_key=object_key,
        )

        service = InventoryService(storage)

        # CREATE
        if method == "POST":
            data = parse_body(event)
            barang = service.create_barang(data)

            return create_response(
                201,
                {
                    "message": "Barang berhasil ditambahkan.",
                    "data": barang,
                },
            )

        # READ
        if method == "GET":
            daftar_barang = service.get_all_barang()

            return create_response(
                200,
                {
                    "message": "Data inventaris berhasil dibaca.",
                    "total": len(daftar_barang),
                    "data": daftar_barang,
                },
            )

        # UPDATE
        if method == "PUT":
            data = parse_body(event)

            barang = service.update_barang(
                id_barang,
                data,
            )

            return create_response(
                200,
                {
                    "message": "Barang berhasil diperbarui.",
                    "data": barang,
                },
            )

        # DELETE
        if method == "DELETE":
            barang = service.delete_barang(
                id_barang
            )

            return create_response(
                200,
                {
                    "message": "Barang berhasil dihapus.",
                    "data": barang,
                },
            )

    except ValidationError as error:
        return create_response(
            400,
            {"message": str(error)},
        )

    except BarangNotFoundError as error:
        return create_response(
            404,
            {"message": str(error)},
        )

    except StorageError:
        logger.exception("Storage error")

        return create_response(
            500,
            {"message": "Terjadi kesalahan penyimpanan."},
        )

    except Exception:
        logger.exception("Unexpected error")

        return create_response(
            500,
            {"message": "Terjadi kesalahan internal."},
        )
