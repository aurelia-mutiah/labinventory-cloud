
# Deployment Plan — LabInventory

## 1. Deployment Objective

Deployment bertujuan untuk menjalankan prototipe
LabInventory pada lingkungan AWS Academy Cloud
Foundations Sandbox serta memverifikasi konektivitas
antara layanan pemrosesan dan penyimpanan data.

Deployment dilakukan secara bertahap dengan
mempertimbangkan keterbatasan izin akses, waktu,
dan anggaran sandbox.

## 2. Deployment Environment

| Komponen | Rencana Konfigurasi |
|---|---|
| Cloud Provider | Amazon Web Services |
| Environment | AWS Academy Cloud Foundations Sandbox |
| Region | Menyesuaikan region yang diizinkan |
| Runtime | Python 3.11 atau versi kompatibel |
| Compute | AWS Lambda |
| Storage | Amazon S3 |
| Access Control | AWS IAM |
| Monitoring | Amazon CloudWatch |
| Architecture | Serverless |

Seluruh konfigurasi merupakan rancangan awal dan
akan disesuaikan dengan kondisi sandbox.

## 3. Prerequisites

- Repository Git telah tersedia.
- Source code aplikasi telah dikembangkan.
- Python dan virtual environment tersedia.
- Dependensi aplikasi telah terpasang.
- Pengujian lokal telah berhasil.
- Akses AWS Academy Sandbox tersedia.
- Layanan dan izin AWS telah diperiksa sebelum
  provisioning dilakukan.

## 4. Resource Configuration Plan

### 4.1 Amazon S3

| Parameter | Rencana Konfigurasi |
|---|---|
| Bucket Name | labinventory-534903-[unique-suffix] |
| Region | Sama dengan Lambda |
| Public Access | Block All Public Access |
| Encryption | SSE-S3 |
| Versioning | Disabled untuk prototipe |
| Object Key | inventory.json |
| Content Type | application/json |

Bucket digunakan untuk menyimpan data inventaris
dalam format JSON.

Objek inventory.json akan diinisialisasi dengan
array kosong:

```json
[]
```

Inisialisasi dilakukan sebelum pengujian Lambda
untuk memastikan objek penyimpanan tersedia.

### 4.2 AWS Lambda

| Parameter | Rencana Konfigurasi |
|---|---|
| Function Name | labinventory-crud |
| Runtime | Python 3.11 atau versi kompatibel |
| Architecture | x86_64 |
| Memory | 128 MB |
| Timeout | 15 seconds |
| Handler | src.lambda_function.lambda_handler |
| Execution Role | LabRole atau role yang diizinkan |
| VPC | Default, tanpa custom VPC |

Environment variables:

| Key | Value |
|---|---|
| BUCKET_NAME | Nama bucket S3 aktual |
| OBJECT_KEY | inventory.json |

Konfigurasi memory dan timeout dapat disesuaikan
berdasarkan hasil pengujian.

### 4.3 AWS IAM

Lambda menggunakan execution role yang tersedia
dan diizinkan pada lingkungan sandbox.

Izin yang dibutuhkan aplikasi meliputi:

- s3:GetObject
- s3:PutObject
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

Izin s3:ListBucket dapat diperlukan untuk mendukung
pemeriksaan keberadaan objek atau bucket.

Pembuatan maupun perubahan IAM role hanya dilakukan
apabila diizinkan oleh sandbox.

### 4.4 Amazon CloudWatch

CloudWatch digunakan untuk memeriksa log eksekusi
Lambda dan membantu proses troubleshooting.

Log group yang diharapkan:

/aws/lambda/labinventory-crud

Ketersediaan log bergantung pada izin execution role.

## 5. Deployment Package

Deployment package disiapkan dalam format ZIP.

Struktur minimum:

```text
labinventory-deployment.zip
└── src/
    ├── __init__.py
    ├── inventory.py
    ├── storage.py
    ├── s3_storage.py
    └── lambda_function.py
```

Folder src harus berada pada root deployment package
agar sesuai dengan konfigurasi Lambda handler.

AWS Lambda Python runtime menyediakan boto3.
Untuk prototipe ini, SDK bawaan runtime dapat
digunakan setelah kompatibilitasnya diverifikasi.

File berikut tidak dimasukkan ke deployment package:

- Virtual environment
- Folder .git
- Folder tests
- Folder docs
- Folder evidence
- File kredensial AWS
- Data penyimpanan lokal

## 6. Deployment Procedure

### Phase 1 - Sandbox Verification

1. Membuka AWS Academy Cloud Foundations.
2. Membuka lingkungan sandbox.
3. Memulai sesi lab.
4. Membuka AWS Management Console.
5. Memeriksa region yang tersedia.
6. Memeriksa akses terhadap S3, Lambda, IAM,
   dan CloudWatch.
7. Memeriksa execution role yang tersedia.
8. Menentukan kelayakan arsitektur awal.

Apabila layanan utama tidak tersedia, arsitektur
akan disesuaikan sebelum provisioning dilanjutkan.

### Phase 2 - Storage Provisioning

1. Membuka layanan Amazon S3.
2. Membuat bucket dengan nama unik.
3. Memilih region yang sesuai.
4. Memastikan Block Public Access aktif.
5. Memastikan enkripsi penyimpanan aktif.
6. Membuat atau mengunggah inventory.json.
7. Memastikan isi awal objek berupa array kosong.
8. Mendokumentasikan konfigurasi bucket.

### Phase 3 - Compute Provisioning

