import pandas as pd

def hitung_total_produksi(data):
    """Menghitung total produksi tiap provinsi"""
    hasil_panen = data.groupby("provinsi")["produksi_kg"].sum().reset_index()
    return hasil_panen

def filter_tahun(data, tahun):
    filter_data_tahun = data[data["tahun"] == tahun]
    return filter_data_tahun