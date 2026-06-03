# Agricultural Intelligence - Pipeline Data Pertanian

Project ini adalah pipeline analisis data pertanian menggunakan Python.  
Fokus awal project adalah mengolah data produksi padi dan sensor tanah, lalu menghasilkan laporan otomatis.

Project ini merupakan bagian dari roadmap pembangunan sistem AI pertanian terintegrasi.

## Fitur

- Membaca data CSV dari folder `data/raw`
- Membersihkan missing value pada data numerik
- Menggabungkan data produksi padi dengan data sensor tanah
- Menyimpan data bersih ke SQLite
- Menghitung total produksi berdasarkan provinsi
- Mendeteksi anomali produksi menggunakan z-score
- Menyimpan laporan dalam format CSV
- Menyimpan laporan Excel multi-sheet
- Menjalankan pipeline melalui command line menggunakan `argparse`
- Menjalankan pipeline otomatis menggunakan APScheduler

## Struktur Folder

```text
AI-PERTANIAN-PANDAS/
│
├── data/
│   ├── raw/                 # Dataset mentah
│   └── processed/           # Hasil laporan CSV dan Excel
│
├── output/                  # Folder output tambahan
│
├── src/
│   ├── script/
│   │   ├── data_loader.py          # Membaca data CSV
│   │   ├── data_cleaning.py        # Membersihkan dan merge data
│   │   ├── data_analysis.py        # Analisis produksi
│   │   ├── data_exporter.py        # Export laporan CSV dan Excel
│   │   ├── database.py             # Fungsi SQLite
│   │   └── anomaly_detection.py    # Deteksi anomali
│   │
│   ├── services/
│   │   ├── cleaning_service.py     # Alur cleaning dan merge
│   │   └── pipeline_service.py     # Pipeline utama
│   │
│   ├── main.py
│   ├── main2.py
│   ├── main3.py                   # Entry point pipeline terbaru
│   └── scheduler.py               # Scheduler otomatis
│
├── pertanian.db
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalasi

Clone repository:

```bash
git clone https://github.com/khairunadjaraya/Agricultural-Inteligence.git
cd Agricultural-Inteligence
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Cara Menjalankan Pipeline Manual

Jalankan pipeline dengan konfigurasi default:

```bash
python src/main3.py
```

Atau jalankan dengan nama tabel, laporan, dan threshold custom:

```bash
python src/main3.py --table produksi_padi_test --report laporan_test --anomaly-report laporan_anomali_test --threshold 1
```

Argumen yang tersedia:

```text
--table             Nama tabel tujuan di SQLite
--report            Nama file laporan summary produksi
--anomaly-report    Nama file laporan anomali produksi
--threshold         Batas z-score untuk mendeteksi anomali
```

## Cara Menjalankan Scheduler

Untuk menjalankan pipeline otomatis setiap 1 menit:

```bash
python src/scheduler.py
```

Hentikan scheduler dengan:

```text
CTRL + C
```

Catatan: scheduler ini berjalan secara lokal. Jika laptop mati, sleep, atau terminal ditutup, scheduler akan berhenti.

## Output

Pipeline menghasilkan beberapa output di folder `data/processed`:

```text
laporan_total_produksi.csv
laporan_anomali_produksi.csv
laporan_pipeline.xlsx
```

File Excel `laporan_pipeline.xlsx` berisi beberapa sheet:

```text
data_bersih
summary_produksi
anomali_produksi
```

## Teknologi

- Python
- Pandas
- SQLite
- OpenPyXL
- APScheduler
- Git & GitHub

## Roadmap Project

Project ini adalah bagian dari roadmap sistem AI pertanian:

```text
Fase 1: Fondasi Python & Data
Fase 2: Data & Sensor Pertanian
Fase 3: Machine Learning Terapan
Fase 4: Integrasi LLM & AI Insight
Fase 5: Deployment & Produksi
```

Status saat ini:

```text
Fase 1 Modul 4 - Integrasi Pipeline
```