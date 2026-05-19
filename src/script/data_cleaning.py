import pandas as pd

def cleaning_data (data):

    for kolom in data.columns:
        total_null = data[kolom].isnull().sum()
        if total_null > 0:
            if pd.api.types.is_numeric_dtype(data[kolom]):
                data[kolom] = data[kolom].fillna(data[kolom].mean())
    return data

def merge_data (data1, data2):
    hasil = pd.merge(data1, data2, on="kabupaten", how="left")
    return hasil