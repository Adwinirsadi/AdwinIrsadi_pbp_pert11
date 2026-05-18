# Diabetes Risk Prediction Web API

Project ini merupakan aplikasi sederhana untuk memprediksi risiko diabetes menggunakan model Machine Learning yang diintegrasikan dengan REST API dan aplikasi web.

Project ini dibuat untuk praktikum Mata Kuliah **Pemrograman Berbasis Platform**. Fokus utama project ini adalah memahami proses integrasi antara model Machine Learning, REST API, dan aplikasi web.

## Deskripsi Project

Aplikasi ini menggunakan model Machine Learning yang telah dilatih sebelumnya di Google Colab. Model tersebut disimpan dalam format `.pkl`, kemudian digunakan oleh REST API berbasis Flask untuk memproses data input dari pengguna.

Pengguna mengisi data kesehatan melalui halaman web. Data tersebut dikirim ke API dalam format JSON. API melakukan prediksi menggunakan model Machine Learning, kemudian mengembalikan hasil prediksi ke halaman web.

URL Google Colab:

```text
https://colab.research.google.com/drive/1q6wwulYJQHKV3IrnLsC6p6SHagnUGEJj?usp=sharing
```

## Alur Sistem

```text
Google Colab
    ↓
Training Model Machine Learning
    ↓
Export Model dan Scaler
    ↓
REST API Flask
    ↓
Aplikasi Web HTML CSS JavaScript
    ↓
Input Data Pengguna
    ↓
Hasil Prediksi Risiko Diabetes
```

## Fitur Aplikasi

- Membaca model Machine Learning dari file `.pkl`
- Membaca scaler dari file `.pkl`
- Menyediakan endpoint API untuk prediksi diabetes
- Menerima input data dalam format JSON
- Mengembalikan hasil prediksi dalam format JSON
- Menyediakan tampilan web untuk input data pengguna
- Menampilkan hasil prediksi, probabilitas, dan tingkat risiko

## Struktur Folder Project

```text
diabetes-risk-web-api/
│
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── venv/
│
├── model/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

## Keterangan Folder

| Folder/File | Keterangan |
|---|---|
| `api/` | Berisi file backend API Flask |
| `api/app.py` | File utama untuk menjalankan REST API |
| `api/requirements.txt` | Daftar library Python yang digunakan |
| `api/venv/` | Virtual environment Python, tidak perlu diunggah ke GitHub |
| `model/` | Berisi file model dan scaler hasil training dari Google Colab |
| `model/diabetes_model.pkl` | File model Machine Learning |
| `model/scaler.pkl` | File scaler untuk normalisasi input |
| `web/` | Berisi file tampilan aplikasi web |
| `web/index.html` | Struktur halaman web |
| `web/style.css` | Desain tampilan web |
| `web/script.js` | Koneksi antara web dan API |
| `.gitignore` | File untuk mengabaikan folder atau file tertentu dari Git |
| `README.md` | Dokumentasi project |

## Dataset

Dataset yang digunakan adalah dataset diabetes berbasis data tabular. Dataset ini memiliki beberapa atribut kesehatan yang digunakan untuk memprediksi risiko diabetes.

Atribut yang digunakan:

| No | Atribut | Keterangan |
|---|---|---|
| 1 | `Pregnancies` | Jumlah kehamilan |
| 2 | `Glucose` | Kadar glukosa |
| 3 | `BloodPressure` | Tekanan darah |
| 4 | `SkinThickness` | Ketebalan lipatan kulit |
| 5 | `Insulin` | Kadar insulin |
| 6 | `BMI` | Body Mass Index |
| 7 | `DiabetesPedigreeFunction` | Riwayat risiko diabetes keluarga |
| 8 | `Age` | Usia |
| 9 | `Outcome` | Label target, 0 berarti tidak diabetes dan 1 berarti diabetes |

Kolom `Outcome` hanya digunakan pada proses training model. Pada tahap prediksi, pengguna hanya mengisi 8 atribut input.

## Tahap 1: Membuat Model di Google Colab

Tahap pertama dilakukan di Google Colab.

Langkah umum:

1. Mengambil dataset diabetes.
2. Membaca dataset menggunakan Pandas.
3. Memisahkan fitur dan label target.
4. Melakukan pembagian data training dan testing.
5. Melakukan normalisasi data menggunakan scaler.
6. Melatih model Machine Learning.
7. Mengevaluasi model.
8. Menyimpan model dan scaler ke file `.pkl`.

Output dari tahap ini:

```text
diabetes_model.pkl
scaler.pkl
```

Kedua file tersebut kemudian dipindahkan ke folder:

```text
model/
```

## Tahap 2: Menyiapkan Project di VS Code

Buat folder utama project:

```bash
mkdir diabetes-risk-web-api
cd diabetes-risk-web-api
```

Buat struktur folder:

```bash
mkdir api model web
```

Masukkan file model hasil dari Google Colab ke folder `model/`:

```text
model/diabetes_model.pkl
model/scaler.pkl
```

## Tahap 3: Membuat REST API Flask

Masuk ke folder `api`:

```bash
cd api
```

Buat file:

```text
app.py
requirements.txt
```

Isi file `requirements.txt`:

```txt
flask
flask-cors
numpy
scikit-learn
```

Buat virtual environment:

```bash
python3 -m venv venv
```

Aktifkan virtual environment:

```bash
source venv/bin/activate
```

Jika berhasil, terminal akan menampilkan awalan seperti berikut:

```text
(venv) mac@macs-MacBook-Pro api %
```

Install library yang dibutuhkan:

```bash
pip install flask flask-cors numpy scikit-learn
```

Simpan daftar library ke file `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Catatan untuk macOS: gunakan `python3`, bukan `python`.

