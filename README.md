# 🏙️ Clustering the Countries by using Unsupervised Learning for HELP International
Sebuah mini-proyek berbasis FastAPI yang yang bertujuan untuk mengelompokkan negara-negara ke dalam 3 cluster guna mengidentifikasi negara mana yang paling membutuhkan bantuan HELP Internasional berdasarkan karakteristik fitur-fitur yang tersedia.

## 📁 Struktur File
├── main.py             # Endpoint API utama

├── model.pkl           # File model Machine Learning yang telah dilatih

├── scaler.pkl          # File scaler untuk normalisasi fitur input

├── requirements.txt    # Daftar dependency yang dibutuhkan

## 🚀 Fitur API
- Pengelompokan negara ke 3 bagian berdasarkan fitur yang relevan untuk menerima HELP Internasional
- Menerima input melalui metode POST
- Hasil pengelompokan: Negara maju, Negara berkembang, dan Negara Krisis
- Ringan, cepat, dan siap diintegrasikan ke aplikasi lain

## ⚙️ Cara Menjalankan
### 1. Buat Virtual Environment
python -m venv .env

.env/bin/activate

### 2. Install Dependensi
pip install -r requirements.txt

### 3. Jalankan API
uvicorn main:app --reload

### 4. Akses Swagger UI
Buka browser ke: http://127.0.0.1:8000/docs

## 🧪 Contoh JSON Input
{
  "child_mort": 111,
  "health": 2,
  "income": 1000,
  "life_expec": 33,
  "gdpp_log": 6.907
}

## ✅ Contoh Output
{
  "input": {
    "child_mort": 111,
    "health": 2,
    "income": 1000,
    "life_expec": 33,
    "gdpp_log": 6.907
  },
  "prediksi_cluster": "Cluster 3"
}
