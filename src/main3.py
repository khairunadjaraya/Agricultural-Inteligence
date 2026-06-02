from services.pipeline_service import run_pipeline

def main():
    print("Menjalankan pipeline data pertanian...")

    summary = run_pipeline()

    print("Pipeline selesai.")
    print(summary)

if __name__ == "__main__":
    main()