import pandas as pd

from script.data_loader import baca_data

def hitung_total_produksi(data):
    """Menghitung total produksi tiap provinsi"""
    hasil_panen = data.groupby("provinsi")["produksi_kg"].sum().reset_index()
    return hasil_panen

def simpan_laporan(hasil_panen):
    """Menyimpan laporan hasil perhitungan total produksi tiap kabupaten"""
    hasil_panen.to_csv("output/laporan_padi.csv", index=False)
    print("\nData telah berhasil disimpan!")

def filter_tahun(data, tahun):
    filter_data_tahun = data[data["tahun"] == tahun]
    return filter_data_tahun

def main():
    data = baca_data()
    hasil_panen = hitung_total_produksi(data)

    print("Berikut adalah data-data produksi padi beberapa tahun terakhir:")
    print(data)

    print("\nBerikut adalah total produksi panen pada setiap provinsi:")
    print(hasil_panen)

    simpan_laporan(hasil_panen)

    pertanyaan = input("\nApakah tertarik untuk melihat data pada tahun tertentu? ")
    if pertanyaan == "ya":
        tahun = int(input("Tahun berapa? "))
        filter_data_tahun = filter_tahun(data, tahun)
        print(hitung_total_produksi(filter_data_tahun))
    elif pertanyaan == "tidak":
        print("Semoga harimu menyenangkan!")
    else:
        print("Saya tidak paham, coba ulang.")

if __name__ == "__main__":
    main()