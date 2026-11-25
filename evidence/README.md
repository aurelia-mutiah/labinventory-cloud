
# Evidence Documentation — LabInventory

## 1. Purpose

Folder evidence digunakan untuk mengelola bukti
pengembangan, konfigurasi infrastruktur, dan hasil
pengujian aplikasi LabInventory.

Bukti dikumpulkan untuk mendukung laporan tugas
Cloud Computing dan menunjukkan kesesuaian antara
rancangan dengan implementasi aktual.

## 2. Directory Structure

```text
evidence/
├── README.md
└── raw/
    ├── 01_local_unit_testing.png
    ├── 02_combined_testing.png
    └── ...
```

Folder raw digunakan untuk menyimpan screenshot asli
secara lokal.

Screenshot yang mengandung informasi sensitif tidak
diunggah ke repository GitHub.

## 3. Evidence Naming Convention

Format penamaan file:

NN_deskripsi_bukti.png

Keterangan:

- NN: nomor urut bukti.
- deskripsi_bukti: penjelasan singkat isi screenshot.
- png: format gambar.

Contoh:

03_sandbox_environment.png

Penamaan dapat disesuaikan apabila terdapat perubahan
arsitektur atau urutan implementasi.

## 4. Evidence Checklist

### 4.1 Local Development

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-01 | 01_local_unit_testing.png | Hasil 20 unit test | Collected |
| EV-02 | 02_combined_testing.png | Hasil 35 pengujian otomatis | Collected |

### 4.2 AWS Environment

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-03 | 03_sandbox_environment.png | Lingkungan AWS Academy Sandbox | Pending |
| EV-04 | 04_aws_console_region.png | AWS Console dan region | Pending |

### 4.3 Storage Provisioning

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-05 | 05_s3_bucket.png | Bucket S3 yang dibuat | Pending |
| EV-06 | 06_s3_public_access.png | Konfigurasi Block Public Access | Pending |
| EV-07 | 07_s3_encryption.png | Konfigurasi enkripsi bucket | Pending |
| EV-08 | 08_s3_initial_object.png | Objek inventory.json | Pending |

### 4.4 Compute Provisioning

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-09 | 09_lambda_function.png | Lambda function overview | Pending |
| EV-10 | 10_lambda_runtime_handler.png | Runtime dan handler | Pending |
| EV-11 | 11_lambda_environment.png | Environment variables | Pending |
| EV-12 | 12_lambda_execution_role.png | Execution role Lambda | Pending |
| EV-13 | 13_lambda_configuration.png | Memory dan timeout | Pending |

### 4.5 Connectivity and CRUD Testing

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-14 | 14_connectivity_test.png | Lambda berhasil membaca S3 | Pending |
| EV-15 | 15_create_barang.png | Hasil operasi Create | Pending |
| EV-16 | 16_read_barang.png | Hasil operasi Read | Pending |
| EV-17 | 17_update_barang.png | Hasil operasi Update | Pending |
| EV-18 | 18_s3_data_persistence.png | Isi data aktual pada S3 | Pending |
| EV-19 | 19_delete_barang.png | Hasil operasi Delete | Pending |
| EV-20 | 20_read_after_delete.png | Verifikasi penghapusan | Pending |
| EV-21 | 21_invalid_quantity.png | Validasi jumlah negatif | Pending |
| EV-22 | 22_barang_not_found.png | Penanganan ID tidak ditemukan | Pending |
| EV-23 | 23_invalid_endpoint.png | Penanganan endpoint tidak valid | Pending |

### 4.6 Monitoring and HTTP Access

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-24 | 24_cloudwatch_logs.png | Log eksekusi Lambda | Pending |
| EV-25 | 25_http_interface.png | Konfigurasi antarmuka HTTP | Conditional |
| EV-26 | 26_http_request_test.png | Hasil pengujian HTTP aktual | Conditional |

### 4.7 Repository and Final Documentation

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-27 | 27_github_repository.png | Repository GitHub final | Pending |
| EV-28 | 28_git_commit_history.png | Riwayat commit Git | Pending |
| EV-29 | 29_final_architecture.png | Diagram arsitektur final | Pending |

## 5. Screenshot Guidelines

Setiap screenshot harus:

- Menampilkan informasi yang relevan.
- Memiliki teks yang dapat dibaca.
- Menampilkan konfigurasi atau hasil aktual.
- Menghindari pemotongan informasi penting.
- Menggunakan penamaan file yang konsisten.
- Tidak menampilkan kredensial AWS.
- Tidak menampilkan token atau informasi rahasia.
- Tidak menampilkan signed URL atau session token.

Informasi sensitif seperti account ID, ARN lengkap,
dan detail akun dapat disamarkan apabila tidak
diperlukan sebagai bukti.

Screenshot asli disimpan secara lokal.

## 6. Evidence Status

| Status | Description |
|---|---|
| Collected | Bukti telah dikumpulkan |
| Pending | Bukti belum dikumpulkan |
| Conditional | Bergantung pada konfigurasi aktual |
| Blocked | Bukti tidak dapat dikumpulkan karena kendala |
| Not Applicable | Bukti tidak relevan pada arsitektur final |

Status diperbarui setelah bukti aktual diperoleh.

## 7. Evidence Security

Folder evidence/raw telah dimasukkan ke dalam
.gitignore agar screenshot tidak ikut terunggah
ke repository publik.

Sebelum screenshot dimasukkan ke laporan akhir,
lakukan pemeriksaan terhadap informasi sensitif.

Jangan menyimpan atau membagikan:

- AWS Access Key ID.
- AWS Secret Access Key.
- AWS Session Token.
- Password.
- Private key.
- Informasi autentikasi lainnya.

## 8. Evidence Selection for Final Report

Tidak seluruh screenshot harus dimasukkan ke dalam
laporan utama.

Bukti utama dipilih berdasarkan relevansinya terhadap:

- Diagram arsitektur.
- Konfigurasi infrastruktur AWS.
- Keamanan dan izin akses.
- Konektivitas antar layanan.
- Pengujian CRUD.
- Persistensi data.
- Repository dan riwayat pengembangan.

Screenshot tambahan dapat disertakan sebagai lampiran
apabila diperlukan.

## 9. Current Status

Local development evidence: Collected

AWS provisioning evidence: Pending

AWS testing evidence: Pending

Final repository evidence: Pending

Dokumen ini merupakan panduan awal pengumpulan bukti.
Daftar screenshot akan disesuaikan berdasarkan
implementasi aktual pada AWS Academy Sandbox.