## Tahap 4: Menjalankan API Flask

API Flask dijalankan dari folder `api`.

Jalankan perintah berikut:

```bash
cd api
source venv/bin/activate
python3 app.py
```

Jika berhasil, API akan berjalan di:

```text
http://127.0.0.1:5000
```

Buka browser dan akses:

```text
http://127.0.0.1:5000/
```

Respons yang benar:

```json
{
  "endpoint": "/predict",
  "message": "API Prediksi Risiko Diabetes berjalan",
  "method": "POST",
  "status": "success"
}
```

Catatan penting: terminal yang menjalankan API Flask tidak boleh ditutup selama aplikasi web digunakan.

## Tahap 5: Menguji Endpoint Prediksi

Endpoint prediksi:

```text
POST http://127.0.0.1:5000/predict
```

Contoh request JSON:

```json
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "SkinThickness": 25,
  "Insulin": 80,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.45,
  "Age": 35
}
```

Contoh response JSON:

```json
{
  "prediction": 1,
  "probability": 0.78,
  "result": "Berisiko Diabetes",
  "risk_level": "Tinggi",
  "status": "success"
}
```

## Tahap 6: Membuat Tampilan Web

Setelah API berhasil berjalan, tahap berikutnya adalah membuat tampilan web.

Buat tiga file di dalam folder `web/`:

```text
web/
├── index.html
├── style.css
└── script.js
```

Keterangan:

| File | Fungsi |
|---|---|
| `index.html` | Membuat form input data kesehatan |
| `style.css` | Mengatur tampilan halaman web |
| `script.js` | Mengirim data dari form ke API Flask |

## Tahap 7: Form Input Web

Form web harus memiliki input berikut:

| Input | ID HTML | Keterangan |
|---|---|---|
| Pregnancies | `Pregnancies` | Jumlah kehamilan |
| Glucose | `Glucose` | Kadar glukosa |
| Blood Pressure | `BloodPressure` | Tekanan darah |
| Skin Thickness | `SkinThickness` | Ketebalan lipatan kulit |
| Insulin | `Insulin` | Kadar insulin |
| BMI | `BMI` | Body Mass Index |
| Diabetes Pedigree Function | `DiabetesPedigreeFunction` | Faktor riwayat diabetes |
| Age | `Age` | Usia |

Nama ID pada HTML harus sama dengan field yang dikirim ke API.

## Tahap 8: Integrasi Web dengan API

File `script.js` bertugas mengambil data dari form, lalu mengirimkannya ke endpoint API:

```text
http://127.0.0.1:5000/predict
```

Data dikirim menggunakan method `POST` dengan format JSON.

Contoh konsep pengiriman data:

```javascript
fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
})
```

Jika API berhasil memberikan respons, hasil prediksi akan ditampilkan pada halaman web.

## Tahap 9: Menjalankan Aplikasi dengan 2 Terminal

Pada project ini, aplikasi dijalankan menggunakan 2 terminal.

Terminal pertama digunakan untuk menjalankan API Flask. Terminal kedua digunakan untuk menjalankan halaman web.

### Terminal 1: Menjalankan API Flask

Buka terminal pertama di VS Code, lalu jalankan:

```bash
cd api
source venv/bin/activate
python3 app.py
```

Pastikan muncul informasi bahwa Flask berjalan di:

```text
http://127.0.0.1:5000
```

Biarkan terminal pertama tetap aktif. Jangan ditutup.

### Terminal 2: Menjalankan Web HTML

