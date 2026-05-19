import pandas as pd

def simpan_laporan(DataFrame, Nama_File):
    """Menyimpan laporan hasil perhitungan total produksi tiap kabupaten"""
    DataFrame.to_csv(f"data/processed/{Nama_File}.csv", index=False)
    print("\nData telah berhasil disimpan!")
