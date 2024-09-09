import os
import requests
from django.shortcuts import render
from django.contrib import messages
from .forms import CityForm
from decouple import config

def index(request):
    api_key = config('WEATHERSTACK_API_KEY')# Get your Weatherstack API key from environment variables

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city_name}'
            response = requests.get(url).json()

            # Check for success response and valid data
            if 'current' in response:
                weather_data = {
                    'city': city_name,
                    'temperature': response['current']['temperature'],
                    'description': response['current']['weather_descriptions'][0],
                    'icon': response['current']['weather_icons'][0],
                    'latitude': response['location']['lat'],
                    'longitude': response['location']['lon'],
                }
            else:
                error_message = response.get('error', {}).get('info', 'City not found. Please enter a valid city name.')
                messages.error(request, error_message)
                weather_data = None
        else:
            weather_data = None
    else:
        form = CityForm()
        weather_data = None

    context = {
        'form': form,
        'weather_data': weather_data,
    }
    return render(request, 'weather/index.html', context)
