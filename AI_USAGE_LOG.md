# AI Usage Log — [Statprob-Kelompok 11]

## Summary

| Member | Role | Tools | ~% code AI-assisted | Interpretation cells AI-assisted? |
| ------ | ------------- | --------------- | ------------------- | --------------------------------- |
| Natasya Nur Afriyani | Data Engineer | Gemini | ~60% | No                             |
| Elpa Padila | Estimation Analyst | Gemini | ~55% | No                               |
| Riyadh Fadilah | Inference Analyst | Gemini, Notebooklm | ~60% | No                               |
| Daffa Alfaridzi | Hypothesis Analyst | Gemini | ~60% | No                               |
| Adam Raysa Rahman | Computation Analyst | Claude, Copilot | ~60% | No                             |

## Detail Penggunaan Peranggota

### Member A — [Natasya Nur Afriyani]

| #   | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1   | Pengambilan data mentah (Data Acquisition) dari API GitHub Pandas-Dev | Gemini | "Mengambil data pulls... Page 1 sukses... Terjadi kesalahan: HTTPSConnectionPool..." dan "kenapa hasil mergednya hanya 77 saja" | Digunakan untuk menyusun script ⁠fetch_pandas_data.py⁠ yang tangguh dengan mekanisme retry, timeout, dan pengurutan terbaru (desc) guna menembus limit API hingga mendapatkan 1116 Issues dan 1334 Merged PRs |
| 2   | Pemecahan masalah error tipe data (AttributeError) pada Pandas saat pelabelan data | Gemini | (Menyalin log error) “AttributeError: Can only use .str accessor with string values, not floating...” | Digunakan untuk memperbaiki logika feature engineering pada kolom ⁠labels⁠ dengan menambahkan fungsi ⁠.astype(str)⁠ sebelum proses pemindaian kata kunci komparatif |
| 3   | Penanganan kegagalan Git Push akibat pemblokiran keamanan (Push Protection) | Gemini | (Menyalin log error) “remote: error: GH013: Repository rule violations found... Push cannot contain secrets” | Digunakan sebagai panduan langkah demi langkah untuk membersihkan token rahasia dari kode, melakukan ⁠git commit --amend⁠ untuk menghapus riwayat commit lama, mendesain mekanisme pengamanan baru, dan melakukan push ulang dengan sukses ke repositori utama kelompok |

### Member B — [Elpa Padila]

| #   | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1   | Pembuatan struktur dasar fungsi di estimator.py  | Gemini  | Buatkan contoh implementasi fungsi mle_bernoulli, mle_poisson, beta_posterior (return dict α, β, mode, mean), serta log_likelihood Bernoulli & Poisson di Python. Berdasarkan referensi Tsun (2020) | Mengambil logika dasar matematika fungsi MLE dan Log-Likelihood. Struktur fungsi, nama parameter, dan isi docstring dirombak agar sesuai dengan spesifikasi tugas. |
| 2   | Riset format penulisan simbol matematika ($\alpha, \beta, \theta$) di Markdown  | Gemini  | bagaimana membuat simbol alpha, beta, theta, dll di markdown cell | Mengadopsi metode penulisan inline menggunakan satu tanda dolar ($...$) untuk menuliskan simbol $\alpha$, $\beta$, dan $\hat{\theta}$ di dalam docstring kode program. |
| 3   | Pembuatan template alur analisis data (Pipeline) di Notebook  | Gemini  | buatkan template kode Python untuk analisis statistik deskriptif dan estimasi parameter. Saya ingin kodenya dibagi menjadi beberapa langkah (Memuat Data, Data Filtering, Kalkulasi Estimasi MLE & Bayesian, dan Plotting Kurva Log-Likelihood) | Mengikuti struktur logika step-by-step (Load data, Filtering, Deskriptif, dan Plotting). Konsep penanganan nilai kosong (dropna) dan pembuatan matriks grid koordinat untuk grafik tetap digunakan. |

### Member C — [Riyadh Fadilah]

| #   | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1   | Roadmap mengerjakan confidence interval  | Notebooklm  | Berikan saya panduan untuk memulai mengerjakan confidence interval dan berikan juga cara untuk mengenali jenis distribusi | Mengambil hasil logika matematika dengan menggunakan library numpy, dan restruktur hasil fungsi  |
| 2   | Membuat fungsi confidence interval pada inference.py  | Gemini  | Berikan saya contoh implementasi penggunaan confidence interval sesuai dengan aturan formula Tsun (2020) | Menyesuaikan kembali dengan data sumber yang diberikan oleh Data Engineer  |

