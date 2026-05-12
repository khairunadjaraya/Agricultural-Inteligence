import pandas as pd

def baca_data():
    """Membaca data"""
    data = pd.read_csv("data/produksi_padi_fiktif.csv")
    return data