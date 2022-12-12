import datetime as dt 
import requests

url = "http://api.openweathermap.org/data/2.5/weather?"
api_Key = open('api_key.txt', 'r').read()
city = "Birmingham"

def temp_conversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

finalUrl = url + "appid=" + api_Key + "&q=" + city
response = requests.get(finalUrl).json()

tempkelvin = response['main']['temp']
tempFahrenheit, tempCelsius = temp_conversion(tempkelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = temp_conversion(feels_like_kelvin)

humidity = response['main']['humidity']

weather_description = response['weather'][0]['description']

sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {city}: {tempCelsius:.2f}C or {tempFahrenheit}F")
print(f"Temperature in {city} feels like : {feels_like_celsius:.2f}C or {feels_like_fahrenheit}F")

print(f"Humidity in {city}: is {humidity}%")
print(f"Weather in {city} {weather_description}")

print(f"Sun rises in {city} at {sunrise_time} local time")
print(f"Sun sets in {city} at {sunset_time} local time")