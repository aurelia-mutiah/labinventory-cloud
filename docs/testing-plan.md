
# Testing Plan — LabInventory

## 1. Testing Objective

Pengujian dilakukan untuk memastikan bahwa sistem
LabInventory dapat menjalankan operasi CRUD,
memvalidasi data masukan, menangani kesalahan,
dan mengakses layanan penyimpanan cloud.

Pengujian dilakukan pada lingkungan lokal dan
AWS Academy Cloud Foundations Sandbox.

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
- Pencatatan log aplikasi.

Pengujian performa skala besar, concurrent write,
antarmuka pengguna, dan autentikasi pengguna aplikasi
tidak termasuk dalam ruang lingkup prototipe.

## 3. Testing Environment

### 3.1 Local Environment

| Komponen | Konfigurasi |
|---|---|
| Operating System | Windows |
| Development Tool | Visual Studio Code |
| Programming Language | Python 3.11 |
| Testing Framework | unittest |
| AWS SDK | boto3 |
| Local Storage | JSON File |
| AWS Simulation | Mock dan Botocore Stubber |
| Version Control | Git dan GitHub |

### 3.2 Cloud Environment

| Komponen | Rencana Konfigurasi |
|---|---|
| Environment | AWS Academy Cloud Foundations Sandbox |
| Compute | AWS Lambda |
| Storage | Amazon S3 |
| Access Control | AWS IAM |
| Monitoring | Amazon CloudWatch |
| Testing Interface | Lambda Console atau HTTP interface |
| Region | Menyesuaikan sandbox |

Konfigurasi cloud akan diperbarui berdasarkan
lingkungan deployment aktual.

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

Perintah pengujian:

```bash
python -m unittest tests.test_aws_integration -v
```

### 4.3 Combined Testing

Seluruh pengujian dijalankan menggunakan:

```bash
python -m unittest discover -s tests -v
```

### 4.4 Local Testing Results

| Test Suite | Total | Passed | Failed |
|---|---:|---:|---:|
| Inventory Unit Testing | 20 | 20 | 0 |
| AWS Integration Simulation | 15 | 15 | 0 |
| Total | 35 | 35 | 0 |

Status: PASSED

Hasil tersebut merupakan pengujian lokal.
Simulasi integrasi AWS tidak membuktikan bahwa
infrastruktur AWS aktual telah berhasil dikonfigurasi.

## 5. Cloud Testing Prerequisites

Sebelum pengujian cloud dilakukan, pastikan:

- Sesi AWS Sandbox aktif.
- Bucket S3 telah tersedia.
- Bucket tidak dapat diakses secara publik.
- Objek inventory.json telah diinisialisasi.
- Lambda function telah dibuat.
- Deployment package telah diunggah.
- Handler telah dikonfigurasi.
- Environment variables telah dikonfigurasi.
- Execution role memiliki izin yang diperlukan.

Pengujian awal menggunakan inventory.json
dengan isi berupa array kosong.

## 6. Cloud Test Cases

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| CT-01 | Lambda membaca objek S3 | Status 200 | Pending |
| CT-02 | Menambahkan barang | Status 201 | Pending |
| CT-03 | Menampilkan daftar barang | Status 200 | Pending |
| CT-04 | Memperbarui barang | Status 200 | Pending |
| CT-05 | Memeriksa persistensi data pada S3 | Data sesuai | Pending |
| CT-06 | Menghapus barang | Status 200 | Pending |
| CT-07 | Membaca inventaris setelah penghapusan | Barang tidak ditemukan dalam daftar | Pending |
| CT-08 | Menambahkan barang dengan jumlah negatif | Status 400 | Pending |
| CT-09 | Memperbarui ID yang tidak ditemukan | Status 404 | Pending |
| CT-10 | Mengakses endpoint tidak valid | Status 404 | Pending |
| CT-11 | Memeriksa CloudWatch Logs | Log eksekusi tersedia | Pending |
| CT-12 | Mengakses endpoint HTTP aktual | Response sesuai | Conditional |

Status Conditional menunjukkan pengujian yang
bergantung pada ketersediaan antarmuka HTTP.

## 7. Cloud Testing Procedure

Pengujian berikut menggunakan format Lambda
test event yang merepresentasikan HTTP request.

### CT-01 - Initial Connectivity Test

Tujuan:

Memastikan Lambda dapat membaca objek
inventory.json pada Amazon S3.

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
- Total barang bernilai 0 jika inventaris kosong.
- Tidak terdapat kesalahan akses S3.

### CT-02 - Create Barang

Tujuan:

Memastikan sistem dapat menambahkan barang baru
dan menyimpannya pada Amazon S3.

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
- Data barang tersimpan pada S3.

ID aktual dari response dicatat untuk digunakan
pada pengujian update dan delete.

### CT-03 - Read Barang

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
- Jumlah barang sesuai dengan data tersimpan.

### CT-04 - Update Barang

Ganti ID_AKTUAL dengan ID barang yang dihasilkan
pada pengujian CT-02.

Test event:

