
"""Pengujian aplikasi LabInventory."""

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.inventory import (
    InventoryService,
    ValidationError,
    BarangNotFoundError,
    REQUIRED_FIELDS,
)
from src.storage import JsonStorage, StorageError


class TestInventory(unittest.TestCase):
    """Pengujian operasi CRUD dan validasi inventaris."""

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.file_path = (
            Path(self.temp_dir.name) / "inventory.json"
        )

        self.storage = JsonStorage(self.file_path)
        self.service = InventoryService(self.storage)

        self.sample_barang = {
            "nama_barang": "Arduino Uno",
            "kategori": "Mikrokontroler",
            "jumlah": 15,
            "kondisi": "Baik",
        }

    def test_01_create_barang(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        self.assertIn("id_barang", barang)
        self.assertEqual(
            barang["nama_barang"], "Arduino Uno"
        )
        self.assertEqual(barang["jumlah"], 15)
        self.assertEqual(
            self.storage.load(), [barang]
        )

    def test_02_get_all_barang(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        hasil = self.service.get_all_barang()

        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0], barang)

    def test_03_get_barang_by_id(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        hasil = self.service.get_barang_by_id(
            barang["id_barang"]
        )

        self.assertEqual(hasil, barang)

    def test_04_update_barang(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        data_baru = {
            "nama_barang": "Arduino Uno",
            "kategori": "Mikrokontroler",
            "jumlah": 20,
            "kondisi": "Rusak Ringan",
        }

        hasil = self.service.update_barang(
            barang["id_barang"], data_baru
        )

        self.assertEqual(hasil["jumlah"], 20)
        self.assertEqual(
            hasil["kondisi"], "Rusak Ringan"
        )
        self.assertEqual(
            hasil["id_barang"], barang["id_barang"]
        )
        self.assertEqual(
            self.storage.load(), [hasil]
        )

    def test_05_delete_barang(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        hasil = self.service.delete_barang(
            barang["id_barang"]
        )

        self.assertEqual(hasil, barang)
        self.assertEqual(
            self.service.get_all_barang(), []
        )

    def test_06_empty_inventory(self):
        self.assertEqual(
            self.service.get_all_barang(), []
        )

    def test_07_negative_quantity(self):
        data = {
            **self.sample_barang,
            "jumlah": -5,
        }

        with self.assertRaises(ValidationError):
            self.service.create_barang(data)

        self.assertEqual(self.storage.load(), [])

    def test_08_invalid_quantity_type(self):
        for jumlah in ("15", 2.5, True):
            with self.subTest(jumlah=jumlah):
                data = {
                    **self.sample_barang,
                    "jumlah": jumlah,
                }

                with self.assertRaises(ValidationError):
                    self.service.create_barang(data)

    def test_09_empty_name(self):
        data = {
            **self.sample_barang,
            "nama_barang": "   ",
        }

        with self.assertRaises(ValidationError):
            self.service.create_barang(data)

    def test_10_invalid_condition(self):
        data = {
            **self.sample_barang,
            "kondisi": "Tidak Diketahui",
        }

        with self.assertRaises(ValidationError):
            self.service.create_barang(data)

    def test_11_missing_required_field(self):
        for field in REQUIRED_FIELDS:
            with self.subTest(field=field):
                data = self.sample_barang.copy()
                del data[field]

                with self.assertRaises(ValidationError):
                    self.service.create_barang(data)

    def test_12_barang_not_found(self):
        with self.assertRaises(BarangNotFoundError):
            self.service.get_barang_by_id("BRG999")

    def test_13_update_nonexistent_barang(self):
        with self.assertRaises(BarangNotFoundError):
            self.service.update_barang(
                "BRG999", self.sample_barang
            )

    def test_14_delete_nonexistent_barang(self):
        with self.assertRaises(BarangNotFoundError):
            self.service.delete_barang("BRG999")

    def test_15_unique_id(self):
        daftar_barang = [
            self.service.create_barang(
                self.sample_barang
            )
            for _ in range(10)
        ]

        daftar_id = {
            barang["id_barang"]
            for barang in daftar_barang
        }

        self.assertEqual(len(daftar_id), 10)
        self.assertEqual(
            len(self.service.get_all_barang()), 10
        )

    def test_16_data_persistence(self):
        barang = self.service.create_barang(
            self.sample_barang
        )

        storage_baru = JsonStorage(self.file_path)
        service_baru = InventoryService(storage_baru)

        self.assertEqual(
            service_baru.get_all_barang(), [barang]
        )

    def test_17_sample_data_validation(self):
        sample_path = (
            Path(__file__).resolve().parent
            / "sample_data.json"
        )

        with sample_path.open(
            "r", encoding="utf-8"
        ) as file:
            data = json.load(file)

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 5)

        daftar_id = set()

        for barang in data:
            with self.subTest(barang=barang):
                self.service.validate_barang(barang)

                self.assertIsInstance(
                    barang["id_barang"], str
                )
                self.assertTrue(
                    barang["id_barang"].strip()
                )
                self.assertNotIn(
                    barang["id_barang"], daftar_id
                )

                daftar_id.add(barang["id_barang"])

    def test_18_invalid_json_storage(self):
        self.file_path.write_text(
            "invalid json",
            encoding="utf-8",
        )

        with self.assertRaises(StorageError):
            self.storage.load()

    def test_19_invalid_storage_format(self):
        with self.assertRaises(StorageError):
            self.storage.save({"invalid": "data"})

    def test_20_zero_quantity(self):
        data = {
            **self.sample_barang,
            "jumlah": 0,
        }

        barang = self.service.create_barang(data)

        self.assertEqual(barang["jumlah"], 0)


if __name__ == "__main__":
    unittest.main()
