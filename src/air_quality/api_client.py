import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution"


def fetch_current_air_quality(latitude: float, longitude: float, api_key: str) -> dict:
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    return response.json()