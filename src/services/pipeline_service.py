from services.cleaning_service import clean_data
from script.database import save_to_db
from script.data_analysis import total_produksi
from script.data_exporter import simpan_laporan, simpan_laporan_excel
from script.anomaly_detection import detect_anomaly_zscore


def run_pipeline(
    table_name="produksi_padi",
    report_name="laporan_total_produksi",
    anomaly_report_name="laporan_anomali_produksi",
    anomaly_threshold=1
):
    data = clean_data()

    save_to_db(data, table_name)

    summary = total_produksi(data, "provinsi")

    anomaly = detect_anomaly_zscore(
        data,
        column="produksi_kg",
        threshold=anomaly_threshold
    )

    simpan_laporan(summary, report_name)
    simpan_laporan(anomaly, anomaly_report_name)
    simpan_laporan_excel(data, summary, anomaly, f"laporan_pipeline")

    return summary, anomaly