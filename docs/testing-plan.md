
# Testing Plan — LabInventory

## 1. Testing Objective

Pengujian dilakukan untuk memastikan bahwa sistem
LabInventory dapat menjalankan operasi CRUD,
memvalidasi data masukan, menangani kesalahan,
dan mengakses layanan penyimpanan cloud.

Pengujian juga bertujuan untuk memverifikasi
konektivitas HTTPS, konfigurasi keamanan dasar,
persistensi data, dan pencatatan log aplikasi.

Pengujian dilaksanakan pada lingkungan lokal dan
AWS Academy Cloud Foundations Sandbox Lingkungan Hidup.

## 2. Testing Scope

Ruang lingkup pengujian meliputi:

- Logika bisnis pengelolaan inventaris.
- Validasi atribut barang.
- Pembuatan ID barang secara otomatis.
- Penyimpanan data lokal.
- Simulasi integrasi Amazon S3.
- Pemrosesan request oleh Lambda handler.
- Konektivitas AWS Lambda dengan Amazon S3.
- Operasi CRUD pada lingkungan AWS.
- Persistensi data.
- Penanganan kesalahan.
- Konektivitas HTTPS melalui Lambda Function URL.
- Konfigurasi keamanan dasar Amazon S3.
- Konfigurasi IAM execution role.
- Pencatatan log aplikasi melalui CloudWatch.

Pengujian performa skala besar, concurrent write,
antarmuka pengguna, dan autentikasi pengguna aplikasi
tidak termasuk dalam ruang lingkup prototipe.

## 3. Testing Environment

### 3.1 Local Environment

| Komponen | Konfigurasi |
|---|---|
| Operating System | Windows |
| Development Tool | Visual Studio Code |
| Programming Language | Python 3.11.8 |
| Testing Framework | unittest |
| AWS SDK | boto3 |
| Local Storage | JSON File |
| AWS Simulation | Mock dan Botocore Stubber |
| Version Control | Git dan GitHub |
| Virtual Environment | .venv |

### 3.2 Cloud Environment

| Komponen | Konfigurasi Aktual |
|---|---|
| Environment | AWS Academy Cloud Foundations Sandbox Lingkungan Hidup |
| Region | US East (N. Virginia) |
| Region Code | us-east-1 |
| Compute | AWS Lambda |
| Function Name | labinventory-crud |
| Runtime | Python 3.11 |
| Memory | 128 MB |
| Timeout | 15 seconds |
| Storage | Amazon S3 |
| Bucket Name | labinventory-534903-20261125 |
| Object Key | inventory.json |
| Access Control | AWS IAM |
| Execution Role | LabRole |
| HTTP Interface | Lambda Function URL |
| HTTP Authentication | AWS_IAM |
| Monitoring | Amazon CloudWatch |
| Testing Interface | Lambda Console dan AWS CloudShell |

## 4. Local Automated Testing

### 4.1 Inventory Unit Testing

File pengujian:

tests/test_inventory.py

Pengujian mencakup:

- Penambahan data barang.
- Pembacaan data inventaris.
- Pembaruan data barang.
- Penghapusan data barang.
- Inventaris kosong.
- Validasi atribut wajib.
- Validasi nama barang.
- Validasi jumlah barang.
- Validasi kondisi barang.
- Penanganan ID yang tidak ditemukan.
- Keunikan ID barang.
- Persistensi data.
- Validasi sample data.
- Penanganan format penyimpanan tidak valid.

Perintah pengujian:

```bash
python -m unittest tests.test_inventory -v
```

Hasil pengujian:

- Total tests: 20.
- Passed: 20.
- Failed: 0.
- Status: PASS.

### 4.2 AWS Integration Simulation

File pengujian:

tests/test_aws_integration.py

Pengujian mencakup:

- Simulasi pembacaan objek Amazon S3.
- Simulasi penyimpanan objek Amazon S3.
- Penanganan objek yang tidak ditemukan.
- Penanganan AccessDenied.
- Penanganan JSON yang tidak valid.
- Pemrosesan operasi CRUD oleh Lambda handler.
- Validasi request.
- Penanganan endpoint yang tidak ditemukan.
- Penanganan HTTP method yang tidak didukung.
- Pemrosesan event HTTP versi 2.
- Penanganan kesalahan penyimpanan.

