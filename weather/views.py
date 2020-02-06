import requests
from django.shortcuts import render
from .models import City

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=253682c0bd759acfb4255d4aa08c3dd7'
  city = 'Montreal'

  cities = City.objects.all()

  weather_data = []

  for city in cities:
    api = requests.get(url.format(city)).json()
    city_weather = {
      'city': city.name,
      'temperature': api['main']['temp'],
      'description': api['weather'][0]['description'],
      'icon': api['weather'][0]['icon'],
    }
    weather_data.append(city_weather)

  context = {'weather_data': weather_data}
  return render(request, 'weather/weather.html', context)
