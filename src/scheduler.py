from apscheduler.schedulers.blocking import BlockingScheduler
from services.pipeline_service import run_pipeline


def scheduled_pipeline():
    print("Menjalankan pipeline terjadwal...")

    summary, anomaly = run_pipeline(
        table_name="produksi_padi_scheduled",
        report_name="laporan_total_produksi_scheduled",
        anomaly_report_name="laporan_anomali_produksi_scheduled",
        anomaly_threshold=1
    )

    print("Pipeline terjadwal selesai.")


def main():
    scheduler = BlockingScheduler()

    scheduler.add_job(
        scheduled_pipeline,
        trigger="interval",
        minutes=1
    )

    print("Scheduler aktif. Pipeline akan berjalan setiap 1 menit.")
    print("Tekan CTRL + C untuk menghentikan.")
    scheduler.start()


if __name__ == "__main__":
    main()