### Member D - [Daffa Alfaridzi]    

| #   | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1   | Implementasi Z-test di hypothesis.py | Gemini | Buatkan fungsi z_test_one_sample dengan input x_bar, mu0, sigma, n. Berikan output dictionary berisi z_stat, p_value, dan decision | Menggunakan logika fungsi untuk kalkulasi Z-stat dan P-value serta adaptasi return menjadi dictionary sesuai struktur proyek |
| 2   | Debugging ModuleNotFoundError | Gemini | Mengapa muncul ModuleNotFoundError untuk pandas/scipy di VS Code padahal sudah diinstal? Bagaimana cara fix kernel? | Mengikuti langkah instalasi library via terminal proyek dan pemilihan kernel Global Python untuk menstabilkan environment |

### Member E — Adam Raysa Rahman

| # | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1 | Menyusun boilerplate algoritma MCMC Knapsack di `simulation.py` | Claude / Gemini | "Implement MCMC for 0-1 Knapsack problem with accept/reject logic using Python without external optimization libraries" | Mengambil struktur dasar *random walk* dan transisi *stochastic acceptance*. Logika evaluasi (penghitungan *weight* dan *value*) dirombak manual agar sesuai dengan struktur data *dictionary* yang dibuat sebelumnya. |
| 2 | Riset implementasi multi-hashing untuk Bloom Filter | Claude / Gemini | "How to implement multiple independent hash functions for a Bloom Filter using Python hashlib module" | Mengadaptasi penggunaan `hashlib.md5` dengan modifikasi penambahan *salt* iteratif untuk menghasilkan $k$ nilai hash yang unik dalam fungsi `_hashes()`. |
| 3 | Debugging environment Jupyter Notebook di VS Code | Gemini | "NameError: name 'np' is not defined in cell 4 but cell 1 has the import. How to fix execution order in VS Code?" | Mengikuti instruksi untuk membersihkan *output cache* (Clear All Outputs), menyusun ulang urutan fisik sel dari atas ke bawah, dan merestart *kernel* agar eksekusi linier. |

## Group Reflection (150–300 words) // Dummy, not fixed



Selama tiga minggu pengerjaan proyek audit repositori `pandas-dev/pandas`, pendekatan kelompok kami dalam menggunakan AI berevolusi dari sekadar mencari jawaban menjadi alat bantu asistensi yang terkontrol. Pada minggu pertama, kami menggunakan AI (seperti Claude, Copilot, dan Gemini) terutama untuk menyusun *scaffolding* kode, *looping* penarikan data via GitHub API yang memperhitungkan *rate limit*, serta *debugging error* teknis di *environment* lokal (seperti `ModuleNotFoundError` atau penyesuaian posisi sel pada Jupyter Notebook). AI menangani penulisan *boilerplate* ini dengan sangat baik dan efisien.

Namun, kami menemukan bahwa *output* AI memerlukan koreksi signifikan saat menyentuh ranah matematis yang spesifik. AI cenderung memberikan implementasi formula statistik yang terlalu umum (pustaka standar). Kami harus melakukan intervensi manual secara ketat agar kode yang dihasilkan mematuhi formula referensi Tsun (2020), seperti mengoreksi parameter Beta pada estimasi Bayesian (memastikan penggunaan $\alpha = k+1$ dan $\beta = m+1$) serta memperbaiki kalkulasi *Theoretical False Positive Rate* pada Bloom Filter.

Kami secara sadar memilih **tidak menggunakan AI sama sekali** pada seluruh tahap penulisan interpretasi naratif dan kesimpulan analitis. Hal ini kami lakukan demi mematuhi integritas akademik; misalnya, kami memastikan sendiri bahwa redaksi pengujian hipotesis menggunakan istilah *"fail to reject H0"* alih-alih *"accept H0"*, serta memastikan bahwa interpretasi *Confidence Interval* menggunakan tata bahasa *frequentist* yang tepat. Seluruh rekomendasi akhir di dalam *Statistical Health Report* dirumuskan murni dari diskusi internal kelompok berdasarkan hasil komputasi *Monte Carlo* dan *MCMC Knapsack*, guna memastikan kelayakan dan relevansi rekomendasi bagi *maintainer* Pandas.

_(repeat for all five members)_

## Group Reflection (150–300 words)
