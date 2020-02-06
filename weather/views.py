import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=YOUR_API_KEY'
  city = 'Montreal'

  if request.method == 'POST':
    form = CityForm(request.POST)
    form.save()

  form = CityForm()

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

  context = {'weather_data': weather_data, 'form': form}
  return render(request, 'weather/weather.html', context)
