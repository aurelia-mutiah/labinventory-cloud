
# Evidence Documentation — LabInventory

## 1. Purpose

Folder evidence digunakan untuk mengelola bukti pengembangan, konfigurasi infrastruktur, deployment, dan hasil pengujian aplikasi LabInventory.

Bukti dikumpulkan untuk mendukung laporan tugas Cloud Computing dan menunjukkan kesesuaian antara rancangan dengan implementasi aktual pada AWS Academy Cloud Foundations Sandbox Lingkungan Hidup.

Dokumen ini berfungsi sebagai indeks bukti pengerjaan dan referensi penyusunan laporan akhir.

---

## 2. Directory Structure

```text
evidence/
├── README.md
└── raw/
    ├── 01_local_unit_testing.png
    ├── 02_combined_testing.png
    ├── 03_sandbox_environment.png
    ├── 04_aws_console_region.png
    ├── 05_s3_bucket_created.png
    ├── 06_s3_initial_data_uploaded.png
    ├── 07_lambda_function_created.png
    ├── 08_lambda_code_deployed.png
    ├── aws_cloudwatch_log_events.png
    ├── aws_cloudwatch_log_group.png
    ├── aws_http_connectivity_test.png
    ├── aws_lambda_cloudwatch_permissions.png
    ├── aws_lambda_environment_variables.png
    ├── aws_lambda_function_url.png
    ├── aws_lambda_general_configuration.png
    ├── aws_lambda_runtime_settings.png
    ├── aws_lambda_s3_permissions.png
    ├── aws_s3_block_public_access.png
    ├── aws_s3_default_encryption.png
    ├── aws_s3_final_inventory.png
    ├── aws_test_delete_barang.png
    ├── aws_test_delete_not_found.png
    ├── aws_test_get_final_verification.png
    ├── aws_test_get_initial_inventory.png
    ├── aws_test_get_read_barang.png
    ├── aws_test_get_verify_update.png
    ├── aws_test_post_create_barang.png
    ├── aws_test_post_invalid_jumlah.png
    ├── aws_test_put_update_barang.png
    ├── final_github_repository.png
    ├── final_git_commit_history.png
    └── final_architecture_diagram.png
```

Folder `raw/` digunakan untuk menyimpan screenshot asli secara lokal.

Folder tersebut dikecualikan dari pelacakan Git melalui `.gitignore` untuk mencegah informasi sensitif ikut terunggah ke repository publik.

Dokumen `README.md` tetap dilacak oleh Git sebagai indeks bukti pengerjaan.

---

## 3. Evidence Naming Convention

Screenshot menggunakan tiga format penamaan:

```text
NN_deskripsi_bukti.png
aws_deskripsi_bukti.png
final_deskripsi_bukti.png
```

Keterangan:

- `NN`: nomor urut pengumpulan bukti awal.
- `aws`: bukti konfigurasi atau pengujian AWS.
- `final`: bukti finalisasi repository dan arsitektur.
- `deskripsi_bukti`: penjelasan singkat isi screenshot.
- `png`: format gambar.

Nama file yang telah digunakan selama implementasi dipertahankan agar sesuai dengan bukti aktual.

ID evidence pada dokumen ini digunakan sebagai referensi dokumentasi dan tidak mengharuskan perubahan nama file screenshot.

---

## 4. Evidence Checklist

### 4.1 Local Development and Testing

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-01 | 01_local_unit_testing.png | Hasil 20 unit tests lokal | Collected |
| EV-02 | 02_combined_testing.png | Hasil 35 automated tests | Collected |

Total: 2 screenshots.

Bukti menunjukkan bahwa logika aplikasi dan simulasi integrasi AWS telah diuji sebelum deployment.

Hasil pengujian lokal:

| Test Category | Total | Passed |
|---|---:|---:|
| Inventory Unit Testing | 20 | 20 |
| AWS Integration Testing | 15 | 15 |
| Total | 35 | 35 |

Seluruh automated tests berhasil dijalankan tanpa kegagalan.

### 4.2 AWS Environment

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-03 | 03_sandbox_environment.png | Lingkungan AWS Academy Cloud Foundations Sandbox | Collected |
| EV-04 | 04_aws_console_region.png | AWS Management Console dan region us-east-1 | Collected |

Total: 2 screenshots.

Lingkungan implementasi:

