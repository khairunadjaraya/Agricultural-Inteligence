import argparse
from services.pipeline_service import run_pipeline
from script.anomaly_detection import detect_anomaly_zscore
from services.cleaning_service import clean_data


def main():

    parser = argparse.ArgumentParser(
        description="Pipeline analisis data pertanian"
    )

    parser.add_argument(
        "--table",
        default="produksi_padi",
        help="Nama tabel tujuan di database SQLite"
    )

    parser.add_argument(
        "--report",
        default="laporan_total_produksi",
        help="Nama file laporan yang akan disimpan"
    )

    args = parser.parse_args()

    print("Menjalankan pipeline data pertanian...")
    print(f"Tabel database: {args.table}")
    print(f"Nama laporan: {args.report}")

    summary, anomaly = run_pipeline(
        table_name=args.table,
        report_name=args.report
    )

    print("Pipeline selesai.")
    print("Ringkasan produksi:")
    print(summary)

    print("Data anomali:")
    print(anomaly)

if __name__ == "__main__":
    main()

