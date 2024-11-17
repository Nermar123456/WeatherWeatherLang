import requests
from django.shortcuts import render

def weather_view(request):
    API_KEY = "bdcb2704a98076394104a91574a1142e"
    city = request.GET.get('city')  # First city
    city1 = request.GET.get('city1')  # Second city

    data = None
    data1 = None

    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error fetching weather for {city}: {response.status_code}")

    if city1:
        url1 = f"http://api.openweathermap.org/data/2.5/weather?q={city1}&appid={API_KEY}&units=metric"
        response1 = requests.get(url1)
        if response1.status_code == 200:
            data1 = response1.json()
        else:
            print(f"Error fetching weather for {city1}: {response1.status_code}")

    context = {
        'data': data,
        'data1': data1,
        'city': city,
        'city1': city1
    }
    return render(request, 'weather/weather.html', context)


def get_weather_music(data):
    # Example of mapping weather conditions to music genres
    if data['weather'][0]['main'] == 'Clouds':
        return "VIDEO_ID_FOR_RELAXING_MUSIC"  # YouTube video ID for relaxing music on cloudy days
    elif data['weather'][0]['main'] == 'Clear':
        return "VIDEO_ID_FOR_SUNNY_MUSIC"  # YouTube video ID for sunny weather
    elif data['weather'][0]['main'] == 'Rain':
        return "VIDEO_ID_FOR_RAINY_MUSIC"  # YouTube video ID for rainy weather
    else:
        return "VIDEO_ID_FOR_DEFAULT"  # Default video for other conditions
