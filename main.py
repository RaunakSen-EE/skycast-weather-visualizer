from weather_api import get_weather

from scenes import (
    draw_sunny_scene,
    draw_rainy_scene,
    draw_cloudy_scene,
    draw_thunder_scene
)

from graph_generator import generate_temperature_graph

temperature_history = []

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

    # Storing temperature
    temperature_history.append(data["temp"])

    # Generating graph
    generate_temperature_graph(temperature_history)

    # Scene switching

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