| Configuration | Value |
|---|---|
| Platform | AWS Academy |
| Course | Cloud Foundations |
| Environment | Sandbox Lingkungan Hidup |
| Region | us-east-1 |
| Region Name | US East (N. Virginia) |
| Architecture | Serverless |

Bukti menunjukkan lingkungan cloud yang digunakan untuk implementasi LabInventory.

### 4.3 Amazon S3 Provisioning and Storage

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-05 | 05_s3_bucket_created.png | Bucket Amazon S3 berhasil dibuat | Collected |
| EV-06 | 06_s3_initial_data_uploaded.png | Objek inventory.json berhasil diunggah | Collected |
| EV-07 | aws_s3_final_inventory.png | Isi akhir inventory.json setelah pengujian | Collected |

Total: 3 screenshots.

Resource penyimpanan:

| Configuration | Value |
|---|---|
| Service | Amazon S3 |
| Bucket Name | labinventory-534903-20261125 |
| Region | us-east-1 |
| Object Key | inventory.json |
| Data Format | JSON |
| Initial Data | [] |
| Final Data | [] |

Bukti menunjukkan keberhasilan provisioning, inisialisasi penyimpanan, dan verifikasi akhir data.

Objek `inventory.json` digunakan sebagai media penyimpanan data inventaris aplikasi.

Setelah seluruh pengujian CRUD selesai, data pengujian dihapus dan isi objek kembali menjadi array kosong.

### 4.4 AWS Lambda Provisioning and Configuration

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-08 | 07_lambda_function_created.png | Lambda function berhasil dibuat | Collected |
| EV-09 | 08_lambda_code_deployed.png | Source code berhasil di-deploy | Collected |
| EV-10 | aws_lambda_runtime_settings.png | Runtime Python dan konfigurasi handler | Collected |
| EV-11 | aws_lambda_environment_variables.png | Konfigurasi environment variables | Collected |
| EV-12 | aws_lambda_general_configuration.png | Konfigurasi memory dan timeout | Collected |

Total: 5 screenshots.

Konfigurasi utama Lambda:

| Configuration | Value |
|---|---|
| Function Name | labinventory-crud |
| Runtime | Python 3.11 |
| Architecture | x86_64 |
| Memory | 128 MB |
| Timeout | 15 seconds |
| Ephemeral Storage | 512 MB |
| Handler | src.lambda_function.lambda_handler |
| Execution Role | LabRole |
| Deployment Type | ZIP Package |

Environment variables:

| Variable | Value |
|---|---|
| BUCKET_NAME | labinventory-534903-20261125 |
| OBJECT_KEY | inventory.json |

Bukti menunjukkan bahwa komponen pemrosesan aplikasi telah berhasil dikonfigurasi dan source code telah berhasil di-deploy.

AWS Lambda digunakan untuk menjalankan logika CRUD, validasi data, komunikasi dengan Amazon S3, serta pembentukan response aplikasi.

### 4.5 IAM and Service Permissions

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-13 | aws_lambda_s3_permissions.png | Informasi izin akses Lambda terhadap Amazon S3 | Collected |
| EV-14 | aws_lambda_cloudwatch_permissions.png | Informasi izin pencatatan Amazon CloudWatch | Collected |

Total: 2 screenshots.

Lambda menggunakan execution role `LabRole` yang disediakan oleh lingkungan AWS Academy Sandbox.

Execution role mendukung akses terhadap layanan yang diperlukan, antara lain:

- Membaca objek inventaris pada Amazon S3.
- Menulis perubahan data inventaris pada Amazon S3.
- Menghasilkan log eksekusi melalui Amazon CloudWatch.

Operasi penyimpanan yang digunakan oleh aplikasi:

- `s3:GetObject`
- `s3:PutObject`

Bukti menunjukkan konfigurasi izin layanan yang mendukung akses penyimpanan dan pencatatan log.

Implementasi tidak mengklaim penerapan custom least-privilege IAM policy secara penuh karena menggunakan execution role yang disediakan oleh lingkungan sandbox.

Penerapan IAM policy dengan izin yang lebih spesifik merupakan rekomendasi pengembangan untuk lingkungan produksi.

### 4.6 AWS Functional Testing

