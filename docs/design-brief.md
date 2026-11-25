
# Design Brief — LabInventory

## Identitas Mahasiswa

- Nama: Aurelia Mutiah Raudyatuzzahra
- NIM: 24/534903/TK/59310
- Kelas: Teknologi Informasi/B
- Mata Kuliah: Cloud Computing
- Judul Proyek: LabInventory — Sistem Inventaris Barang Laboratorium Berbasis Cloud

## 1. Gambaran Umum dan Latar Belakang

LabInventory merupakan prototipe sistem inventaris barang
laboratorium berbasis cloud yang dikembangkan untuk membantu
pengelolaan data peralatan dan barang laboratorium secara
terpusat.

Pencatatan inventaris secara manual dapat menyebabkan
ketidaksesuaian data, kesulitan memperbarui informasi barang,
dan keterbatasan akses terhadap informasi inventaris.

LabInventory memanfaatkan pendekatan serverless pada Amazon
Web Services (AWS) untuk menyediakan fungsi pengelolaan
data tanpa harus menyediakan dan mengelola server fisik
secara mandiri.

## 2. Tujuan

- Menyediakan sistem pengelolaan data inventaris laboratorium.
- Mengimplementasikan empat operasi CRUD terhadap entitas Barang.
- Memanfaatkan layanan cloud untuk pemrosesan dan penyimpanan data.
- Mengimplementasikan konfigurasi dasar infrastruktur AWS.
- Menguji fungsi aplikasi, keamanan dasar, dan konektivitas layanan cloud.

## 3. Ruang Lingkup

Sistem berfokus pada pengelolaan satu entitas, yaitu Barang,
dengan empat fungsi utama:

1. Menambahkan barang baru.
2. Menampilkan seluruh data barang.
3. Memperbarui data barang berdasarkan ID.
4. Menghapus data barang berdasarkan ID.

Frontend, autentikasi pengguna pada tingkat aplikasi,
peminjaman barang, dan pelaporan inventaris tidak termasuk
dalam ruang lingkup prototipe.

## 4. Model Data

| Atribut | Tipe Data | Keterangan |
|---|---|---|
| id_barang | String | Identitas unik yang dibuat otomatis |
| nama_barang | String | Nama barang, tidak boleh kosong |
| kategori | String | Kategori barang, tidak boleh kosong |
| jumlah | Integer | Jumlah barang, minimal 0 |
| kondisi | String | Baik, Rusak Ringan, atau Rusak Berat |

Data inventaris disimpan dalam bentuk array JSON pada
objek inventory.json di Amazon S3.

## 5. Rancangan API

| Method | Endpoint | Fungsi | Success Status |
|---|---|---|---|
| POST | /barang | Menambahkan barang | 201 Created |
| GET | /barang | Menampilkan seluruh barang | 200 OK |
| PUT | /barang/{id_barang} | Memperbarui barang | 200 OK |
| DELETE | /barang/{id_barang} | Menghapus barang | 200 OK |

Pertukaran data menggunakan format JSON. Operasi PUT
menggunakan pembaruan penuh terhadap atribut barang
dengan mempertahankan ID yang sudah ada.

Sistem juga menangani kesalahan input dengan status
400 Bad Request dan barang yang tidak ditemukan dengan
status 404 Not Found.

## 6. Arsitektur Cloud

LabInventory diimplementasikan menggunakan arsitektur
serverless pada AWS Academy Cloud Foundations Sandbox
Lingkungan Hidup, region US East (N. Virginia), us-east-1.

| Layanan | Peran |
|---|---|
| AWS Lambda | Menjalankan logika CRUD, routing, dan validasi data |
| Lambda Function URL | Menyediakan antarmuka HTTPS |
| Amazon S3 | Menyimpan data inventaris dalam format JSON |
| AWS IAM | Mengatur autentikasi dan izin akses layanan |
| Amazon CloudWatch | Mencatat log dan informasi eksekusi Lambda |

Client mengirimkan request HTTPS melalui Lambda Function
URL menggunakan autentikasi AWS_IAM. AWS Lambda memproses
request, menjalankan operasi CRUD, serta membaca atau
memperbarui data pada Amazon S3.

