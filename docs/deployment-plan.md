
# Deployment Plan — LabInventory

## 1. Deployment Objective

Deployment dilakukan untuk mengimplementasikan
arsitektur serverless LabInventory pada AWS Academy
Cloud Foundations Sandbox Lingkungan Hidup.

Tujuan deployment meliputi:

- Melakukan provisioning infrastruktur cloud.
- Menjalankan logika aplikasi pada AWS Lambda.
- Menyimpan data inventaris pada Amazon S3.
- Mengintegrasikan Lambda dengan Amazon S3.
- Menerapkan konfigurasi keamanan dasar.
- Menyediakan antarmuka HTTPS terautentikasi.
- Memverifikasi operasi CRUD.
- Memverifikasi persistensi data.
- Memastikan pencatatan log aplikasi tersedia.

## 2. Deployment Environment

| Parameter | Actual Configuration |
|---|---|
| Cloud Provider | Amazon Web Services |
| Environment | AWS Academy Cloud Foundations Sandbox Lingkungan Hidup |
| Region | US East (N. Virginia) |
| Region Code | us-east-1 |
| Architecture | Serverless |
| Compute | AWS Lambda |
| Storage | Amazon S3 |
| Access Control | AWS IAM |
| HTTP Interface | Lambda Function URL |
| Monitoring | Amazon CloudWatch |
| Deployment Method | ZIP Package |
| Programming Language | Python 3.11 |

## 3. Deployment Prerequisites

Persyaratan sebelum deployment:

- Akses AWS Academy Cloud Foundations Sandbox.
- Sesi sandbox aktif.
- Akses AWS Management Console.
- Source code aplikasi tersedia.
- Pengujian lokal telah berhasil.
- Deployment package tersedia.
- Execution role yang diizinkan oleh sandbox.
- Region AWS yang sesuai.
- Ketersediaan layanan Lambda dan Amazon S3.

Seluruh 35 pengujian otomatis lokal telah berhasil
sebelum deployment dilakukan.

## 4. AWS Resource Configuration

### 4.1 Amazon S3

| Parameter | Actual Configuration |
|---|---|
| Bucket Name | labinventory-534903-20261125 |
| Region | us-east-1 |
| Object Key | inventory.json |
| Data Format | JSON |
| Block All Public Access | On |
| Default Encryption | SSE-S3 |

Data awal inventory.json:

```json
[]
```

Amazon S3 digunakan sebagai penyimpanan utama
data inventaris.

Bucket tidak dikonfigurasi untuk memberikan
akses publik.

### 4.2 AWS Lambda

| Parameter | Actual Configuration |
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

Lambda menjalankan logika bisnis, validasi data,
routing request, dan operasi CRUD.

### 4.3 Environment Variables

| Variable | Value |
|---|---|
| BUCKET_NAME | labinventory-534903-20261125 |
| OBJECT_KEY | inventory.json |

Environment variables digunakan agar konfigurasi
penyimpanan tidak ditanamkan langsung pada source code.

### 4.4 AWS IAM

Execution role yang digunakan:

LabRole

Role tersebut disediakan oleh lingkungan
AWS Academy Sandbox.

Izin yang diperlukan oleh aplikasi meliputi:

- Membaca objek Amazon S3.
- Menulis objek Amazon S3.
- Membuat dan mengirimkan log CloudWatch.

Implementasi menggunakan role yang tersedia pada
sandbox dan belum menerapkan custom least-privilege
IAM policy secara penuh.

### 4.5 Lambda Function URL

| Parameter | Actual Configuration |
|---|---|
| Interface | Lambda Function URL |
| Authentication | AWS_IAM |
| Invoke Mode | BUFFERED |
| Protocol | HTTPS |
| CORS | Not enabled |

Function URL menyediakan antarmuka HTTPS untuk
mengakses Lambda menggunakan autentikasi AWS IAM.

Alamat Function URL tidak dicantumkan pada
repository publik.

### 4.6 Amazon CloudWatch

Log group:

/aws/lambda/labinventory-crud

CloudWatch digunakan untuk mencatat:

- Informasi request aplikasi.
- Informasi eksekusi Lambda.
- START, END, dan REPORT.
- Durasi eksekusi.
- Penggunaan memori.
- Informasi kesalahan aplikasi apabila terjadi error.

## 5. Deployment Package

Source code yang digunakan:

```text
src/
├── __init__.py
├── inventory.py
├── lambda_function.py
├── s3_storage.py
└── storage.py
```

Deployment package dibuat menggunakan
Windows PowerShell dari root repository:

