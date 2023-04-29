import requests

api_key = "YOUR_API_KEY_HERE"

city_name = "New York" # Replace this with whatever you want.

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(url)

data = response.json()

weather_description = data['weather'][0]['description']
temperature = data['main']['temp']
humidity = data['main']['humidity']

print(f"The weather in {city_name} is currently {weather_description}, with a temperature of {temperature} Kelvin and a humidity of {humidity}%.")