Informasi eksekusi Lambda dicatat melalui Amazon CloudWatch.

Lambda Function URL dipilih karena menyediakan antarmuka
HTTPS langsung tanpa memerlukan komponen API Gateway.

Amazon S3 dipilih karena kebutuhan penyimpanan prototipe
masih sederhana dan hanya mencakup satu entitas utama.

Diagram dan konfigurasi arsitektur secara lengkap tersedia
pada dokumen architecture.md.

## 7. Keamanan dan Jaringan

Implementasi menerapkan konfigurasi keamanan berikut:

- Amazon S3 Block Public Access diaktifkan.
- Default encryption menggunakan SSE-S3.
- AWS Lambda menggunakan execution role LabRole.
- Lambda Function URL menggunakan autentikasi AWS_IAM.
- Request HTTPS ditandatangani menggunakan AWS Signature Version 4.
- Kredensial AWS tidak disimpan dalam source code atau repository.
- Screenshot mentah dikecualikan dari pelacakan Git.

Arsitektur tidak menggunakan custom VPC, subnet, NAT Gateway,
atau Internet Gateway. Komunikasi antar layanan memanfaatkan
jaringan yang dikelola AWS dan menggunakan HTTPS.

AWS Lambda dan Amazon S3 berada pada region yang sama,
yaitu us-east-1.

## 8. Hasil Pengujian

| Pengujian | Hasil |
|---|---|
| Unit testing lokal | 20/20 PASS |
| Simulasi integrasi AWS secara lokal | 15/15 PASS |
| Pengujian fungsional AWS Lambda | 9/9 PASS |
| Konektivitas HTTPS melalui Function URL | HTTP 200 OK |
| Verifikasi penyimpanan Amazon S3 | PASS |
| Verifikasi Amazon CloudWatch Logs | PASS |
| Verifikasi Block Public Access dan SSE-S3 | PASS |

Seluruh operasi CRUD berhasil diuji melalui Lambda Test
Event, termasuk validasi jumlah negatif dan penanganan
barang yang tidak ditemukan.

Pengujian konektivitas HTTPS dilakukan menggunakan AWS
CloudShell melalui metode GET /barang dengan autentikasi
AWS_IAM dan menghasilkan HTTP Status 200.

Pemeriksaan akhir Amazon S3 menunjukkan bahwa objek
inventory.json kembali berisi array kosong setelah
rangkaian pengujian CRUD dan validasi selesai.

## 9. Batasan dan Asumsi

- Sistem merupakan prototipe akademik, bukan sistem produksi.
- Penyimpanan menggunakan satu objek JSON.
- Concurrent write belum ditangani secara aman.
- IAM mengikuti kebijakan LabRole bawaan sandbox.
- Belum tersedia frontend dan autentikasi pengguna aplikasi.
- Pengujian HTTP langsung baru mencakup metode GET.
- Belum dilakukan load testing.
- Ketersediaan infrastruktur mengikuti kebijakan dan masa
  aktif AWS Academy Sandbox.

Pengembangan berikutnya dapat mempertimbangkan penggunaan
Amazon DynamoDB, custom IAM policy berdasarkan prinsip
least privilege, dan antarmuka pengguna.

## 10. Repository

Source code, dokumentasi arsitektur, deployment plan,
testing plan, dan riwayat pengembangan tersedia pada:

https://github.com/aurelia-mutiah/labinventory-cloud

Repository menggunakan Git untuk mencatat perkembangan
implementasi secara bertahap.

## 11. Status Implementasi dan Kesimpulan

**Status: Implemented and Tested**

LabInventory telah berhasil diimplementasikan sebagai
prototipe sistem inventaris barang laboratorium berbasis
cloud menggunakan pendekatan serverless.

Integrasi AWS Lambda dengan Amazon S3 berhasil menjalankan
seluruh operasi CRUD. Lambda Function URL menyediakan akses
HTTPS terautentikasi, sedangkan Amazon CloudWatch menyediakan
pencatatan aktivitas eksekusi.

Hasil pengujian menunjukkan bahwa fungsi utama aplikasi,
konektivitas layanan cloud, dan konfigurasi keamanan dasar
telah berjalan sesuai dengan tujuan pengembangan prototipe.
