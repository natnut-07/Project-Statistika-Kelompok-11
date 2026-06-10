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

| #   | Task | AI yang Digunakan | Prompt | Bagaimana Output AI Digunakan |
| --- | ---- | ---- | ------ | ----------------------- | 
| 1   | Membuat algoritma MCMC Knapsack pada simulation.py | Gemini | Berikan saya panduan dan contoh kode untuk membuat algoritma MCMC Knapsack 0-1 menggunakan Python | Mengambil logika dasar *random walk* dan menyesuaikannya dengan struktur *dictionary* dari data project |
| 2   | Membuat fungsi multi-hashing untuk Bloom Filter | Gemini | Berikan saya cara menggunakan library hashlib md5 untuk membuat 3 nilai hash yang berbeda dari satu input | Mengambil hasil manipulasi *string* (*salt*) dan menerapkan operasi modulo agar sesuai dengan ukuran array |
| 3   | Mengatasi error import folder src pada notebook | Gemini | Berikan saya solusi untuk mengatasi ImportError saat memanggil file python dari folder yang berbeda di Jupyter Notebook | Mengambil fungsi library sys dan os untuk mendaftarkan *path* folder secara otomatis |
| 4   | Optimasi memori pada simulasi Monte Carlo | Gemini | Berikan saya cara mengoptimalkan perulangan data yang besar di Python agar tidak memakan banyak memori | Mengubah penggunaan *list* standar menjadi *generator expression* untuk efisiensi eksekusi |


## Group Reflection

Sebagai tim audit statistik terhadap repository open-source pandas, kami menggunakan dan mengintegrasikan AI dalam alur perencanaan dan pengerjaan kami selama tiga minggu terakhir. 

Data Engineer kami sangat terbantu dengan adanya AI dalam melakukan perbaikan logika, menyusun script, dan panduan langkah demi langkah, sehingga AI menangani hal tersebut dengan baik. Selain itu pada Estimaton Analyst kami mengandalkan AI untuk mengambil logika dasar matematika fungsi MLE dan likelihood sebagai struktur dasar. 

Inference dan Hypothesis Analyst kami mengandalkan AI untuk debugging dan contoh implementasi yang baik dalam projek statistik ini. Sementara itu, Computation Analyst kami membuat algoritma MCMC Knapsack pada simulation.py, dan juga membuat fungsi multi-hashing untuk Bloom Filter.

Keputusan kami adalah menggunakan AI sebagai optimasi pekerjaan, namun tetap divalidasi manual agar hasil generate AI tersebut tidak bias dari RQ yang telah disediakan. Kami merasa jika kami mengandalkan AI sepenuhnya dalam pengambilan keputusan strategis, rasanya tidak etis dalam kelompok kami. Oleh karena itu, kami menempatkan AI sebagai alat bantu teknis, bukan pengambil keputusan utama dalam proses pengerjaan projek ini.



