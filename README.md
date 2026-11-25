
# LabInventory

## Sistem Inventaris Barang Laboratorium Berbasis Cloud

Proyek Individu Cloud Computing - Week 12: Design & AWS Setup.

## Identitas Pengembang

- Nama: Aurelia Mutiah Raudyatuzzahra
- NIM: 24/534903/TK/59310
- Kelas: Teknologi Informasi/B

## 1. Deskripsi Proyek

LabInventory merupakan aplikasi backend berbasis cloud yang dirancang untuk membantu pengelolaan data inventaris barang laboratorium.

Aplikasi ini menyediakan fungsi untuk menambahkan, menampilkan, memperbarui, dan menghapus data barang melalui operasi CRUD (Create, Read, Update, dan Delete).

Proyek dikembangkan menggunakan Python dengan pendekatan arsitektur cloud yang disesuaikan dengan layanan yang tersedia pada AWS Academy Cloud Foundations Sandbox.

## 2. Latar Belakang

Pengelolaan inventaris barang laboratorium secara manual dapat menyebabkan kesulitan dalam pencarian data, pembaruan jumlah barang, serta pemantauan kondisi peralatan.

LabInventory dirancang sebagai solusi sederhana untuk menyediakan pengelolaan data inventaris secara terpusat dengan memanfaatkan layanan cloud.

## 3. Tujuan

- Mengembangkan sistem pengelolaan inventaris barang laboratorium.
- Mengimplementasikan empat operasi CRUD.
- Merancang arsitektur aplikasi berbasis cloud.
- Memanfaatkan layanan AWS sesuai batasan lingkungan sandbox.
- Melakukan pengujian aplikasi dan konektivitas antar layanan AWS.

## 4. Ruang Lingkup

Proyek berfokus pada pengelolaan satu entitas utama, yaitu Barang.

Fitur yang direncanakan:

- Menambahkan data barang baru.
- Menampilkan daftar barang.
- Memperbarui data barang.
- Menghapus data barang.

Pengembangan frontend, autentikasi pengguna, peminjaman barang, dan pelaporan otomatis tidak termasuk dalam ruang lingkup proyek ini.

## 5. Rancangan Entitas Data

Entitas: Barang

| Atribut | Tipe Data | Keterangan |
|---|---|---|
| id_barang | String | Identitas unik barang |
| nama_barang | String | Nama barang laboratorium |
| kategori | String | Kategori barang |
| jumlah | Integer | Jumlah barang tersedia |
| kondisi | String | Kondisi barang |

Contoh data:

```json
{
  "id_barang": "BRG001",
  "nama_barang": "Arduino Uno",
  "kategori": "Mikrokontroler",
  "jumlah": 15,
  "kondisi": "Baik"
}
```

## 6. Rancangan API

| Method | Endpoint | Deskripsi |
|---|---|---|
| POST | /barang | Menambahkan barang |
| GET | /barang | Menampilkan daftar barang |
| PUT | /barang/{id_barang} | Memperbarui barang |
| DELETE | /barang/{id_barang} | Menghapus barang |

Endpoint tersebut merupakan kontrak API yang direncanakan. Implementasi akses HTTP akan disesuaikan dengan hasil verifikasi lingkungan AWS.

## 7. Teknologi dan Lingkungan Pengembangan

- Python 3
- Visual Studio Code
- Git dan GitHub
- JSON
- AWS Academy Cloud Foundations Sandbox
- AWS Region: us-east-1

### Kandidat Layanan AWS

| Layanan | Rencana Penggunaan |
|---|---|
| AWS Lambda | Menjalankan logika aplikasi |
| Amazon S3 | Penyimpanan data inventaris |
| AWS IAM LabRole | Mengatur izin akses antar layanan |
| Amazon CloudWatch | Monitoring dan pencatatan log |

Pemilihan layanan dan arsitektur final akan ditetapkan setelah verifikasi akses serta izin pada lingkungan sandbox.

## 8. Struktur Repository

```text
labinventory-cloud/
├── docs/
│   ├── design-brief.md
│   ├── deployment-plan.md
│   └── testing-plan.md
├── evidence/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── inventory.py
│   ├── lambda_function.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   ├── sample_data.json
│   └── test_inventory.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 9. Rencana Pengembangan

1. Menyusun spesifikasi dan rancangan data.
2. Menyiapkan repository dan struktur proyek.
3. Mengimplementasikan logika CRUD.
4. Melakukan pengujian lokal.
5. Memverifikasi layanan AWS Sandbox.
6. Menetapkan arsitektur cloud.
7. Melakukan konfigurasi dan deployment AWS.
8. Melakukan pengujian konektivitas.
9. Mendokumentasikan hasil pengujian.
10. Melakukan finalisasi dokumentasi proyek.

## 10. Rencana Deployment

Deployment akan dilakukan melalui AWS Academy Cloud Foundations Sandbox setelah kode aplikasi dan pengujian lokal selesai.

Konfigurasi layanan, izin akses, serta pengujian konektivitas akan didokumentasikan pada folder `docs/`.

Bukti konfigurasi dan pengujian akan disimpan pada folder `evidence/`.

## 11. Keamanan dan Batasan Lingkungan

- Penggunaan layanan AWS mengikuti izin yang tersedia pada sandbox.
- Kredensial AWS tidak disimpan dalam source code atau repository.
- Penggunaan resource disesuaikan dengan kebutuhan pengujian.
- Resource sandbox bersifat sementara dan dapat dihapus ketika sesi berakhir.
- Kode, dokumentasi, dan bukti pengujian disimpan di luar lingkungan sandbox.

---

LabInventory - Individual Cloud Computing Project.
