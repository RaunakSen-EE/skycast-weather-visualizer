from weather_api import get_weather

from scenes import (
    draw_sunny_scene,
    draw_rainy_scene,
    draw_cloudy_scene,
    draw_thunder_scene
)

print(" Welcome to SkyCast")
print("--------------------------")

city = input("Enter city name: ")

data = get_weather(city)

if data:

    weather = data["weather"]

    print("\n Weather Report")
    print("--------------------------")
    print("City:", data["city"])
    print("Weather:", weather)
    print("Temperature:", data["temp"], "°C")
    print("Humidity:", data["humidity"], "%")

    
    if weather == "Clear":
        draw_sunny_scene()

    elif weather in ["Rain", "Drizzle"]:
        draw_rainy_scene()

    elif weather in ["Clouds", "Mist", "Fog", "Haze", "Smoke"]:
        draw_cloudy_scene()

    elif weather == "Thunderstorm":
        draw_thunder_scene()

    else:
        print("\n No visual scene available for:", weather)

else:
    print("\n Failed to fetch weather data.")