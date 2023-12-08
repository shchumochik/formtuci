import requests

city = "Moscow,RU"
appid = "dc4ed5312f3f936f6ba0384c615687b9"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print(city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура", data['main']['temp'])
print("Минимальная температура", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
