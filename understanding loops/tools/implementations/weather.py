from tools.registry import tool

import requests

from config import OPENWEATHER_API_KEY


@tool(
    name="get_weather",
    description="Get the current weather for a location.",
    input_schema={
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country"
            }
        },
        "required": ["location"]
    }
)
def get_weather(location: str):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    weather = response.json()

    return {
        "temperature": weather["main"]["temp"],
        "conditions": weather["weather"][0]["description"]
    }