
"""Logika pengelolaan inventaris barang laboratorium."""

from uuid import uuid4


VALID_CONDITIONS = (
    "Baik",
    "Rusak Ringan",
    "Rusak Berat",
)

REQUIRED_FIELDS = (
    "nama_barang",
    "kategori",
    "jumlah",
    "kondisi",
)


class InventoryError(Exception):
    """Exception dasar untuk aplikasi inventaris."""


class ValidationError(InventoryError):
    """Exception ketika data barang tidak valid."""


class BarangNotFoundError(InventoryError):
    """Exception ketika barang tidak ditemukan."""


class InventoryService:
    """Menangani operasi CRUD data inventaris."""

    def __init__(self, storage):
        self.storage = storage

    def validate_barang(self, data):
        """Memastikan seluruh atribut barang valid."""

        if not isinstance(data, dict):
            raise ValidationError(
                "Data barang harus berupa objek."
            )

        for field in REQUIRED_FIELDS:
            if field not in data:
                raise ValidationError(
                    f"Atribut {field} wajib diisi."
                )

        for field in ("nama_barang", "kategori"):
            value = data[field]

            if not isinstance(value, str) or not value.strip():
                raise ValidationError(
                    f"{field} harus berupa teks yang tidak kosong."
                )

        jumlah = data["jumlah"]

        if type(jumlah) is not int:
            raise ValidationError(
                "Jumlah barang harus berupa bilangan bulat."
            )

        if jumlah < 0:
            raise ValidationError(
                "Jumlah barang tidak boleh negatif."
            )

        if data["kondisi"] not in VALID_CONDITIONS:
            raise ValidationError(
                "Kondisi barang harus Baik, Rusak Ringan, "
                "atau Rusak Berat."
            )

        return {
            "nama_barang": data["nama_barang"].strip(),
            "kategori": data["kategori"].strip(),
            "jumlah": jumlah,
            "kondisi": data["kondisi"],
        }

    def create_barang(self, data):
        """Menambahkan barang baru ke penyimpanan."""

        validated_data = self.validate_barang(data)
        barang_list = self.storage.load()

        existing_ids = {
            barang["id_barang"] for barang in barang_list
        }

        while True:
            id_barang = f"BRG-{uuid4().hex[:12].upper()}"

            if id_barang not in existing_ids:
                break

        barang_baru = {
            "id_barang": id_barang,
            **validated_data,
        }

        barang_list.append(barang_baru)
        self.storage.save(barang_list)

        return barang_baru

    def get_all_barang(self):
        """Mengembalikan seluruh data barang."""

        return self.storage.load()

    def get_barang_by_id(self, id_barang):
        """Mencari barang berdasarkan ID."""

        barang_list = self.storage.load()

        for barang in barang_list:
            if barang["id_barang"] == id_barang:
                return barang

        raise BarangNotFoundError(
            f"Barang dengan ID {id_barang} tidak ditemukan."
        )

    def update_barang(self, id_barang, data):
        """Memperbarui data barang berdasarkan ID."""

        validated_data = self.validate_barang(data)
        barang_list = self.storage.load()

        for index, barang in enumerate(barang_list):
            if barang["id_barang"] == id_barang:

                barang_baru = {
                    "id_barang": id_barang,
                    **validated_data,
                }

                barang_list[index] = barang_baru
                self.storage.save(barang_list)

                return barang_baru

        raise BarangNotFoundError(
            f"Barang dengan ID {id_barang} tidak ditemukan."
        )

    def delete_barang(self, id_barang):
        """Menghapus barang berdasarkan ID."""

        barang_list = self.storage.load()

        for index, barang in enumerate(barang_list):
            if barang["id_barang"] == id_barang:

                barang_dihapus = barang_list.pop(index)
                self.storage.save(barang_list)

                return barang_dihapus

        raise BarangNotFoundError(
            f"Barang dengan ID {id_barang} tidak ditemukan."
        )
