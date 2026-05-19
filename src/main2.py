import pandas as pd
import sqlite3

from script.data_loader import read_data
from script.data_analysis import total_produksi, filter_tahun, filter_kg, sort_data
from script.data_exporter import simpan_laporan
from script.data_cleaning import cleaning_data, merge_data
from script.database import save_to_db, read_from_db, show_tables, sum_produksi_by_provinsi, query_by_column
from services.cleaning_service import clean_data


def main():
    print("=====MENU UTAMA=====")
    print("1. Menampilkan dan menyimpan data mentah")
    print("2. Menampilkan tabel pada database saat ini")
    print("3. Menampilkan nama tabel pada database saat ini")
    print("4. Menampilkan tabel hanya pada daerah atau tahun tertentu")
    print("5. Menampilkan total produksi berdasarkan provinsi")

    tujuan = int(input("\nMau pilih nomor berapa? "))
    print(tujuan)

    if tujuan == 1:
        nama_file = input("Nama file: ").lower().replace(" ", "_")
        try:
            data = read_data(f"{nama_file}")
            print(data)
            if input("Simpan data ke database? (y/n): ").lower() == "y":
                nama_tabel = input("Nama tabel: ").lower().replace(" ", "_")
                save_to_db(data, f"{nama_tabel}")
                print(f"Data telah di simpan ke tabel {nama_tabel}.csv")
            else:
                print("Data tidak disimpan ke database.")
        except FileNotFoundError:
            print(f"File {nama_file} tidak ditemukan.")


    elif tujuan == 2:
        nama_tabel = input("Nama tabel: ").lower().replace(" ", "_")
        try:
            data = read_from_db(f"{nama_tabel}")
            print(data)
        except FileNotFoundError:
            print(f"Nama tabel {nama_tabel} tidak ditemukan")

    elif tujuan == 3:
        print(show_tables())

    elif tujuan == 4:
        column = input("Ingin memfilter data berdasarkan apa? (Provinsi/Tahun): ").lower().strip()
        if column.lower().strip() == "provinsi":
            value = input("Masukkan Provinsi: ").title()
            hasil = query_by_column("provinsi", value)
            print(hasil)
        elif column.lower().strip() == "tahun":
            try:
                value = int(input("Masukkan Tahun: "))
                hasil = query_by_column("tahun", value)
                if value < 0:
                    print("Input tahun tidak boleh negatif.")
                    return
                elif hasil.empty:
                    print(f"Tidak ada data pada tahun {value}")
                    return
                else:
                    print(hasil)
            except ValueError:
                print("Input tahun harus berupa angka.")
            
        else:
            print("Tidak bisa filter di luar kategori provinsi dan tahun")
        
    elif tujuan == 5:
        print(sum_produksi_by_provinsi())

if __name__ == "__main__":
    main()