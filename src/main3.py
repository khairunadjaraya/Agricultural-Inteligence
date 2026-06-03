import argparse
from services.pipeline_service import run_pipeline


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
        help="Nama file laporan ringkasan produksi"
    )

    parser.add_argument(
        "--anomaly-report",
        default="laporan_anomali_produksi",
        help="Nama file laporan anomali produksi"
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=1,
        help="Batas z-score untuk mendeteksi anomali"
    )

    args = parser.parse_args()

    print("Menjalankan pipeline data pertanian...")
    print(f"Tabel database: {args.table}")
    print(f"Laporan summary: {args.report}")
    print(f"Laporan anomali: {args.anomaly_report}")
    print(f"Threshold anomali: {args.threshold}")

    summary, anomaly = run_pipeline(
        table_name=args.table,
        report_name=args.report,
        anomaly_report_name=args.anomaly_report,
        anomaly_threshold=args.threshold
    )

    print("Pipeline selesai.")

    print("\nRingkasan produksi:")
    print(summary)

    print("\nData anomali:")
    print(anomaly)


if __name__ == "__main__":
    main()