```powershell
Compress-Archive -Path .\src -DestinationPath .\labinventory-deployment.zip -Force
```

Nama deployment package:

labinventory-deployment.zip

Folder src harus berada pada root arsip ZIP
agar sesuai dengan konfigurasi handler.

Handler:

src.lambda_function.lambda_handler

Deployment package tidak dimasukkan ke dalam
repository publik.

## 6. Deployment Procedure

### Phase 1 — Sandbox Environment Preparation

Tahapan:

1. Membuka AWS Academy Cloud Foundations.
2. Membuka Sandbox Lingkungan Hidup.
3. Menjalankan sesi sandbox.
4. Membuka AWS Management Console.
5. Memastikan region us-east-1 digunakan.

Result: COMPLETED.

Evidence:

- 03_sandbox_environment.png
- 04_aws_console_region.png

### Phase 2 — Storage Provisioning

Tahapan:

1. Membuka layanan Amazon S3.
2. Membuat bucket labinventory-534903-20261125.
3. Memastikan Block All Public Access aktif.
4. Memastikan default encryption menggunakan SSE-S3.
5. Membuat file inventory.json.
6. Menginisialisasi file dengan array kosong.
7. Mengunggah file ke bucket.

Result: COMPLETED.

Evidence:

- 05_s3_bucket_created.png
- 06_s3_initial_data_uploaded.png
- aws_s3_block_public_access.png
- aws_s3_default_encryption.png

### Phase 3 — Compute Provisioning

Tahapan:

1. Membuka layanan AWS Lambda.
2. Membuat function labinventory-crud.
3. Menggunakan runtime Python 3.11.
4. Menggunakan architecture x86_64.
5. Menggunakan execution role LabRole.
6. Mengunggah deployment package.
7. Mengatur Lambda handler.
8. Mengatur memory menjadi 128 MB.
9. Mengatur timeout menjadi 15 seconds.
10. Mengatur environment variables.
11. Menyimpan konfigurasi.

Result: COMPLETED.

Evidence:

- 07_lambda_function_created.png
- 08_lambda_code_deployed.png
- aws_lambda_runtime_settings.png
- aws_lambda_environment_variables.png
- aws_lambda_general_configuration.png

### Phase 4 — IAM and Service Connectivity

Tahapan:

1. Memeriksa execution role Lambda.
2. Memeriksa izin akses Amazon S3.
3. Memeriksa izin pencatatan CloudWatch.
4. Menjalankan Lambda Test Event.

Initial test event:

```json
{
    "httpMethod": "GET",
    "path": "/barang"
}
```

Actual result:

- Status code: 200.
- Total: 0.
- Data: [].

Result: PASSED.

Evidence:

- aws_lambda_s3_permissions.png
- aws_lambda_cloudwatch_permissions.png
- aws_test_get_initial_inventory.png

### Phase 5 — Functional Testing

Pengujian dilakukan menggunakan Lambda Test Event.

| Test Scenario | Expected | Actual | Result |
|---|---:|---:|---|
| Initial connectivity | 200 | 200 | PASS |
| Create barang | 201 | 201 | PASS |
| Read barang | 200 | 200 | PASS |
| Update barang | 200 | 200 | PASS |
| Verify updated data | 200 | 200 | PASS |
| Delete barang | 200 | 200 | PASS |
| Read after delete | 200 | 200 | PASS |
| Invalid quantity | 400 | 400 | PASS |
| Delete barang not found | 404 | 404 | PASS |

Total functional tests: 9.

Passed: 9.

Failed: 0.

Result: PASSED.

Status code 400 dan 404 merupakan hasil yang
diharapkan pada skenario negative testing.

Prosedur dan hasil pengujian lengkap tersedia
pada docs/testing-plan.md.

### Phase 6 — Monitoring Verification

Tahapan:

1. Membuka layanan Amazon CloudWatch.
2. Membuka log group Lambda.
3. Memilih log stream.
4. Memeriksa informasi request aplikasi.
5. Memeriksa informasi eksekusi Lambda.

Actual result:

- Log group tersedia.
- Log stream tersedia.
- Informasi request aplikasi tersedia.
- Informasi START, END, dan REPORT tersedia.

Result: PASSED.

Evidence:

- aws_cloudwatch_log_group.png
- aws_cloudwatch_log_events.png

### Phase 7 — HTTP Interface Configuration

Tahapan:

1. Membuka konfigurasi Lambda function.
2. Membuka bagian Function URL.
3. Membuat Function URL.
4. Menggunakan authentication type AWS_IAM.
5. Menggunakan invoke mode BUFFERED.
6. Menyimpan konfigurasi.

