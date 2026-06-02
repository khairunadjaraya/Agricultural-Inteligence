import pandas as pd

def read_data(data):
    """Membaca data"""
    hasil = pd.read_csv(f"data/raw/{data}.csv")
    return hasil

    



