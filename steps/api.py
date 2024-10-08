import requests



def get_weather(city: str = "Chicago"):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=NX6j4SODwtlAC3FCOLIXc6kwsDZMZU0R"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = response.json()
    return f"Temperature in {city} is {data["data"]["values"]["temperature"]}°C"


def get_humidity(city: str = "Chicago"):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=NX6j4SODwtlAC3FCOLIXc6kwsDZMZU0R"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = response.json()
    return f"Temperature in {city} is {data["data"]["values"]["humidity"]}°C"


if __name__ == "__main__":
    print(get_weather("San Francisco"))