Result: COMPLETED.

Evidence:

aws_lambda_function_url.png

### Phase 8 — Authenticated HTTP Connectivity

Pengujian dilakukan melalui AWS CloudShell
menggunakan AWS session credentials dan
AWS Signature Version 4.

Request:

- Method: GET.
- Path: /barang.
- Authentication: AWS_IAM.
- Protocol: HTTPS.

Pemeriksaan identitas AWS:

```bash
aws sts get-caller-identity
```

Contoh script untuk mereplikasi pengujian HTTPS:

```python
import boto3
import urllib.request

from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

region = "us-east-1"

function_url = "https://YOUR_FUNCTION_URL.lambda-url.us-east-1.on.aws/"
url = function_url.rstrip("/") + "/barang"

session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

request = AWSRequest(
    method="GET",
    url=url
)

SigV4Auth(
    credentials,
    "lambda",
    region
).add_auth(request)

http_request = urllib.request.Request(
    url=url,
    headers=dict(request.headers),
    method="GET"
)

with urllib.request.urlopen(http_request) as response:
    print("HTTP Status:", response.status)
    print(response.read().decode("utf-8"))
```

Placeholder YOUR_FUNCTION_URL harus diganti dengan
alamat Function URL yang tersedia pada sandbox.

Script tersebut menggunakan kredensial dari
AWS session dan tidak menanamkan access key,
secret key, maupun session token pada source code.

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

Result: PASSED.

Evidence:

aws_http_connectivity_test.png

Pengujian HTTPS aktual dilakukan pada metode GET.

Operasi POST, PUT, dan DELETE telah diuji melalui
Lambda Test Event, bukan melalui request HTTP langsung.

### Phase 9 — Final Storage Verification

Tahapan:

1. Membuka layanan Amazon S3.
2. Membuka bucket LabInventory.
3. Memilih objek inventory.json.
4. Memeriksa isi akhir objek.
5. Memastikan data sesuai dengan hasil pengujian.

Actual result:

```json
[]
```

Objek inventory.json tetap tersedia dengan ukuran
2 bytes setelah seluruh rangkaian pengujian.

Result: PASSED.

Evidence:

aws_s3_final_inventory.png

## 7. Security and Network Configuration

Konfigurasi keamanan dasar meliputi:

- S3 Block All Public Access aktif.
- Default encryption menggunakan SSE-S3.
- Lambda menggunakan execution role LabRole.
- Function URL menggunakan AWS_IAM.
- Komunikasi client menggunakan HTTPS.
- Kredensial AWS tidak ditanamkan pada source code.
- Screenshot mentah dikecualikan dari Git.
- Informasi autentikasi tidak dipublikasikan.

Arsitektur tidak merancang custom VPC, subnet,
atau EC2 instance.

Komunikasi antar layanan menggunakan fasilitas
layanan AWS terkelola dan izin IAM.

## 8. Cost Management

Implementasi menggunakan pendekatan serverless
untuk menjaga kesederhanaan provisioning dan
menghindari kebutuhan server virtual yang
berjalan secara terus-menerus.

Pengendalian penggunaan resource meliputi:

- Menggunakan Lambda dengan memory 128 MB.
- Menggunakan timeout 15 seconds.
- Menggunakan satu objek JSON pada Amazon S3.
- Menggunakan data contoh berukuran kecil.
- Menjalankan pengujian sesuai kebutuhan.
- Tidak membuat resource tambahan yang tidak diperlukan.
- Memantau penggunaan kredit sandbox.
- Mengakhiri sesi sandbox sesuai ketentuan lab
  setelah kegiatan selesai.

Biaya aktual bergantung pada penggunaan resource
dan ketentuan AWS Academy Sandbox.

Implementasi tidak mengklaim biaya penggunaan nol.

## 9. Troubleshooting

| Issue | Possible Cause | Recommended Action |
|---|---|---|
| AccessDenied | Izin IAM tidak sesuai | Memeriksa execution role |
| NoSuchBucket | Nama bucket tidak sesuai | Memeriksa BUCKET_NAME |
| NoSuchKey | Objek tidak tersedia | Memeriksa OBJECT_KEY |
| ImportModuleError | Struktur ZIP atau handler salah | Memeriksa deployment package |
| Lambda timeout | Eksekusi melebihi batas waktu | Memeriksa timeout dan CloudWatch |
| Invalid JSON | Format request tidak valid | Memeriksa request body |
| HTTP 403 | Autentikasi atau izin IAM tidak sesuai | Memeriksa AWS credentials dan SigV4 |
| HTTP 404 | Barang atau endpoint tidak tersedia | Memeriksa ID dan path |
| HTTP 500 | Internal server atau storage error | Memeriksa CloudWatch Logs |