Pengujian menggunakan Mock dan Botocore Stubber
untuk mensimulasikan interaksi dengan layanan AWS
tanpa menggunakan resource cloud aktual.

Perintah pengujian:

```bash
python -m unittest tests.test_aws_integration -v
```

Hasil pengujian:

- Total tests: 15.
- Passed: 15.
- Failed: 0.
- Status: PASS.

### 4.3 Combined Testing

Seluruh pengujian otomatis dijalankan menggunakan:

```bash
python -m unittest discover -s tests -v
```

### 4.4 Local Testing Results

| Test Suite | Total | Passed | Failed | Result |
|---|---:|---:|---:|---|
| Inventory Unit Testing | 20 | 20 | 0 | PASS |
| AWS Integration Simulation | 15 | 15 | 0 | PASS |
| Total | 35 | 35 | 0 | PASS |

Success rate: 100%.

Seluruh pengujian otomatis lokal berhasil dijalankan.

Simulasi integrasi AWS merupakan pengujian terhadap
perilaku aplikasi dan adapter penyimpanan secara lokal,
bukan pengujian terhadap infrastruktur AWS aktual.

Pengujian cloud dilakukan secara terpisah setelah
provisioning selesai.

## 5. Cloud Testing Prerequisites

Sebelum pengujian cloud dilakukan, konfigurasi berikut
telah disiapkan:

- Sesi AWS Academy Sandbox aktif.
- Bucket Amazon S3 tersedia.
- S3 Block Public Access aktif.
- Objek inventory.json telah diinisialisasi.
- Lambda function telah dibuat.
- Deployment package telah diunggah.
- Lambda handler telah dikonfigurasi.
- Environment variables telah dikonfigurasi.
- Execution role LabRole telah digunakan.

Pengujian awal menggunakan inventory.json dengan
isi berupa array JSON kosong:

```json
[]
```

Data yang digunakan merupakan data contoh untuk
kebutuhan pengujian, bukan data inventaris
laboratorium aktual.

## 6. Cloud Functional Test Cases

| ID | Test Scenario | Expected Status | Actual Status | Result |
|---|---|---:|---:|---|
| CT-01 | Initial inventory connectivity | 200 | 200 | PASS |
| CT-02 | Create barang | 201 | 201 | PASS |
| CT-03 | Read barang | 200 | 200 | PASS |
| CT-04 | Update barang | 200 | 200 | PASS |
| CT-05 | Verify updated data | 200 | 200 | PASS |
| CT-06 | Delete barang | 200 | 200 | PASS |
| CT-07 | Read after delete | 200 | 200 | PASS |
| CT-08 | Invalid quantity | 400 | 400 | PASS |
| CT-09 | Delete barang not found | 404 | 404 | PASS |

Seluruh sembilan skenario dijalankan melalui AWS
Lambda Console menggunakan Lambda Test Event.

Status code pada tabel merupakan status aplikasi
yang dikembalikan oleh Lambda handler.

Status tersebut berbeda dari status HTTP aktual
yang diperoleh melalui Lambda Function URL.

## 7. Cloud Testing Procedure and Results

Contoh event pada bagian ini dapat digunakan untuk
mereplikasi skenario pengujian yang telah dilakukan.

### CT-01 — Initial Connectivity Test

Tujuan:

Memastikan Lambda dapat membaca objek inventory.json
pada Amazon S3.

Test event:

```json
{
    "httpMethod": "GET",
    "path": "/barang"
}
```

Expected result:

- Status code 200.
- Response dalam format JSON.
- Total barang bernilai 0.
- Data inventaris berupa array kosong.

Actual result:

- Status code: 200.
- Total: 0.
- Data: [].

Result: PASS.

Evidence:

aws_test_get_initial_inventory.png

### CT-02 — Create Barang

Tujuan:

Memastikan sistem dapat menambahkan barang baru,
membuat ID secara otomatis, dan menyimpan data
pada Amazon S3.

Test event:

```json
{
    "httpMethod": "POST",
    "path": "/barang",
    "body": "{\"nama_barang\":\"Arduino Uno\",\"kategori\":\"Mikrokontroler\",\"jumlah\":15,\"kondisi\":\"Baik\"}"
}
```

Expected result:

