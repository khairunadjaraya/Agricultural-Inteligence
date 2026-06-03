import pandas as pd

def simpan_laporan(DataFrame, Nama_File):
    """Menyimpan laporan hasil perhitungan total produksi tiap kabupaten"""
    DataFrame.to_csv(f"data/processed/{Nama_File}.csv", index=False)
    print("\nData telah berhasil disimpan!")

def simpan_laporan_excel(data_bersih, summary, anomaly, nama_file):
    """Menyimpan laporan pipeline ke Excel dengan beberapa sheet."""
    output_path = f"data/processed/{nama_file}.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        data_bersih.to_excel(writer, sheet_name="data_bersih", index=False)
        summary.to_excel(writer, sheet_name="summary_produksi", index=False)
        anomaly.to_excel(writer, sheet_name="anomali_produksi", index=False)

    print(f"\nLaporan Excel berhasil disimpan di {output_path}")