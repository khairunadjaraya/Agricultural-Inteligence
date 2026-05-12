import pandas as pd

def simpan_laporan(hasil_panen):
    """Menyimpan laporan hasil perhitungan total produksi tiap kabupaten"""
    hasil_panen.to_csv("output/laporan_padi.csv", index=False)
    print("\nData telah berhasil disimpan!")
