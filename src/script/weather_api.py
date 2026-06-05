import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()


def get_current_weather(
    location_name="Bogor",
    latitude=-6.5971,
    longitude=106.8060
):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if api_key is None:
        raise ValueError("OPENWEATHER_API_KEY belum ditemukan di file .env")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric",
        "lang": "id"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(
            f"Gagal mengambil data cuaca: {response.status_code} - {response.text}"
        )

    data = response.json()

    weather_data = {
        "location_name": location_name,
        "latitude": latitude,
        "longitude": longitude,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "rain_1h": data.get("rain", {}).get("1h", 0),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return weather_data


if __name__ == "__main__":
    print(get_current_weather())