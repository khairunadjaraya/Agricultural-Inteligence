
def detect_anomaly_zscore(data, column="produksi_kg", threshold=2):
    mean_value = data[column].mean()
    std_value = data[column].std()

    data = data.copy()
    data["z_score"] = (data[column] - mean_value) / std_value
    data["is_anomaly"] = data["z_score"].abs() > threshold

    anomaly_data = data[data["is_anomaly"] == True]

    return anomaly_data

