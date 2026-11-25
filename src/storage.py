
"""Penyimpanan data inventaris menggunakan file JSON."""

import json
from pathlib import Path


class StorageError(Exception):
    """Exception ketika terjadi kesalahan penyimpanan."""


class JsonStorage:
    """Mengelola penyimpanan data inventaris secara lokal."""

    def __init__(self, file_path=None):
        if file_path is None:
            project_root = Path(__file__).resolve().parent.parent
            file_path = project_root / "data" / "inventory.json"

        self.file_path = Path(file_path)

    def load(self):
        """Membaca seluruh data barang dari file JSON."""

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open(
                "r", encoding="utf-8"
            ) as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise StorageError(
                    "Format penyimpanan harus berupa list."
                )

            return data

        except json.JSONDecodeError as error:
            raise StorageError(
                "File penyimpanan bukan JSON yang valid."
            ) from error

        except OSError as error:
            raise StorageError(
                "Gagal membaca file penyimpanan."
            ) from error

    def save(self, data):
        """Menyimpan seluruh data barang ke file JSON."""

        if not isinstance(data, list):
            raise StorageError(
                "Data yang disimpan harus berupa list."
            )

        try:
            self.file_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            temporary_path = self.file_path.with_suffix(
                self.file_path.suffix + ".tmp"
            )

            with temporary_path.open(
                "w", encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False,
                )

            temporary_path.replace(self.file_path)

        except (OSError, TypeError, ValueError) as error:
            raise StorageError(
                "Gagal menyimpan data inventaris."
            ) from error
