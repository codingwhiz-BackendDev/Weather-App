from django.shortcuts import render

import urllib.request
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9f86fc6e4b78c46fde16292440ff18a8').read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coord": str(json_data['coord']['lon']) + ' longitude '+' ' + str(json_data['coord']['lat'])+' latitude',
            "temp": str(json_data['main']['temp'])+ 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }          
    else:
        data = {}
        city = ''
    return render(request, 'index.html', {'city': city, 'data': data}, )
 