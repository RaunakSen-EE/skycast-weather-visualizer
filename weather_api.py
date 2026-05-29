import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    if data.get("cod") != 200:
        return None

    return {
        "city": data["name"],
        "weather": data["weather"][0]["main"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }