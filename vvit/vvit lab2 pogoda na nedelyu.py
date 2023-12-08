import requests
s_city = 'Moscow, RU'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+s_city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': s_city, 'units': 'metric', 'lang': 'ru'})
data = requests.get(url).json()
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])