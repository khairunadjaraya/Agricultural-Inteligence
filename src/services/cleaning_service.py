import pandas as pd
from script.data_loader import read_data
from script.data_cleaning import cleaning_data, merge_data

def clean_data():
    data_kotor = read_data("produksi_padi")
    tanah_kotor = read_data("sensor_tanah")
    tanah = cleaning_data(tanah_kotor)
    data_padi = cleaning_data(data_kotor)

    data = merge_data(data_padi, tanah)
    return data