Buka terminal kedua di VS Code.

Dari folder utama project, masuk ke folder `web`:

```bash
cd web
```

Jalankan web server sederhana:

```bash
python3 -m http.server 5500
```

Jika berhasil, web akan berjalan di:

```text
http://localhost:5500
```

Buka browser, lalu akses:

```text
http://localhost:5500
```

Setelah halaman web terbuka, isi form prediksi, lalu klik tombol prediksi.

Jika berhasil, halaman web akan menampilkan:

- Hasil prediksi
- Probabilitas risiko
- Tingkat risiko

## Ringkasan Cara Menjalankan Project

Gunakan dua terminal.

### Terminal 1

```bash
cd api
source venv/bin/activate
python3 app.py
```

Akses API:

```text
http://127.0.0.1:5000/
```

### Terminal 2

```bash
cd web
python3 -m http.server 5500
```

Akses web:

```text
http://localhost:5500
```

## Tahap 10: Menyimpan Project ke GitHub

Pastikan berada di folder utama project:

```bash
cd diabetes-risk-web-api
```

Inisialisasi Git:

```bash
git init
```

Tambahkan file ke staging area:

```bash
git add .
```

Commit project:

```bash
git commit -m "Initial commit: diabetes risk prediction web API"
```

Ubah branch ke `main`:

```bash
git branch -M main
```

Hubungkan ke repository GitHub:

```bash
git remote add origin https://github.com/username/diabetes-risk-web-api.git
```

Push ke GitHub:

```bash
git push -u origin main
```

Ganti `username` dengan username GitHub masing-masing.

## Contoh .gitignore

Buat file `.gitignore` di folder utama project:

```gitignore
# Python virtual environment
venv/
api/venv/

# Python cache
__pycache__/
*.pyc
*.pyo

# macOS
.DS_Store

# Jupyter checkpoint
.ipynb_checkpoints/

# Environment file
.env
```

## Troubleshooting

### 1. `zsh: command not found: python`

Gunakan perintah:

```bash
python3 app.py
```

### 2. `ModuleNotFoundError: No module named 'flask'`

Aktifkan `venv`, lalu install Flask:

```bash
source venv/bin/activate
pip install flask flask-cors
```

### 3. Error saat membuat virtual environment karena nama folder mengandung `:`

Hindari penggunaan karakter `:` pada nama folder. Gunakan nama folder seperti:

```text
2025_2026_GENAP
```

bukan:

```text
2025:2026 GENAP
```

### 4. Web tidak bisa mengakses API

Pastikan API sudah berjalan di terminal pertama:

```text
http://127.0.0.1:5000
```

Pastikan juga Flask sudah menggunakan CORS:

```python
from flask_cors import CORS
CORS(app)
```

Pastikan endpoint di `script.js` mengarah ke:

```text
http://127.0.0.1:5000/predict
```

### 5. Halaman HTML terbuka, tetapi hasil prediksi tidak muncul

Periksa tiga hal berikut:

1. API Flask harus aktif di Terminal 1.
2. Web server harus aktif di Terminal 2.
3. Browser harus membuka alamat `http://localhost:5500`, bukan hanya membuka file langsung dari Finder.

### 6. Hasil prediksi error

Pastikan nama field yang dikirim dari web sama dengan nama field yang diminta API:

```text
Pregnancies
Glucose
BloodPressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age
```


## Tampilan Aplikasi Web

Berikut adalah tampilan halaman prediksi risiko diabetes.

![Tampilan Web Prediksi Diabetes](https://github.com/banyustudiodev/diabetes-risk-web-api/blob/main/Screenshot%202026-05-17%20at%2015.49.56.png)


## Catatan Penting

Aplikasi ini dibuat untuk tujuan pembelajaran. Hasil prediksi tidak boleh digunakan sebagai diagnosis medis. Sistem ini hanya merupakan simulasi integrasi Machine Learning, REST API, dan aplikasi web.

Keputusan medis tetap harus dilakukan oleh tenaga kesehatan profesional.

## Status Project

- [x] Model Machine Learning dibuat di Google Colab
- [x] Model dan scaler disimpan dalam format `.pkl`
- [x] REST API Flask dibuat
- [x] Endpoint utama `/` berjalan
- [x] Endpoint prediksi `/predict` berhasil diuji
- [x] Tampilan web dibuat
- [x] Web berhasil terhubung dengan API
- [x] Project selesai dan didokumentasikan di GitHub

## Lisensi

Project ini dibuat untuk kebutuhan pembelajaran dan praktikum.
#   A d w i n I r s a d i _ p b p _ p e r t 1 1  
 