- Status code 201.
- ID barang dibuat secara otomatis.
- Data barang berhasil disimpan.

Actual result:

- Status code: 201.
- Message: Barang berhasil ditambahkan.
- ID barang: BRG-DAC9867BF6AC.
- Nama barang: Arduino Uno.
- Kategori: Mikrokontroler.
- Jumlah: 15.
- Kondisi: Baik.

Result: PASS.

Evidence:

aws_test_post_create_barang.png

### CT-03 — Read Barang

Tujuan:

Memastikan barang yang telah ditambahkan dapat
dibaca kembali dari penyimpanan.

Test event:

```json
{
    "httpMethod": "GET",
    "path": "/barang"
}
```

Expected result:

- Status code 200.
- Data Arduino Uno muncul dalam daftar.
- Jumlah barang sesuai dengan data sebelumnya.

Actual result:

- Status code: 200.
- Total: 1.
- ID barang: BRG-DAC9867BF6AC.
- Nama barang: Arduino Uno.
- Jumlah: 15.
- Kondisi: Baik.

Result: PASS.

Evidence:

aws_test_get_read_barang.png

### CT-04 — Update Barang

Tujuan:

Memastikan atribut barang dapat diperbarui tanpa
mengubah identitas unik barang.

Test event:

```json
{
    "httpMethod": "PUT",
    "path": "/barang/BRG-DAC9867BF6AC",
    "body": "{\"nama_barang\":\"Arduino Uno\",\"kategori\":\"Mikrokontroler\",\"jumlah\":12,\"kondisi\":\"Rusak Ringan\"}"
}
```

Expected result:

- Status code 200.
- Jumlah barang berubah dari 15 menjadi 12.
- Kondisi berubah dari Baik menjadi Rusak Ringan.
- ID barang tetap sama.

Actual result:

- Status code: 200.
- ID barang: BRG-DAC9867BF6AC.
- Nama barang: Arduino Uno.
- Kategori: Mikrokontroler.
- Jumlah: 12.
- Kondisi: Rusak Ringan.

Result: PASS.

Evidence:

aws_test_put_update_barang.png

Apabila pengujian dilakukan kembali, ID pada path
harus diganti dengan ID yang dihasilkan oleh
operasi Create terbaru.

### CT-05 — Verify Updated Data

Tujuan:

Memastikan perubahan data hasil operasi Update
dapat dibaca kembali melalui Lambda.

Test event:

```json
{
    "httpMethod": "GET",
    "path": "/barang"
}
```

Expected result:

- Status code 200.
- Total data bernilai 1.
- Jumlah barang bernilai 12.
- Kondisi barang bernilai Rusak Ringan.
- ID barang tidak berubah.

Actual result:

- Status code: 200.
- Total: 1.
- ID barang: BRG-DAC9867BF6AC.
- Jumlah: 12.
- Kondisi: Rusak Ringan.

Result: PASS.

Evidence:

aws_test_get_verify_update.png

Pengujian ini menunjukkan bahwa perubahan data
dapat dibaca kembali pada invocation berikutnya.

### CT-06 — Delete Barang

Tujuan:

Memastikan barang dapat dihapus berdasarkan ID.

Test event:

```json
{
    "httpMethod": "DELETE",
    "path": "/barang/BRG-DAC9867BF6AC"
}
```

Expected result:

- Status code 200.
- Barang berhasil dihapus dari daftar inventaris.
- Response memuat data barang yang dihapus.

Actual result:

- Status code: 200.
- ID barang yang dihapus: BRG-DAC9867BF6AC.
- Operasi penghapusan berhasil.

Result: PASS.

Evidence:

aws_test_delete_barang.png

### CT-07 — Read After Delete

Tujuan:

Memastikan barang yang telah dihapus tidak muncul
kembali pada daftar inventaris.

Test event:

```json
{
    "httpMethod": "GET",
    "path": "/barang"
}
```

Expected result:

- Status code 200.
- Barang yang dihapus tidak muncul kembali.
- Total data bernilai 0.
- Data inventaris berupa array kosong.

Actual result:

- Status code: 200.
- Total: 0.
- Data: [].

Result: PASS.

Evidence:

aws_test_get_final_verification.png

### CT-08 — Invalid Quantity

Tujuan:

