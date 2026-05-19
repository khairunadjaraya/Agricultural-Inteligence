import pandas as pd
import sqlite3

from script.data_loader import read_data
from script.data_analysis import total_produksi, filter_tahun, filter_kg, sort_data
from script.data_exporter import simpan_laporan
from script.data_cleaning import cleaning_data, merge_data
from services.cleaning_service import clean_data

def main():
    print("=====MENU UTAMA=====")
    print("1. Menampilkan keseluruhan data")
    print("2. Mengurutkan data")
    print("3. Memfilter data")    
    print("4. Menampilkan total produksi")

    tujuan = int(input("Mau pilih nomor berapa? "))
    print(tujuan)

    if tujuan == 1:
        data = clean_data()
        print (data)
        simpan_laporan(data, "data_utama")
        print(f"Data telah di simpan di file data_utama.csv")
    elif tujuan == 2:
        data = clean_data()
        kategori = input ("Mengurutkan data berdasarkan apa? (Tahun/Luas Lahan/Jumlah Produksi/Curah Hujan)")
        kategori_input = kategori.strip().lower().replace(" ", "_")
        mapping = {"tahun": "tahun",
                   "luas_lahan": "luas_lahan_ha", 
                   "jumlah_produksi": "produksi_kg",
                   "curah_hujan": "curah_hujan_mm"}
        target = mapping[kategori_input]
        
        print (sort_data(data,f"{target}"))
        simpan_laporan(data, f"data_terurut({target})")
        print(f"Data telah di simpan di file data_utama.csv")
    elif tujuan == 3:
        data = show_data()
        target = input("Ingin memfilter data berdasarkan apa? (Jumlah Produksi/Tahun): ")
        if target.strip().lower() == "jumlah produksi":
            target = int(input("Target: "))
            operator = input("operator: ")
            hasil = filter_kg(data, operator, target)
            print(hasil)
            simpan_laporan(hasil, "data_filter_produksi")
        elif target.strip().lower() == "tahun":
            tahun = int(input("Tahun: "))
            hasil =filter_tahun(data, tahun)
            print(hasil)
            simpan_laporan(hasil, "data_filter_tahun")
    elif tujuan == 4:
        data = show_data()
        kategori = input("Berdasarkan apa? (Provinsi/Kabupaten): ")
        print(total_produksi(data, kategori.strip().lower()))
    
if __name__ == "__main__":
    main()