| ID | Filename | Description | Result |
|---|---|---|---|
| EV-15 | aws_test_get_initial_inventory.png | GET initial inventory | PASS - 200 |
| EV-16 | aws_test_post_create_barang.png | POST create barang | PASS - 201 |
| EV-17 | aws_test_get_read_barang.png | GET read barang | PASS - 200 |
| EV-18 | aws_test_put_update_barang.png | PUT update barang | PASS - 200 |
| EV-19 | aws_test_get_verify_update.png | GET verify updated data | PASS - 200 |
| EV-20 | aws_test_delete_barang.png | DELETE barang | PASS - 200 |
| EV-21 | aws_test_get_final_verification.png | GET verification after delete | PASS - 200 |
| EV-22 | aws_test_post_invalid_jumlah.png | Validasi jumlah negatif | PASS - 400 |
| EV-23 | aws_test_delete_not_found.png | Penanganan ID barang tidak ditemukan | PASS - 404 |

Total: 9 screenshots.

Seluruh screenshot pada kategori ini telah dikumpulkan.

Pengujian dilakukan melalui Lambda Test Event.

Status code merupakan response aplikasi yang dikembalikan oleh Lambda handler.

Status 400 dan 404 merupakan hasil yang diharapkan pada skenario negative testing.

#### Test Data

| Attribute | Initial Value | Updated Value |
|---|---|---|
| id_barang | BRG-DAC9867BF6AC | BRG-DAC9867BF6AC |
| nama_barang | Arduino Uno | Arduino Uno |
| kategori | Mikrokontroler | Mikrokontroler |
| jumlah | 15 | 12 |
| kondisi | Baik | Rusak Ringan |

#### CRUD Testing Summary

| Operation | Endpoint | Expected Status | Result |
|---|---|---:|---|
| Create | POST /barang | 201 | PASS |
| Read | GET /barang | 200 | PASS |
| Update | PUT /barang/{id_barang} | 200 | PASS |
| Delete | DELETE /barang/{id_barang} | 200 | PASS |

#### Negative Testing Summary

| Scenario | Expected Status | Result |
|---|---:|---|
| Jumlah barang negatif | 400 | PASS |
| ID barang tidak ditemukan | 404 | PASS |

#### Final Data Verification

Setelah seluruh pengujian selesai, barang berhasil dihapus dan inventaris kembali berisi array kosong.

Response akhir:

```json
{
    "message": "Data inventaris berhasil dibaca.",
    "total": 0,
    "data": []
}
```

Hasil pengujian menunjukkan bahwa seluruh operasi CRUD dan skenario validasi yang diuji telah berjalan sesuai expected result.

### 4.7 Amazon CloudWatch Monitoring

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-24 | aws_cloudwatch_log_group.png | Log group Lambda tersedia | Collected |
| EV-25 | aws_cloudwatch_log_events.png | Informasi request dan log eksekusi Lambda | Collected |

Total: 2 screenshots.

Log group:

```text
/aws/lambda/labinventory-crud
```

Bukti menunjukkan bahwa Lambda berhasil menghasilkan log eksekusi melalui Amazon CloudWatch.

Informasi log digunakan untuk membantu:

- Monitoring eksekusi Lambda.
- Pemeriksaan request aplikasi.
- Identifikasi kesalahan.
- Troubleshooting.
- Pemeriksaan durasi eksekusi dan penggunaan memory.

CloudWatch digunakan sebagai komponen monitoring dasar dalam arsitektur LabInventory.

### 4.8 HTTP Interface and Connectivity

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-26 | aws_lambda_function_url.png | Konfigurasi Lambda Function URL dengan AWS_IAM | Collected |
| EV-27 | aws_http_connectivity_test.png | Pengujian HTTPS melalui AWS CloudShell | Collected |

Total: 2 screenshots.

Konfigurasi antarmuka:

| Configuration | Value |
|---|---|
| Interface | Lambda Function URL |
| Authentication | AWS_IAM |
| Invoke Mode | BUFFERED |
| Protocol | HTTPS |
| Request Authentication | AWS Signature Version 4 |
| Test Client | AWS CloudShell |
| Tested Method | GET |
| Tested Endpoint | /barang |

Hasil pengujian HTTP aktual:

```text
HTTP Status: 200
```

Response body:

```json
{
    "message": "Data inventaris berhasil dibaca.",
    "total": 0,
    "data": []
}
```

