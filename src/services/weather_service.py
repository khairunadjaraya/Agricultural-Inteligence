from script.weather_api import get_current_weather
from script.database import save_to_db, read_from_db
import pandas as pd


def get_weather_dataframe(
    location_name="Bogor",
    latitude=-6.5971,
    longitude=106.8060
):
    weather_data = get_current_weather(
        location_name=location_name,
        latitude=latitude,
        longitude=longitude
    )

    df = pd.DataFrame([weather_data])

    return df


def save_current_weather(
    location_name="Bogor",
    latitude=-6.5971,
    longitude=106.8060,
    table_name="weather_readings"
):
    weather_df = get_weather_dataframe(
        location_name=location_name,
        latitude=latitude,
        longitude=longitude
    )

    save_to_db(weather_df, table_name, mode="append")

    return weather_df


def get_weather_history(table_name="weather_readings"):
    return read_from_db(table_name)


if __name__ == "__main__":
    latest_weather = save_current_weather()

    print("Data cuaca terbaru:")
    print(latest_weather)

    print("\nRiwayat data cuaca:")
    print(get_weather_history())