Memastikan sistem menolak data barang dengan
jumlah negatif.

Contoh test event untuk mereplikasi pengujian:

```json
{
    "httpMethod": "POST",
    "path": "/barang",
    "body": "{\"nama_barang\":\"Multimeter\",\"kategori\":\"Alat Ukur\",\"jumlah\":-5,\"kondisi\":\"Baik\"}"
}
```

Expected result:

- Status code 400.
- Sistem menolak jumlah negatif.
- Data tidak ditambahkan ke inventaris.

Actual result:

- Status code: 400.
- Message: Jumlah barang tidak boleh negatif.

Result: PASS.

Evidence:

aws_test_post_invalid_jumlah.png

Status 400 merupakan response yang diharapkan
pada pengujian validasi input.

### CT-09 — Delete Barang Not Found

Tujuan:

Memastikan sistem menangani permintaan penghapusan
terhadap ID barang yang tidak tersedia.

Test event:

```json
{
    "httpMethod": "DELETE",
    "path": "/barang/BRG-NOTFOUND"
}
```

Expected result:

- Status code 404.
- Sistem memberikan informasi bahwa barang
  tidak ditemukan.
- Data inventaris tidak berubah.

Actual result:

- Status code: 404.
- Message: Barang dengan ID BRG-NOTFOUND tidak ditemukan.

Result: PASS.

Evidence:

aws_test_delete_not_found.png

Status 404 merupakan response yang diharapkan
pada skenario barang tidak ditemukan.

## 8. Infrastructure and Connectivity Verification

### IV-01 — Final S3 Storage Verification

Tujuan:

Memastikan isi akhir objek inventory.json sesuai
dengan hasil rangkaian pengujian CRUD.

Prosedur:

1. Membuka layanan Amazon S3.
2. Membuka bucket labinventory-534903-20261125.
3. Memilih objek inventory.json.
4. Membuka isi objek.
5. Memeriksa data inventaris akhir.

Expected result:

```json
[]
```

Actual result:

```json
[]
```

Objek inventory.json tetap tersedia dengan ukuran
2 bytes dan berisi array JSON kosong.

Result: PASS.

Evidence:

aws_s3_final_inventory.png

### IV-02 — CloudWatch Log Verification

Tujuan:

Memastikan Lambda dapat menghasilkan log eksekusi
melalui Amazon CloudWatch.

Log group:

/aws/lambda/labinventory-crud

Prosedur:

1. Membuka layanan Amazon CloudWatch.
2. Membuka log group Lambda.
3. Memilih log stream yang tersedia.
4. Memeriksa informasi request dan eksekusi.

Actual result:

- Log group tersedia.
- Log stream tersedia.
- Informasi START, END, dan REPORT tersedia.
- Informasi request aplikasi tersedia.
- Informasi durasi dan penggunaan memori tersedia.

Result: PASS.

Evidence:

- aws_cloudwatch_log_group.png
- aws_cloudwatch_log_events.png

### IV-03 — HTTP Interface Configuration

Tujuan:

Memastikan aplikasi memiliki antarmuka HTTPS
dengan mekanisme autentikasi yang sesuai.

Actual configuration:

| Parameter | Value |
|---|---|
| Interface | Lambda Function URL |
| Authentication | AWS_IAM |
| Invoke Mode | BUFFERED |
| Protocol | HTTPS |
| CORS | Not enabled |

Result: PASS.

Evidence:

aws_lambda_function_url.png

### IV-04 — Authenticated HTTP Connectivity

Tujuan:

Memastikan client yang memiliki autentikasi dan
otorisasi AWS dapat mengakses aplikasi melalui
endpoint HTTPS aktual.

Testing environment:

- AWS CloudShell.
- Python.
- boto3.
- Botocore SigV4Auth.
- AWS session credentials.

Request:

- Method: GET.
- Path: /barang.
- Authentication: AWS Signature Version 4.

Expected result:

- HTTP Status 200.
- Response dalam format JSON.
- Data inventaris sesuai dengan penyimpanan.

Actual result:

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

Result: PASS.

Evidence:

aws_http_connectivity_test.png

Pengujian ini merupakan pengujian HTTP aktual,
berbeda dari direct invocation melalui Lambda Console.