Pengujian menunjukkan bahwa client yang memiliki kredensial dan izin AWS yang sesuai dapat mengakses Lambda Function URL melalui request HTTPS yang ditandatangani menggunakan AWS Signature Version 4.

Pengujian HTTP langsung dilakukan menggunakan metode `GET /barang`.

Pengujian seluruh operasi CRUD dilakukan melalui Lambda Test Event.

Dengan demikian, pengujian konektivitas HTTP aktual dibedakan dari pengujian fungsional seluruh operasi CRUD.

Function URL tidak dicantumkan secara langsung pada dokumentasi publik.

### 4.9 Amazon S3 Security Configuration

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-28 | aws_s3_block_public_access.png | Block All Public Access aktif | Collected |
| EV-29 | aws_s3_default_encryption.png | Default encryption menggunakan SSE-S3 | Collected |

Total: 2 screenshots.

Konfigurasi keamanan:

| Security Configuration | Value |
|---|---|
| Block All Public Access | Enabled |
| Default Encryption | Enabled |
| Encryption Type | SSE-S3 |
| Public Storage Access | Not Configured |
| HTTP Interface Authentication | AWS_IAM |

Bukti menunjukkan konfigurasi keamanan dasar penyimpanan Amazon S3.

Bucket tidak dikonfigurasi untuk memberikan akses publik dan menggunakan enkripsi penyimpanan dengan kunci yang dikelola Amazon S3.

Akses terhadap data inventaris dilakukan melalui Lambda yang menggunakan execution role sesuai lingkungan AWS Academy Sandbox.

---

## 5. Evidence Summary

| Evidence Category | Total | Collected |
|---|---:|---:|
| Local Development and Testing | 2 | 2 |
| AWS Environment | 2 | 2 |
| Amazon S3 Provisioning and Storage | 3 | 3 |
| AWS Lambda Provisioning and Configuration | 5 | 5 |
| IAM and Service Permissions | 2 | 2 |
| AWS Functional Testing | 9 | 9 |
| Amazon CloudWatch Monitoring | 2 | 2 |
| HTTP Interface and Connectivity | 2 | 2 |
| Amazon S3 Security Configuration | 2 | 2 |
| Final Repository Evidence | 2 | 2 |
| Final Architecture Diagram | 1 | 1 |
| **Total** | **32** | **32** |

Sebanyak 32 screenshot telah dikumpulkan untuk mendokumentasikan pengembangan, provisioning, konfigurasi, pengujian, dan finalisasi LabInventory.

Jumlah tersebut terdiri atas:

- 29 screenshot teknis.
- 2 screenshot dokumentasi repository.
- 1 screenshot diagram arsitektur final.

Seluruh bukti mentah disimpan secara lokal dan tidak diunggah ke repository publik.

---

## 6. Additional Final Documentation Evidence

Bukti tambahan telah dikumpulkan pada tahap finalisasi repository dan dokumentasi.

| ID | Filename | Description | Status |
|---|---|---|---|
| EV-30 | final_github_repository.png | Tampilan repository GitHub final | Collected |
| EV-31 | final_git_commit_history.png | Riwayat commit pengembangan | Collected |
| EV-32 | final_architecture_diagram.png | Diagram arsitektur final | Collected |

Total: 3 screenshots.

### 6.1 GitHub Repository Evidence

Repository:

https://github.com/aurelia-mutiah/labinventory-cloud

Branch:

```text
main
```

Repository berisi:

- Source code aplikasi.
- Automated tests.
- Dokumentasi arsitektur.
- Design brief.
- Deployment plan.
- Testing plan.
- Evidence documentation.
- Dependency configuration.
- Git ignore configuration.

Bukti repository menunjukkan bahwa source code, dokumentasi, dan konfigurasi proyek telah dikelola menggunakan Git dan GitHub.

### 6.2 Git Commit History Evidence

Riwayat commit:

https://github.com/aurelia-mutiah/labinventory-cloud/commits/main/

Riwayat commit mendokumentasikan perkembangan proyek secara bertahap, mulai dari inisialisasi repository, pengembangan aplikasi, pengujian, hingga finalisasi dokumentasi.

Progressive commits digunakan untuk menunjukkan proses pengembangan dan pengelolaan perubahan proyek.

### 6.3 Final Architecture Diagram Evidence

