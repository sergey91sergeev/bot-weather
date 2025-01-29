import requests
from config import API_KEY

weather_api_key = API_KEY


def get_weather(city: str) -> str:
    """Функция принимает название города и возвращает сводку по погоде"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return "Город не найден."

    weather_description = response["weather"][0]["description"].capitalize()
    temperature = response["main"]["temp"]
    speed = response["wind"]["speed"]
    clouds = response["clouds"]["all"]
    humidity = response["main"]["humidity"]
    feels_like = response["main"]["feels_like"]
    weather_condition = response["weather"][0]["main"].lower()
    icon = get_weather_icon(weather_condition)

    return (f"{weather_description} {icon}\n"
            f"Температура {round(temperature, 1)} °C\n"
            f"Ощущается как {round(feels_like, 1)} °C\n"
            f"Ветер {round(speed, 1)} м/с\n"
            f"Облачность {clouds} %\n"
            f"Влажность {humidity} %\n")


def get_weather_icon(weather_condition: str) -> str:
    """Функция принимает параметр weather_condition (погодные условия)
    и возвращает эмодзи, соответствующий условиям"""
    weather_icons = {
        "clear": "\U00002600",  # ☀️
        "clouds": "\U00002601",  # ☁️
        "rain": "\U0001F327",  # 🌧
        "thunderstorm": "\U0001F329",  # 🌩
        "snow": "\U0001F328",  # 🌨
        "fog": "\U0001F32B",  # 🌫
        "partly cloudy": "\U000026C5",  # ⛅
        "windy": "\U0001F32C"  # 🌬
    }
    return weather_icons.get(weather_condition)