Pengujian HTTP langsung hanya dilakukan pada metode
GET. Operasi POST, PUT, dan DELETE diuji melalui
Lambda Test Event.

### IV-05 — S3 Public Access Verification

Tujuan:

Memastikan bucket tidak dikonfigurasi untuk
memberikan akses publik.

Expected configuration:

Block All Public Access: On.

Actual configuration:

Block All Public Access: On.

Result: PASS.

Evidence:

aws_s3_block_public_access.png

### IV-06 — S3 Encryption Verification

Tujuan:

Memastikan konfigurasi enkripsi penyimpanan
Amazon S3 telah diaktifkan.

Expected configuration:

Server-side encryption with Amazon S3 managed
keys (SSE-S3).

Actual configuration:

SSE-S3.

Result: PASS.

Evidence:

aws_s3_default_encryption.png

### IV-07 — IAM Execution Role Verification

Tujuan:

Memastikan Lambda menggunakan execution role
yang tersedia pada lingkungan sandbox.

Actual configuration:

- Execution role: LabRole.
- Akses Amazon S3 berhasil digunakan.
- Pencatatan CloudWatch berhasil digunakan.

Result: PASS.

Evidence:

- aws_lambda_s3_permissions.png
- aws_lambda_cloudwatch_permissions.png

Pengujian ini memverifikasi konfigurasi role dan
keberhasilan akses layanan yang diperlukan aplikasi.

Pengujian tidak mencakup audit seluruh kebijakan IAM
atau pembuktian penerapan least privilege secara penuh.

## 9. Testing Evidence

Screenshot pengujian disimpan pada folder:

evidence/raw/

### 9.1 Local Testing Evidence

| File | Description |
|---|---|
| 01_local_unit_testing.png | Hasil 20 unit tests |
| 02_combined_testing.png | Hasil 35 automated tests |

### 9.2 AWS Functional Testing Evidence

| File | Description |
|---|---|
| aws_test_get_initial_inventory.png | Initial connectivity test |
| aws_test_post_create_barang.png | Create barang |
| aws_test_get_read_barang.png | Read barang |
| aws_test_put_update_barang.png | Update barang |
| aws_test_get_verify_update.png | Verifikasi data setelah update |
| aws_test_delete_barang.png | Delete barang |
| aws_test_get_final_verification.png | Verifikasi setelah delete |
| aws_test_post_invalid_jumlah.png | Validasi jumlah negatif |
| aws_test_delete_not_found.png | Penanganan ID tidak ditemukan |

### 9.3 Infrastructure Verification Evidence

| File | Description |
|---|---|
| aws_s3_final_inventory.png | Isi akhir inventory.json |
| aws_cloudwatch_log_group.png | CloudWatch log group |
| aws_cloudwatch_log_events.png | Log eksekusi Lambda |
| aws_lambda_function_url.png | Konfigurasi Function URL |
| aws_http_connectivity_test.png | Hasil pengujian HTTPS |
| aws_s3_block_public_access.png | Konfigurasi Block Public Access |
| aws_s3_default_encryption.png | Konfigurasi SSE-S3 |
| aws_lambda_s3_permissions.png | Informasi izin akses S3 |
| aws_lambda_cloudwatch_permissions.png | Informasi izin CloudWatch |

Bukti provisioning dan konfigurasi lainnya
didokumentasikan pada evidence/README.md.

Screenshot mentah tidak dilacak oleh Git dan
tidak diunggah langsung ke repository publik.

Informasi sensitif perlu disensor sebelum screenshot
disertakan dalam laporan atau dibagikan kepada
pihak lain.

## 10. Test Result Classification

| Status | Description |
|---|---|
| PASS | Hasil aktual sesuai expected result |
| FAIL | Hasil aktual tidak sesuai expected result |
| NOT TESTED | Pengujian belum dilaksanakan |
| BLOCKED | Pengujian terhambat kendala teknis |
| NOT APPLICABLE | Pengujian tidak relevan pada konfigurasi final |

Status PASS hanya diberikan pada skenario yang
telah dilaksanakan dan memiliki hasil aktual.

Status 400 dan 404 pada negative testing dapat
diklasifikasikan sebagai PASS apabila sesuai
dengan expected result.

## 11. Testing Summary

### 11.1 Automated Local Testing

| Category | Total | Passed | Failed |
|---|---:|---:|---:|
| Inventory Unit Testing | 20 | 20 | 0 |
| AWS Integration Simulation | 15 | 15 | 0 |
| Total | 35 | 35 | 0 |

Local automated testing success rate: 100%.

### 11.2 AWS Functional Testing

| Category | Total | Passed | Failed |
|---|---:|---:|---:|
| Positive Functional Testing | 7 | 7 | 0 |
| Negative Functional Testing | 2 | 2 | 0 |
| Total | 9 | 9 | 0 |

AWS functional testing success rate: 100%.

### 11.3 Infrastructure Verification

| Verification | Result |
|---|---|
| Final S3 storage | PASS |
| CloudWatch Logs | PASS |
| Function URL configuration | PASS |
| Authenticated HTTP connectivity | PASS |
| S3 Block Public Access | PASS |
| S3 default encryption | PASS |
| IAM execution role | PASS |

Seluruh pemeriksaan infrastruktur yang tercantum
pada bagian ini telah berhasil dilakukan.

Persentase keberhasilan hanya berlaku untuk
skenario yang benar-benar dilaksanakan.

## 12. Testing Limitations

Pengujian yang belum dilakukan atau berada di luar
ruang lingkup prototipe meliputi:

| Test Scenario | Status |
|---|---|
| Direct HTTP POST request | NOT TESTED |
| Direct HTTP PUT request | NOT TESTED |
| Direct HTTP DELETE request | NOT TESTED |
| Invalid endpoint pada AWS aktual | NOT TESTED |
| Unauthorized HTTP request | NOT TESTED |
| Concurrent write testing | NOT TESTED |
| Load testing | NOT TESTED |
| Performance benchmarking | NOT TESTED |
| Penetration testing | NOT TESTED |
| Full IAM least-privilege audit | NOT TESTED |
| Frontend testing | NOT APPLICABLE |

Penanganan endpoint tidak valid dan HTTP method
yang tidak didukung telah diuji secara lokal.

Keberhasilan pengujian tidak membuktikan bahwa
sistem telah memenuhi seluruh kebutuhan keamanan,
skalabilitas, dan reliabilitas lingkungan produksi.

## 13. Acceptance Criteria

| Acceptance Criteria | Result |
|---|---|
| Seluruh pengujian otomatis lokal berhasil | PASS |
| Lambda dapat menjalankan source code aplikasi | PASS |
| Lambda dapat membaca data dari S3 | PASS |
| Lambda dapat menulis data ke S3 | PASS |
| Operasi Create berhasil | PASS |
| Operasi Read berhasil | PASS |
| Operasi Update berhasil | PASS |
| Operasi Delete berhasil | PASS |
| Persistensi data dapat diverifikasi | PASS |
| Input jumlah negatif dapat ditangani | PASS |
| ID barang tidak ditemukan dapat ditangani | PASS |
| Endpoint HTTPS berhasil dikonfigurasi | PASS |
| Konektivitas HTTPS terautentikasi berhasil | PASS |
| CloudWatch Logs tersedia | PASS |
| Konfigurasi keamanan dasar S3 terverifikasi | PASS |
| Bukti pengujian tersedia | PASS |

Seluruh acceptance criteria teknis utama prototipe
LabInventory telah terpenuhi.

## 14. Testing Status and Conclusion

**Overall Status: PASSED**

Ringkasan hasil pengujian:

- Local automated testing: 35/35 PASS.
- AWS functional testing: 9/9 PASS.
- Authenticated HTTP connectivity: HTTP 200 OK.
- Final S3 storage verification: PASS.
- CloudWatch Logs verification: PASS.
- Basic storage security verification: PASS.
- IAM execution role verification: PASS.

Hasil pengujian menunjukkan bahwa LabInventory
berhasil menjalankan fungsi utama pengelolaan
inventaris barang laboratorium.

AWS Lambda berhasil terintegrasi dengan Amazon S3
untuk menjalankan seluruh operasi CRUD.

Lambda Function URL berhasil menyediakan akses
HTTPS terautentikasi, sedangkan Amazon CloudWatch
berhasil mencatat informasi eksekusi aplikasi.

Sistem telah memenuhi target fungsional prototipe
akademik dengan batasan pengujian dan implementasi
yang telah didokumentasikan.