Diagram arsitektur tersedia pada README utama dan dokumentasi arsitektur.

Diagram telah berhasil dirender pada GitHub menggunakan Mermaid.

Komponen yang ditampilkan:

- Authorized Client / AWS CloudShell.
- AWS Lambda Console Tester.
- Lambda Function URL dengan AWS_IAM.
- AWS Lambda Python CRUD Handler.
- AWS IAM LabRole.
- Amazon S3 Private Bucket.
- Amazon CloudWatch.
- AWS Region us-east-1.

Diagram menggambarkan request flow, data flow, execution permissions, konektivitas HTTPS, dan hubungan antar layanan yang digunakan pada implementasi aktual.

Ketiga screenshot dokumentasi final telah dihitung dalam total 32 screenshot pada Evidence Summary.

---

## 7. Screenshot Guidelines

Setiap screenshot harus:

- Menampilkan informasi yang relevan.
- Memiliki teks yang dapat dibaca.
- Menampilkan konfigurasi atau hasil aktual.
- Menghindari pemotongan informasi penting.
- Menggunakan penamaan file yang jelas.
- Tidak menampilkan kredensial AWS pada salinan yang dibagikan.
- Tidak menampilkan token atau informasi rahasia pada salinan yang dibagikan.
- Tidak menampilkan presigned URL atau session token pada salinan yang dibagikan.

Informasi seperti account ID, ARN lengkap, alamat email, dan detail akun dapat disamarkan apabila tidak diperlukan sebagai bukti.

Screenshot asli disimpan secara lokal.

Apabila diperlukan penyensoran, perubahan dilakukan pada salinan screenshot, bukan pada file asli.

Penyensoran tidak boleh mengubah hasil pengujian atau konfigurasi teknis yang menjadi bukti.

---

## 8. Evidence Status Classification

| Status | Description |
|---|---|
| Collected | Bukti telah dikumpulkan |
| Pending | Bukti belum dikumpulkan |
| PASS | Hasil pengujian sesuai expected result |
| FAIL | Hasil pengujian tidak sesuai expected result |
| Blocked | Bukti tidak dapat dikumpulkan karena kendala |
| Not Applicable | Bukti tidak relevan pada implementasi final |
| In Progress | Proses dokumentasi atau finalisasi masih berlangsung |

Status Collected menunjukkan bahwa file bukti telah tersedia.

Status PASS menunjukkan bahwa hasil pengujian sesuai dengan expected result.

Ketersediaan screenshot tidak secara otomatis membuktikan seluruh aspek keamanan atau kualitas sistem telah diuji.

---

## 9. Evidence Security

Folder `evidence/raw/` telah dimasukkan ke dalam `.gitignore` agar screenshot mentah tidak ikut terunggah ke repository publik.

Aturan pengecualian:

```gitignore
/evidence/raw/
/evidence/private/
```

Pemeriksaan aturan Git dilakukan menggunakan:

```bash
git check-ignore evidence/raw/aws_s3_final_inventory.png
```

Hasil pemeriksaan:

```text
evidence/raw/aws_s3_final_inventory.png
```

Pemeriksaan file yang dilacak dilakukan menggunakan:

```bash
git ls-files evidence/raw
```

Hasil pemeriksaan tidak menampilkan file apa pun.

Hasil tersebut menunjukkan bahwa folder `evidence/raw/` tidak memiliki file yang sedang dilacak oleh Git.

Pemeriksaan ini tidak mencakup audit menyeluruh terhadap seluruh riwayat commit.

Sebelum screenshot dimasukkan ke laporan akhir, lakukan pemeriksaan terhadap informasi sensitif.

Informasi yang tidak boleh dibagikan meliputi:

- AWS Access Key ID.
- AWS Secret Access Key.
- AWS Session Token.
- Password.
- Private key.
- Presigned URL beserta parameter autentikasinya.
- Informasi autentikasi lainnya.

Alamat Function URL dan informasi identitas akun dapat disamarkan apabila tidak diperlukan untuk keperluan penilaian.

Screenshot mentah tetap disimpan secara lokal dan tidak diunggah ke repository publik.

---

## 10. Evidence Selection for Final Report

Tidak seluruh screenshot harus dimasukkan ke dalam bagian utama laporan.

Pemilihan bukti dilakukan berdasarkan relevansi terhadap tujuan tugas Cloud Computing.