Tabel tersebut merupakan panduan troubleshooting,
bukan daftar error yang seluruhnya terjadi selama
deployment aktual.

## 10. Rollback and Recovery Plan

Apabila deployment mengalami kegagalan:

1. Memeriksa pesan kesalahan pada CloudWatch.
2. Memeriksa konfigurasi Lambda.
3. Memeriksa environment variables.
4. Memeriksa execution role.
5. Menggunakan source code dari commit yang stabil.
6. Membuat ulang deployment package.
7. Mengunggah package yang telah diperbaiki.
8. Menjalankan pengujian konektivitas.
9. Menjalankan kembali pengujian CRUD.

Apabila data inventaris perlu dipulihkan,
gunakan salinan data yang valid apabila tersedia.

Inisialisasi ulang dengan array kosong hanya
dilakukan pada lingkungan pengujian apabila
penghapusan data memang diizinkan.

Prosedur rollback merupakan rencana pemulihan
dan belum diuji sebagai skenario terpisah.

## 11. Resource Cleanup Plan

Setelah seluruh kegiatan pengujian dan dokumentasi
selesai, resource dapat dievaluasi sesuai ketentuan
AWS Academy Sandbox.

Tahapan cleanup apabila penghapusan diizinkan:

1. Memastikan seluruh bukti telah dikumpulkan.
2. Menyimpan dokumentasi dan source code.
3. Menghapus Function URL apabila tidak diperlukan.
4. Menghapus Lambda function apabila diizinkan.
5. Menghapus objek dan bucket S3 apabila diizinkan.
6. Menghapus CloudWatch log group apabila diperlukan.
7. Mengakhiri sesi sandbox sesuai ketentuan lab.

Resource tidak boleh dihapus apabila masih
diperlukan untuk penilaian atau demonstrasi.

Cleanup merupakan rencana dan tidak dinyatakan
telah dilakukan.

## 12. Deployment Acceptance Criteria

| Acceptance Criteria | Result |
|---|---|
| AWS Sandbox dapat digunakan | PASS |
| Amazon S3 bucket tersedia | PASS |
| Objek inventory.json tersedia | PASS |
| Lambda function tersedia | PASS |
| Source code berhasil di-deploy | PASS |
| Runtime dan handler sesuai | PASS |
| Environment variables sesuai | PASS |
| IAM execution role tersedia | PASS |
| Lambda dapat mengakses Amazon S3 | PASS |
| Operasi CRUD berhasil | PASS |
| Negative testing berhasil | PASS |
| Persistensi data terverifikasi | PASS |
| CloudWatch Logs tersedia | PASS |
| Lambda Function URL tersedia | PASS |
| Konektivitas HTTPS terautentikasi berhasil | PASS |
| Konfigurasi keamanan dasar S3 terverifikasi | PASS |
| Bukti deployment tersedia | PASS |

Seluruh acceptance criteria teknis utama
deployment prototipe telah terpenuhi.

## 13. Deployment Status

| Component | Status |
|---|---|
| Local Implementation | COMPLETED |
| Local Automated Testing | PASSED - 35/35 |
| AWS Environment Preparation | COMPLETED |
| S3 Provisioning | COMPLETED |
| Lambda Provisioning | COMPLETED |
| Source Code Deployment | COMPLETED |
| IAM Configuration | VERIFIED |
| AWS Functional Testing | PASSED - 9/9 |
| HTTP Interface Configuration | COMPLETED |
| HTTP Connectivity | PASSED - HTTP 200 |
| CloudWatch Monitoring | VERIFIED |
| S3 Persistence Verification | PASSED |
| Basic S3 Security | VERIFIED |
| Resource Cleanup | NOT CONFIRMED |

**Overall Deployment Status: COMPLETED**

LabInventory telah berhasil di-deploy pada
AWS Academy Cloud Foundations Sandbox Lingkungan Hidup.

AWS Lambda berhasil menjalankan logika aplikasi
dan terintegrasi dengan Amazon S3 untuk melakukan
operasi CRUD.

Konektivitas HTTPS terautentikasi telah diverifikasi
melalui Lambda Function URL, sedangkan Amazon
CloudWatch berhasil mencatat informasi eksekusi.

Implementasi dan pengujian telah memenuhi target
teknis prototipe akademik dengan batasan yang
didokumentasikan.
