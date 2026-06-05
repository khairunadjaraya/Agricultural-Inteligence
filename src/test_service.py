from services.weather_service import get_weather_dataframe
from script.database import save_to_db, read_from_db


weather_df = get_weather_dataframe()

print("Data cuaca terbaru:")
print(weather_df)

save_to_db(weather_df, "weather_data", mode="append")

print("\nRiwayat data cuaca:")
print(read_from_db("weather_data"))