1. Membuka layanan AWS Lambda.
2. Membuat function labinventory-crud.
3. Memilih runtime Python yang kompatibel.
4. Memilih execution role yang diizinkan.
5. Mengunggah deployment package.
6. Mengatur konfigurasi handler.
7. Mengatur environment variables.
8. Mengatur memory dan timeout.
9. Menyimpan konfigurasi function.

### Phase 4 - Connectivity Verification

1. Membuat Lambda test event untuk GET /barang.
2. Menjalankan function.
3. Memeriksa status code.
4. Memeriksa response JSON.
5. Memastikan Lambda dapat membaca objek S3.
6. Memeriksa CloudWatch Logs jika tersedia.
7. Melakukan troubleshooting apabila terdapat error.

### Phase 5 - CRUD Verification

1. Menambahkan data barang melalui POST /barang.
2. Menampilkan data melalui GET /barang.
3. Memperbarui barang melalui PUT /barang/{id_barang}.
4. Menghapus barang melalui DELETE /barang/{id_barang}.
5. Memeriksa perubahan objek inventory.json.
6. Mendokumentasikan hasil setiap pengujian.

### Phase 6 - HTTP Access (Conditional)

Apabila layanan dan izin sandbox memungkinkan,
antarmuka HTTP dapat dikonfigurasi menggunakan
API Gateway atau Lambda Function URL.

Antarmuka HTTP harus menggunakan mekanisme akses
yang sesuai dan tidak dibuka secara publik tanpa
pengamanan.

Apabila konfigurasi HTTP tidak memungkinkan,
pengujian dilakukan melalui Lambda Console dengan
event yang merepresentasikan request HTTP.

Keterbatasan tersebut akan dicatat dalam laporan.

### Phase 7 - Final Verification

1. Memastikan konfigurasi resource sesuai rancangan.
2. Memastikan operasi CRUD telah diuji.
3. Memeriksa penyimpanan data pada S3.
4. Memeriksa log aplikasi.
5. Mengumpulkan screenshot dan hasil pengujian.
6. Memperbarui diagram arsitektur.
7. Memperbarui dokumentasi repository.

## 7. Cost Management

Penggunaan resource dibatasi pada kebutuhan
provisioning dan pengujian prototipe.

Strategi pengendalian penggunaan:

- Menggunakan Lambda dengan konfigurasi minimal.
- Menyimpan data JSON berukuran kecil.
- Membatasi jumlah invocation pengujian.
- Tidak membuat resource yang tidak diperlukan.
- Menghindari NAT Gateway dan infrastruktur tambahan
  yang tidak dibutuhkan.
- Memantau sisa anggaran sandbox jika tersedia.
- Menghentikan sesi lab sesuai petunjuk AWS Academy.

## 8. Troubleshooting Plan

| Error | Pemeriksaan |
|---|---|
| AccessDenied | Execution role dan izin layanan |
| NoSuchBucket | Nama bucket dan region |
| NoSuchKey | Keberadaan inventory.json |
| ImportModuleError | Struktur ZIP dan handler |
| ModuleNotFoundError | Dependensi dan runtime |
| Timeout | Timeout function dan konektivitas |
| Status 400 | Format request dan validasi data |
| Status 404 | Endpoint atau ID barang |
| Status 500 | Konfigurasi, penyimpanan, dan log |

Setiap kendala akan diperiksa berdasarkan pesan
error aktual sebelum perubahan konfigurasi dilakukan.

## 9. Rollback and Adaptation

Apabila deployment gagal karena keterbatasan
sandbox, langkah berikut dapat dilakukan:

1. Mengidentifikasi penyebab kegagalan.
2. Memeriksa alternatif konfigurasi yang diizinkan.
3. Menyesuaikan arsitektur jika diperlukan.
4. Membuat branch Git terpisah untuk perubahan besar.
5. Mempertahankan versi implementasi lokal sebelumnya.
6. Menjalankan ulang pengujian setelah perubahan.
7. Memperbarui dokumentasi sesuai implementasi aktual.

## 10. Resource Cleanup

Setelah pengujian dan pengumpulan bukti selesai:

1. Memastikan seluruh screenshot telah tersimpan.
2. Memastikan hasil pengujian telah terdokumentasi.
3. Memastikan perubahan kode telah tersimpan di Git.
4. Memeriksa resource yang masih aktif.
5. Menghapus resource yang tidak lagi diperlukan
   apabila diizinkan dan tidak dibutuhkan untuk
   penilaian.
6. Mengakhiri sesi lab sesuai petunjuk AWS Academy.

Mengakhiri sesi lab tidak diasumsikan otomatis
menghapus seluruh resource.

## 11. Deployment Success Criteria

Deployment dinyatakan berhasil apabila:

- Resource utama berhasil dikonfigurasi.
- Lambda dapat menjalankan source code aplikasi.
- Lambda dapat membaca dan menulis data pada S3.
- Empat operasi CRUD berhasil diuji.
- Perubahan data dapat diverifikasi.
- Bukti konfigurasi dan pengujian tersedia.
- Dokumentasi sesuai dengan implementasi aktual.

Ketersediaan endpoint HTTP aktual dicatat secara
terpisah dari keberhasilan pengujian Lambda.

## 12. Deployment Status

Status: Planned - Not Yet Deployed

Implementasi dan pengujian lokal telah selesai.
Provisioning AWS belum dilaksanakan.

Dokumen ini akan diperbarui setelah pelaksanaan
deployment pada AWS Academy Sandbox.
