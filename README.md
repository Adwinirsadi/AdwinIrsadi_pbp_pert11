# Health Risk Prediction Web API

Aplikasi web untuk memprediksi risiko **Diabetes** dan **Stroke** menggunakan model Machine Learning yang terintegrasi dengan REST API dan aplikasi web interaktif.

Project ini dibuat untuk praktikum Mata Kuliah **Pemrograman Berbasis Platform (PBP)** dengan fokus pada integrasi antara Machine Learning, REST API, dan Frontend Web.

## 📋 Deskripsi Project

Aplikasi ini menggunakan **dua model Machine Learning** yang telah dilatih untuk memprediksi:

1. **Risiko Diabetes** - Berdasarkan 8 parameter kesehatan
2. **Risiko Stroke** - Berdasarkan 10 parameter kesehatan

Model dan scaler disimpan dalam format `.pkl`, kemudian digunakan oleh REST API berbasis Flask untuk memproses data input dari pengguna. Pengguna dapat memilih dataset yang ingin diprediksi melalui interface web yang user-friendly.

**Alur Sistem:**

```
User Input (Web Interface)
    ↓
Pilih Dataset (Diabetes / Stroke)
    ↓
Isi Form Sesuai Dataset
    ↓
JavaScript Send JSON to Flask API
    ↓
Flask API Process & Predict
    ↓
Return Prediction Result
    ↓
Display Result on Web
```

## ⭐ Fitur Utama

- ✅ **Dual Model Support** - Diabetes dan Stroke dalam satu aplikasi
- ✅ **Dataset Selector** - Pengguna dapat memilih jenis prediksi
- ✅ **Dynamic Forms** - Form otomatis sesuai dataset yang dipilih
- ✅ **REST API** - Dua endpoint terpisah untuk kedua model
- ✅ **Probabilitas Prediksi** - Menampilkan confidence level
- ✅ **Risk Level Classification** - Tinggi (>70%), Sedang (40-70%), Rendah (<40%)
- ✅ **Responsive Design** - UI yang responsif di berbagai ukuran layar
- ✅ **Real-time Validation** - Validasi input sebelum dikirim ke API

## 📁 Struktur Folder Project

```
health-risk-prediction/
│
├── api/
│   ├── app.py                  # Flask API dengan dual endpoints
│   └── requirements.txt         # Dependencies
│
├── model/
│   ├── diabetes_model.pkl      # Model diabetes terlatih
│   ├── scaler.pkl              # Scaler untuk diabetes
│   ├── stroke_model.pkl        # Model stroke terlatih (NEW)
│   └── stroke_label_encoders.pkl  # Label encoders stroke (NEW)
│
├── web/
│   ├── index.html              # Web interface dengan selector
│   ├── style.css               # Styling responsive
│   └── script.js               # JavaScript handler
│
├── notebook/
│   ├── PrediksiDiabetes.ipynb  # Notebook training diabetes
│   └── PrediksiStroke.ipynb    # Notebook training stroke (NEW)
│
├── dataset_stroke/             # Dataset stroke CSV (NEW)
│   └── healthcare-dataset-stroke-data.csv
│
├── .gitignore
└── README.md
```

## 📊 Model Information

### Model Diabetes
- **Algorithm:** Logistic Regression / StandardScaler
- **Input Features:** 8 parameters
- **Scaler Type:** StandardScaler
- **File:** `diabetes_model.pkl`, `scaler.pkl`

### Model Stroke (NEW)
- **Algorithm:** Random Forest Classifier
- **Input Features:** 10 parameters
- **Training Accuracy:** 100%
- **Testing Accuracy:** 94.81%
- **Files:** `stroke_model.pkl`, `stroke_label_encoders.pkl`

## 📥 Dataset

### Dataset Diabetes
8 fitur untuk prediksi diabetes:
| No | Fitur | Keterangan |
|---|---|---|
| 1 | `Pregnancies` | Jumlah kehamilan |
| 2 | `Glucose` | Kadar glukosa (mg/dL) |
| 3 | `BloodPressure` | Tekanan darah (mmHg) |
| 4 | `SkinThickness` | Ketebalan lipatan kulit (mm) |
| 5 | `Insulin` | Kadar insulin (μU/ml) |
| 6 | `BMI` | Body Mass Index |
| 7 | `DiabetesPedigreeFunction` | Faktor genetik diabetes |
| 8 | `Age` | Usia (tahun) |

### Dataset Stroke (NEW)
10 fitur untuk prediksi stroke:
| No | Fitur | Keterangan |
|---|---|---|
| 1 | `gender` | Jenis kelamin (Male/Female) |
| 2 | `age` | Usia (tahun) |
| 3 | `hypertension` | Tekanan darah tinggi (0/1) |
| 4 | `heart_disease` | Penyakit jantung (0/1) |
| 5 | `ever_married` | Pernah menikah (Yes/No) |
| 6 | `work_type` | Jenis pekerjaan |
| 7 | `Residence_type` | Tipe tempat tinggal (Urban/Rural) |
| 8 | `avg_glucose_level` | Rata-rata kadar glukosa |
| 9 | `bmi` | Body Mass Index |
| 10 | `smoking_status` | Status merokok |

**Dataset Stroke Info:**
- Total Records: 5,110
- Positive Cases (Stroke): 249 (4.87%)
- Negative Cases: 4,861 (95.13%)
- Source: `dataset_stroke/healthcare-dataset-stroke-data.csv`

