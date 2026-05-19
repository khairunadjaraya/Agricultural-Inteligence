import pandas as pd

def read_data(data):
    """Membaca data"""
    hasil = pd.read_csv(f"data/raw/{data}.csv")
    return hasil

def show_data():
    data_kotor = read_data("produksi_padi")
    tanah_kotor = read_data("sensor_tanah")
    tanah = cleaning_data(tanah_kotor)
    data_padi = cleaning_data(data_kotor)

    data = pd.merge(data_padi, tanah, on="kabupaten", how="left")
    return data
    



