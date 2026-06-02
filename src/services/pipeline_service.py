from services.cleaning_service import clean_data
from script.database import save_to_db
from script.data_analysis import total_produksi
from script.data_exporter import simpan_laporan

def run_pipeline():
    data = clean_data()

    save_to_db(data, "produksi_padi")

    summary = total_produksi(data, "provinsi")

    simpan_laporan(summary, "laporan_total_produksi")

    return summary