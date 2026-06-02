from services.cleaning_service import clean_data
from script.database import save_to_db
from script.data_analysis import total_produksi
from script.data_exporter import simpan_laporan

def run_pipeline(table_name="produksi_padi", report_name="laporan_total_produksi"):
    data = clean_data()

    save_to_db(data, table_name)

    summary = total_produksi(data, "provinsi")

    simpan_laporan(summary, report_name)

    return summary