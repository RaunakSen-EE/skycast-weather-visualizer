import requests
from config import API_KEY

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        print("Error:", data["message"])
        return None

    return {
        "weather": data["weather"][0]["main"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }