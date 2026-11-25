
# Design Brief — LabInventory

## Identitas Mahasiswa

- Nama: Aurelia Mutiah Raudyatuzzahra
- NIM: 24/534903/TK/59310
- Kelas: Teknologi Informasi/B
- Mata Kuliah: Cloud Computing

## 1. Gambaran Umum

LabInventory merupakan prototipe sistem inventaris barang
laboratorium berbasis cloud yang dirancang untuk membantu
pengelolaan data peralatan dan barang laboratorium secara
terpusat.

Sistem menyediakan fungsi penambahan, pembacaan, pembaruan,
dan penghapusan data barang melalui antarmuka backend.

## 2. Latar Belakang

Pencatatan inventaris laboratorium secara manual dapat
menyebabkan ketidaksesuaian data, kesulitan memperbarui
informasi barang, dan keterbatasan akses terhadap informasi
inventaris.

Pemanfaatan cloud computing memungkinkan data inventaris
disimpan secara terpusat serta menyediakan infrastruktur
yang dapat dikelola tanpa harus membangun server fisik
secara mandiri.

## 3. Tujuan

- Menyediakan sistem pengelolaan data inventaris.
- Mengimplementasikan operasi CRUD.
- Memanfaatkan layanan cloud untuk pemrosesan dan
  penyimpanan data.
- Melakukan konfigurasi awal infrastruktur AWS.
- Menguji fungsi aplikasi dan konektivitas layanan cloud.

## 4. Ruang Lingkup

Sistem berfokus pada pengelolaan satu entitas, yaitu Barang.

Fitur yang disediakan:

1. Menambahkan barang.
2. Menampilkan seluruh data barang.
3. Memperbarui data barang berdasarkan ID.
4. Menghapus data barang berdasarkan ID.

Pengembangan antarmuka pengguna, autentikasi pengguna
aplikasi, peminjaman barang, dan pelaporan inventaris
tidak termasuk dalam ruang lingkup prototipe ini.

## 5. Model Data

| Atribut | Tipe Data | Keterangan |
|---|---|---|
| id_barang | String | Identitas unik, dibuat otomatis |
| nama_barang | String | Nama barang |
| kategori | String | Kategori barang |
| jumlah | Integer | Jumlah barang, minimal 0 |
| kondisi | String | Kondisi barang |

Nilai kondisi yang diperbolehkan:

- Baik
- Rusak Ringan
- Rusak Berat

## 6. Rancangan API

| Method | Endpoint | Fungsi |
|---|---|---|
| POST | /barang | Menambahkan barang |
| GET | /barang | Menampilkan seluruh barang |
| PUT | /barang/{id_barang} | Memperbarui barang |
| DELETE | /barang/{id_barang} | Menghapus barang |

Pertukaran data menggunakan format JSON. Operasi PUT
menggunakan pembaruan penuh terhadap atribut barang
dengan mempertahankan ID yang sudah ada.

## 7. Rancangan Arsitektur Cloud

Pendekatan awal menggunakan arsitektur serverless.

Layanan AWS yang direncanakan:

- AWS Lambda: menjalankan logika aplikasi dan CRUD.
- Amazon S3: menyimpan data inventaris dalam format JSON.
- AWS IAM: mengatur izin akses antar layanan.
- Amazon CloudWatch: menyediakan pencatatan log aplikasi.

Antarmuka HTTP akan disesuaikan dengan layanan dan izin
yang tersedia pada AWS Academy Sandbox.

Apabila antarmuka HTTP tidak dapat dikonfigurasi,
pengujian fungsi dapat dilakukan melalui Lambda Console
menggunakan test event.

## 8. Keamanan dan Jaringan

Bucket Amazon S3 direncanakan bersifat privat dengan
Block Public Access diaktifkan.

AWS Lambda menggunakan execution role yang tersedia
dan diizinkan dalam lingkungan sandbox.

Kredensial AWS tidak disimpan dalam kode sumber maupun
repository GitHub.

Arsitektur awal tidak memerlukan konfigurasi VPC khusus.
Akses antar layanan mengikuti mekanisme keamanan AWS
dan kebijakan IAM yang berlaku.

## 9. Strategi Pengujian

Pengujian dilakukan secara bertahap melalui:

1. Unit testing terhadap logika CRUD.
2. Pengujian validasi data dan penanganan kesalahan.
3. Simulasi integrasi Lambda dan S3 secara lokal.
4. Pengujian fungsi pada lingkungan AWS.
5. Verifikasi penyimpanan data dan log aplikasi.

## 10. Batasan dan Asumsi

Sistem merupakan prototipe untuk kebutuhan akademik
dan belum ditujukan untuk penggunaan produksi.

Penyimpanan menggunakan satu objek JSON sehingga belum
mendukung pembaruan data secara bersamaan dengan aman.

Pemilihan layanan, konfigurasi IAM, region, dan mekanisme
akses aplikasi bergantung pada fasilitas yang tersedia
dalam AWS Academy Sandbox.

## 11. Status Implementasi

Logika CRUD, penyimpanan lokal, adapter Amazon S3,
dan Lambda handler telah dikembangkan.

Sebanyak 35 pengujian otomatis telah berhasil dijalankan
secara lokal.

Provisioning infrastruktur, konektivitas antar layanan,
dan pengujian langsung pada AWS masih menunggu
pelaksanaan sandbox.

Dokumen ini merupakan rancangan awal dan akan
diperbarui berdasarkan hasil implementasi aktual.
