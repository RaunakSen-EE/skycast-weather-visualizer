from weather_api import get_weather
from scenes import draw_sunny_scene, draw_rainy_scene

city = input("Enter city name: ")

data = get_weather(city)

if data:

    # weather = data["weather"]
    weather = "Rain"

    print("\n Weather Report")
    print("----------------------")
    print("Weather:", weather)
    print("Temperature:", data["temp"], "°C")
    print("Humidity:", data["humidity"], "%")

    if weather == "Clear":
        draw_sunny_scene()

    elif weather == "Rain":
        draw_rainy_scene()

    else:
        print("No scene available for this weather yet.")