### 10.1 Development Evidence

- Hasil 35 automated local tests.
- Repository GitHub final.
- Riwayat commit pengembangan.

### 10.2 Architecture Evidence

- Diagram arsitektur final.
- Konfigurasi region AWS.
- Hubungan antara Lambda, S3, IAM, Function URL, dan CloudWatch.

### 10.3 Infrastructure Evidence

- Bucket Amazon S3.
- Objek inventory.json.
- Lambda function.
- Source code deployment.
- Runtime dan handler.
- Environment variables.
- General configuration.

### 10.4 Security Evidence

- IAM execution role dan service permissions.
- S3 Block Public Access.
- S3 default encryption.
- Lambda Function URL dengan AWS_IAM.

### 10.5 Functional Testing Evidence

- Initial inventory verification.
- Create barang.
- Read barang.
- Update barang.
- Verifikasi hasil update.
- Delete barang.
- Verifikasi setelah delete.
- Validasi jumlah negatif.
- Penanganan ID barang tidak ditemukan.

### 10.6 Connectivity and Monitoring Evidence

- Pengujian HTTPS melalui AWS CloudShell.
- CloudWatch log group.
- CloudWatch log events.
- Isi akhir inventory.json.

Bukti utama dapat ditempatkan pada bagian implementasi dan pengujian laporan.

Screenshot tambahan dapat disertakan pada bagian lampiran agar laporan utama tetap terstruktur.

Seluruh screenshot yang dipilih perlu diperiksa keterbacaan dan keamanan informasinya sebelum laporan diselesaikan.

---

## 11. Relationship with Project Documentation

| Document | Relationship |
|---|---|
| [Architecture Documentation](../docs/architecture.md) | Diagram, konfigurasi, dan keputusan arsitektur |
| [Design Brief](../docs/design-brief.md) | Gambaran sistem, tujuan, model data, dan hasil implementasi |
| [Deployment Plan](../docs/deployment-plan.md) | Prosedur provisioning dan deployment AWS |
| [Testing Plan](../docs/testing-plan.md) | Skenario, hasil, dan referensi bukti pengujian |
| [Project README](../README.md) | Gambaran umum repository dan panduan penggunaan |
| [Evidence Documentation](README.md) | Indeks bukti pengembangan dan implementasi |

Seluruh dokumentasi harus konsisten dengan konfigurasi aktual dan hasil pengujian.

---

## 12. Current Status

| Evidence Category | Status |
|---|---|
| Local Development Evidence | Collected |
| AWS Environment Evidence | Collected |
| AWS Provisioning Evidence | Collected |
| AWS Configuration Evidence | Collected |
| AWS Functional Testing Evidence | Collected |
| AWS Security Evidence | Collected |
| CloudWatch Monitoring Evidence | Collected |
| HTTP Connectivity Evidence | Collected |
| Final Repository Evidence | Collected |
| Final Architecture Diagram Evidence | Collected |
| Final Report Evidence Selection | In Progress |

### 12.1 Final Evidence Summary

| Category | Result |
|---|---|
| Technical Screenshots | 29 |
| Final Documentation Screenshots | 3 |
| Total Screenshots | 32 |
| Local Automated Tests | 35/35 Passed |
| AWS Lambda Functional Tests | 9/9 Passed |
| HTTPS Connectivity Test | HTTP 200 |
| Final Inventory Verification | Empty Array |
| GitHub Repository | Available |
| Architecture Diagram | Available |

### 12.2 Completion Status

**Technical Evidence Status: Collected**

**Final Documentation Evidence Status: Collected**

**Overall Evidence Collection Status: COMPLETED**

**Final Report Status: IN PROGRESS**

Bukti teknis utama LabInventory telah dikumpulkan dan mencakup pengembangan lokal, deployment AWS, pengujian CRUD, konektivitas HTTPS, keamanan dasar, persistensi data, serta monitoring.

Bukti repository final, riwayat commit, dan diagram arsitektur juga telah dikumpulkan.

Seluruh bukti disimpan secara lokal untuk mendukung penyusunan laporan akhir tugas Cloud Computing.

Pemilihan dan penyesuaian bukti pada laporan akhir masih dalam tahap finalisasi.

---

## Repository

https://github.com/aurelia-mutiah/labinventory-cloud

Developed for Cloud Computing coursework.
