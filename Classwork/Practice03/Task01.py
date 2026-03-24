import requests
import json

city = 'Иркутск'
url= 'https://api.openweathermap.org/data/2.5/weather'
params= {
"q": city,
"units": "metric",
"lang": "ru",
"appid":"79d1ca96933b0328e1c7e3e7a26cb347"
}

weather_data= requests.get(url, params=params).json()
weather_data_structure = json.dumps(weather_data, indent=2)
print(weather_data_structure)
temperature = round(weather_data['main']['temp'])
temperature_feels= round(weather_data['main']['feels_like'])
pressure = int(weather_data['main']['pressure'])*0.75
humidity = int(weather_data['main']['humidity'])
wind_speed= int(weather_data['wind']['speed'])

clouds_percent = weather_data['clouds']['all']
if clouds_percent == 0:
    cloudiness = "Ясно"
elif 0 < clouds_percent <= 50:
    cloudiness = "Переменная облачность"
else:
    cloudiness = "Пасмурно"

precipitations = ""
if 'rain' in weather_data:
    precipitations = "Идет дождь"
if 'snow' in weather_data:
    precipitations = "Идет снег"


print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')
print('Давление ', str(pressure), 'Мм.рт.ст.')
print('Влажность ', str(humidity), '%')
print('Скорость ветра ', str(wind_speed), 'м/с')
print(f"Облачность и осадки : {cloudiness}{precipitations}")
