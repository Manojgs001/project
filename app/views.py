from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    
    city= request.GET.get('city')
    
    api_key = "1fa8f1415423bb651b944996eeb88971"
    
    api_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    print(api_url)
    
    api = requests.get(api_url).json()
    
    
    temperature= api["main"]["temp"]
    city=api["name"]
    country = api['sys']['country']
    wind_speed = api['wind']['speed']
    humidity = api['main']['humidity']
    name = api['name']
    icon = api['weather'][0]['icon']
    weather = api["weather"][0]['main']
    description = api['weather'][0]['description']
    
    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    
    # https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=b87770e0c526050cc7426cd23fa9cf28&units=metric

    
    
    
    
    return render(request,'index.html',{'temperature':temperature, 'wind_speed':wind_speed, 'humidity':humidity, 'name':name, 'country':country,'img_url':img_url, 'weather':weather, 'description':description})
