import requests

API_KEY = '7fa17462b5544420c772c29a0e60e341'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'imperial'
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\nWeather in {city.title()}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temp}°F")
    print(f"Feels Like: {feels_like}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found. Please check the spelling.")