## 🚀 Cara Menggunakan

### Prerequisite
- Python 3.7+
- Flask & Flask-CORS
- scikit-learn
- NumPy & Pandas

### Instalasi Dependencies

```bash
cd api
pip install -r requirements.txt
```

### Jalankan Flask API

```bash
cd api
python app.py
```

API akan berjalan di: `http://127.0.0.1:5000`

### Buka Web Interface

**Opsi 1 - File langsung di browser:**
```
file:///path/to/web/index.html
```

**Opsi 2 - Live Server (Rekomendasi):**
- Install extension "Live Server" di VS Code
- Klik kanan `index.html` → "Open with Live Server"

## 🔗 API Endpoints

### 1. Home Endpoint
```
GET http://127.0.0.1:5000/
```
**Response:**
```json
{
  "status": "success",
  "message": "API Prediksi Risiko Kesehatan (Diabetes & Stroke)",
  "endpoints": {
    "diabetes": {
      "path": "/predict/diabetes",
      "method": "POST",
      "description": "Prediksi risiko diabetes"
    },
    "stroke": {
      "path": "/predict/stroke",
      "method": "POST",
      "description": "Prediksi risiko stroke"
    }
  }
}
```

### 2. Prediksi Diabetes
```
POST http://127.0.0.1:5000/predict/diabetes
Content-Type: application/json
```

**Request Body:**
```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

**Response:**
```json
{
  "status": "success",
  "dataset": "diabetes",
  "prediction": 1,
  "result": "Berisiko Diabetes",
  "probability": 0.83,
  "risk_level": "Tinggi"
}
```

### 3. Prediksi Stroke
```
POST http://127.0.0.1:5000/predict/stroke
Content-Type: application/json
```

**Request Body:**
```json
{
  "gender": "Male",
  "age": 67,
  "hypertension": 0,
  "heart_disease": 1,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 228.69,
  "bmi": 36.6,
  "smoking_status": "formerly smoked"
}
```

**Response:**
```json
{
  "status": "success",
  "dataset": "stroke",
  "prediction": 1,
  "result": "Berisiko Stroke",
  "probability": 0.85,
  "risk_level": "Tinggi"
}
```

## 💻 Teknologi Stack

| Komponen | Teknologi |
|----------|-----------|
| Backend | Flask, Flask-CORS, Python |
| ML Framework | scikit-learn, NumPy, Pandas |
| Model Serialization | Pickle |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Data Processing | Pandas, NumPy |
| Training Environment | Jupyter Notebook |

## 📝 Catatan Penting

- ⚠️ **Flask harus tetap berjalan** agar web interface dapat terhubung ke API
- ⚠️ Aplikasi ini **hanya untuk pembelajaran**, bukan diagnosis medis profesional
- ℹ️ Stroke model menggunakan Random Forest dengan 94.81% akurasi testing
- ℹ️ Diabetes model sudah tersedia dari praktikum sebelumnya

## 🔍 Troubleshooting

**Error: "API belum berjalan atau tidak dapat diakses"**
- Pastikan Flask sudah berjalan di terminal dengan command: `python api/app.py`
- Cek apakah server berjalan di `http://127.0.0.1:5000`

**Error: "Field wajib diisi"**
- Pastikan semua field form sudah diisi sebelum submit
- Periksa tipe data (number harus angka, select harus dipilih)

**Model version warning saat startup**
- Warning ini normal, terjadi karena versi scikit-learn yang berbeda saat training
- Model tetap berfungsi dengan baik

## 📚 File-file Penting

| File | Deskripsi |
|------|-----------|
| `notebook/PrediksiDiabetes.ipynb` | Training notebook untuk model diabetes |
| `notebook/PrediksiStroke.ipynb` | Training notebook untuk model stroke (NEW) |
| `api/app.py` | Aplikasi Flask dengan dual endpoints |
| `web/index.html` | Halaman web dengan selector dan forms |
| `web/script.js` | Handler untuk form submission |
| `web/style.css` | Styling responsive |

## 🎓 Pembelajaran dari Project

1. **ML Model Integration** - Mengintegrasikan model ML ke dalam API
2. **REST API Development** - Membuat API yang robust dan scalable
3. **Frontend-Backend Communication** - Menghubungkan web dengan backend
4. **Data Preprocessing** - Normalisasi dan encoding data
5. **Error Handling** - Menangani error di berbagai lapisan aplikasi

## ✅ Versi & Update

**Versi 2.0 (Current):**
- ✨ Tambahan Stroke prediction model
- ✨ Dual dataset support dengan selector
- ✨ Update UI/UX untuk multiple forms
- ✨ Improved API endpoints

**Versi 1.0:**
- Diabetes prediction only
- Single model support

## 📧 Informasi Project

- **Mata Kuliah:** Pemrograman Berbasis Platform (PBP)
- **Semester:** 6
- **Tujuan:** Memahami integrasi ML, API, dan Web Development
- **Status:** ✅ Complete & Tested

---

**Catatan:** Untuk dokumentasi lengkap tentang training model, lihat di file notebook masing-masing (`notebook/PrediksiDiabetes.ipynb` dan `notebook/PrediksiStroke.ipynb`).

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
#   A d w i n I r s a d i _ p b p _ p e r t 1 1 
 
 