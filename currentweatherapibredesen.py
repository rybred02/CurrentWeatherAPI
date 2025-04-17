import requests

API_KEY = '7fa17462b5544420c772c29a0e60e341' # This is where I entered my API code from OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # This pulls data from the live weather service

city = input("Enter city name: ") # Input area

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'imperial' # Imperial temperature format was used here instead of having Celsius as an output
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description'] # Weather description
    temp = data['main']['temp'] # Gets the current temperature
    feels_like = data['main']['feels_like'] # The rest are self exaplanatory
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\nWeather in {city.title()}:") # This and below prints out the weather data for the inputted city
    print(f"Description: {weather}")
    print(f"Temperature: {temp}°F")
    print(f"Feels Like: {feels_like}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found. Please check the spelling.")
