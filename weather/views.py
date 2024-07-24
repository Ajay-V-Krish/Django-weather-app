from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'].capitalize()
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+ '&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(res)
        data = {
            'city' : city,
            'country' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp' : str((json_data['main']['temp']) - 273.15) + ' C',
            'pressure' :  str(json_data['main']['pressure']),
            'humidity' : str(json_data['main']['humidity'])
        }
    else:
        data = {}
    return render(request, 'index.html',{'data': data})