```json
{
    "httpMethod": "PUT",
    "path": "/barang/ID_AKTUAL",
    "body": "{\"nama_barang\":\"Arduino Uno\",\"kategori\":\"Mikrokontroler\",\"jumlah\":20,\"kondisi\":\"Baik\"}"
}
```

Expected result:

- Status code 200.
- Jumlah barang berubah dari 15 menjadi 20.
- ID barang tetap sama.
- Perubahan tersimpan pada S3.

### CT-05 - Data Persistence Verification

Prosedur:

1. Membuka bucket Amazon S3.
2. Membuka atau mengunduh inventory.json.
3. Memeriksa data barang.
4. Memastikan jumlah barang bernilai 20.
5. Membandingkan isi objek dengan response Lambda.

Expected result:

Data pada Amazon S3 sesuai dengan hasil
operasi create dan update.

### CT-06 - Delete Barang

Ganti ID_AKTUAL dengan ID barang dari CT-02.

Test event:

```json
{
    "httpMethod": "DELETE",
    "path": "/barang/ID_AKTUAL"
}
```

Expected result:

- Status code 200.
- Barang berhasil dihapus dari daftar inventaris.
- Perubahan tersimpan pada S3.

### CT-07 - Read After Delete

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
- Inventaris kosong apabila tidak ada barang lain.

### CT-08 - Invalid Quantity

Test event:

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

### CT-09 - Barang Not Found

Test event:

```json
{
    "httpMethod": "PUT",
    "path": "/barang/BRG-NOT-FOUND",
    "body": "{\"nama_barang\":\"Multimeter\",\"kategori\":\"Alat Ukur\",\"jumlah\":5,\"kondisi\":\"Baik\"}"
}
```

Expected result:

- Status code 404.
- Sistem memberikan informasi bahwa barang
  tidak ditemukan.
- Data inventaris tidak berubah.

### CT-10 - Invalid Endpoint

Test event:

```json
{
    "httpMethod": "GET",
    "path": "/invalid"
}
```

Expected result:

- Status code 404.
- Sistem menolak endpoint yang tidak tersedia.

### CT-11 - CloudWatch Log Verification

Prosedur:

1. Membuka layanan Amazon CloudWatch.
2. Membuka log group Lambda.
3. Memilih log stream dari pengujian terbaru.
4. Memeriksa informasi eksekusi dan error.

Expected result:

Log eksekusi Lambda tersedia apabila execution
role memiliki izin pencatatan log.

### CT-12 - HTTP Interface Verification

Pengujian dilakukan apabila API Gateway atau
Lambda Function URL berhasil dikonfigurasi
dengan mekanisme akses yang sesuai.

Prosedur:

1. Mengirimkan request HTTP yang diizinkan.
2. Memeriksa HTTP status code.
3. Memeriksa response JSON.
4. Memastikan request diproses oleh Lambda.
5. Memastikan perubahan data tersimpan pada S3.

Apabila HTTP interface tidak tersedia,
pengujian ditandai sebagai Not Applicable
dengan alasan yang didokumentasikan.

## 8. Testing Evidence

Bukti pengujian yang direncanakan:

| Evidence | Description |
|---|---|
| Local Unit Testing | Hasil 20 pengujian lokal |
| Combined Testing | Hasil 35 pengujian otomatis |
| Connectivity Test | Lambda berhasil membaca S3 |
| Create Test | Response penambahan barang |
| Read Test | Response daftar barang |
| Update Test | Response pembaruan barang |
| S3 Persistence | Isi objek inventory.json |
| Delete Test | Response penghapusan barang |
| Read After Delete | Verifikasi hasil penghapusan |
| Validation Test | Penolakan data tidak valid |
| CloudWatch Logs | Log eksekusi Lambda |
| HTTP Interface | Bukti akses HTTP jika tersedia |

Screenshot disimpan pada folder evidence/raw
dan tidak diunggah langsung ke repository publik.

## 9. Test Result Classification

| Status | Description |
|---|---|
| Passed | Hasil aktual sesuai expected result |
| Failed | Hasil aktual tidak sesuai expected result |
| Pending | Pengujian belum dilaksanakan |
| Blocked | Pengujian terhambat kendala teknis |
| Conditional | Bergantung pada konfigurasi yang tersedia |
| Not Applicable | Pengujian tidak relevan pada konfigurasi final |

Status pengujian hanya diperbarui setelah
hasil aktual diperoleh.

## 10. Acceptance Criteria

Prototipe dinyatakan memenuhi target fungsional
awal apabila:

- Seluruh pengujian lokal berhasil.
- Lambda dapat menjalankan kode aplikasi.
- Konektivitas Lambda dengan S3 berhasil.
- Empat operasi CRUD berhasil.
- Persistensi data dapat diverifikasi.
- Input tidak valid dapat ditangani.
- Bukti pengujian tersedia.

Ketersediaan endpoint HTTP aktual dilaporkan
secara terpisah dari pengujian Lambda test event.

## 11. Testing Status

Local Testing: PASSED

Total Local Tests: 35

Cloud Testing: PENDING

HTTP Interface Testing: CONDITIONAL

Dokumen ini akan diperbarui berdasarkan hasil
pengujian aktual pada AWS Academy Sandbox.
