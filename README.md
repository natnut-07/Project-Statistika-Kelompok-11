# Project-Statistika-Kelompok-11

<<<<<<< HEAD
> Audit statistik terhadap repository open-source `pandas` 
> dengan menggunakan Konsep Statistika dan Probabilitas.
=======
> **Audit Statistik Komprehensif Terhadap Stabilitas dan Efisiensi Open-Source Software**
> *Proyek Mata Kuliah Statistika dan Probabilitas (STI 2025)*
>>>>>>> 7002209 (Fixing code)

## 📝 Latar Belakang
Pandas adalah library manipulasi data paling populer di ekosistem Python. Dengan ribuan kontributor, menjaga kualitas kode adalah tantangan besar. Proyek ini bertujuan untuk melakukan audit kesehatan repositori menggunakan pendekatan statistika formal untuk mengukur efisiensi kerja developer dan stabilitas sistem.

## 🎯 Research Questions

| # | Pertanyaan | Tujuan | Teknik | Notebook |
|---|-----------|-------|--------|---------|
| **RQ1** | Berapa estimasi probabilitas sebuah Pull Request (PR) di repositori Pandas berhasil di-merge (diterima), dan seberapa tinggi tingkat ketidakpastian estimasi tersebut? | Menghitung tingkat penerimaan kontribusi di Pandas | MLE Bernoulli & Beta Distribution | `02` + `03` |
| **RQ2** | Apakah laju kemunculan laporan bug (kind/bug) setiap minggunya mengalami perubahan signifikan setelah rilis versi stabil Pandas terbaru dibandingkan periode sebelumnya? | Menguji apakah update software menambah/mengurangi bug | MLE Poisson + Z-test | `02` + `04` |
| **RQ3** | Berapa peluang sebuah issue di Pandas tetap terbuka (tidak terselesaikan) lebih dari 60 hari, dan bagaimana distribusinya jika disimulasikan secara komputasi? | Memprediksi peluang issue "macet" dalam jangka panjang | Monte Carlo Simulation | `05` |

## 👥 Tim (Kelompok 11)

| Peran | Nama | NIM | Jobdesk |
| :--- | :--- | :--- | :--- |
| **Member A** | Natasya Nur Afriyani | 1519625022 | **Data Engineer**: Scraping GitHub API & Data Cleaning |
| **Member B** | Elpa Padila | 1519625020 | **Estimation Analyst**: MLE & Parameter Fitting |
| **Member C** | Riyadh Fadilah | 1519625030 | **Inference Analyst**: Bayesian & Confidence Interval |
| **Member D** | Daffa Alfaridzi | 1519625054 | **Hypothesis Analyst**: Z-Test & Significance Testing |
| **Member E** | Adam Raysa Rahman | 1519625009 | **Computation Analyst**: Monte Carlo Simulation |

## 📁 Struktur Repository

```text
Project-Statistika-Kelompok-11/
├── data/
<<<<<<< HEAD
│   ├── raw/           # Data mentah (.csv) dari GitHub API Pandas
│   └── clean/         # Data siap olah (dataset_final.csv)
├── notebooks/
│   ├── 01_eda.ipynb   # Visualisasi durasi & status issue Pandas
│   ├── 02_estimation.ipynb   # Perhitungan MLE (Lambda & Bernoulli)
│   ├── 03_bayes.ipynb # Update Bayesian (Beta Distribution)
│   ├── 04_test.ipynb  # Uji Hipotesis laju Bug (Z-Test)
│   └── 05_sim.ipynb   # Simulasi Monte Carlo durasi > 60 hari
├── src/               # Script modular (.py)
├── README.md          # Dokumentasi Proyek
└── requirements.txt   # Library: pandas, scipy, matplotlib, seaborn
=======
│   ├── raw/           # Data mentah hasil scraping (Issues & PRs)
│   └── clean/         # Dataset final setelah cleaning & feature engineering
├── notebooks/
│   ├── 01_eda.ipynb   # Preprocessing & Visualisasi Dasar (Member A)
│   ├── 02_est.ipynb   # Estimasi Parameter MLE (Member B)
│   ├── 03_bayes.ipynb # Analisis Bayesian & CI (Member C)
│   ├── 04_test.ipynb  # Uji Hipotesis (Member D)
│   └── 05_sim.ipynb   # Simulasi Monte Carlo (Member E)
├── src/
│   └── fetch_pandas.py # Script automation penarik data
└── README.md
>>>>>>> 7002209 (Fixing code)
```
## 🚀 Cara Menjalankan

```bash
# 1. Clone repositori ini.

# 2. Install library
<<<<<<< HEAD
pip install -r requirements.txt.
=======
pip install pandas numpy scipy matplotlib seaborn requests
>>>>>>> 7002209 (Fixing code)

# 3. Jalankan notebook secara berurutan dari 01 sampai 05.
```
## 📊 Temuan Utama (Statistical Insights)

Masih dalam pengerjaan

## 🔗 Sumber Data & Metodologi

* **Repositori Target:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas)
* **Endpoint API:** GitHub REST API v3 (`/repos/{owner}/{repo}/issues`)
* **Periode Data:** Data diambil hingga tanggal **28 Mei 2026**.
<<<<<<< HEAD
* **Volume Data:** ~1.000 record (terdiri dari Issues dan Pull Requests).
* **Kriteria Pembersihan (Cleaning):** * Hanya menyertakan data dengan status `closed` untuk perhitungan durasi yang akurat.
    * Penghapusan pencilan (outliers) menggunakan metode **Interquartile Range (IQR)** pada kolom `duration_days`.
    * Konversi zona waktu ke UTC untuk standarisasi pengerjaan global.
=======

Data ditarik secara *real-time* melalui **GitHub REST API v3** dengan spesifikasi sebagai berikut:

* **Closed Issues (n = 1.000):** Data murni kategori *issue* (non-PR) untuk analisis durasi pengerjaan.
* **Merged Pull Requests (n = 500):** Data kontribusi kode yang sukses terintegrasi untuk analisis probabilitas merge.
* **Metode Penarikan:** Menggunakan sistem *Time-based Cursor Pagination* (parameter `until`) untuk menghindari limitasi API pada dataset besar (Error 422).
* **Lokasi Data:**
    * Mentah: `data/raw/pandas_issues_raw.csv` & `data/raw/pandas_prs_raw.csv`
    * Siap Olah: `data/clean/dataset_final.csv`
>>>>>>> 7002209 (Fixing code)

---

## 📜 Lisensi & Penggunaan AI
* Proyek ini dibuat untuk tujuan edukasi di **Universitas Negeri Jakarta**.
<<<<<<< HEAD
* Penggunaan AI (Gemini/ChatGPT) didokumentasikan secara transparan dalam file `AI_USAGE_LOG.md` sesuai dengan etika akademik STI 2025.
=======
* Penggunaan AI (Gemini/ChatGPT) didokumentasikan secara transparan dalam file `AI_USAGE_LOG.md` sesuai dengan etika akademik STI 2025.
>>>>>>> 7002209 (Fixing code)
