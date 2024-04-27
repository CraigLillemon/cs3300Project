from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import TrailForm, CreateUserForm
import requests
import json
from itertools import zip_longest
import urllib.request
from django.contrib.auth.models import Group
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .decorate import allowed_users
# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
   states = State.objects.all()
   return render( request, 'trail_app/index.html', {'states':states})
def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        group = Group.objects.get(name='manager_role')
        user.groups.add(group)
        #user = User.objects.create(user=user)
        
        trailFolder = TrailFolders.objects.create()
        user.trailFolder = trailFolder
        user.save()
        messages.success(request, 'Account was create for ' + username)
        return redirect('login')
    context={'form':form}
        
    return render(request, 'registration/register.html', context)
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout')
    return render(request, 'registration/logout.html')
    



def state_list(request):
# Render the HTML template index.html with the data in the context variable.
   states = State.objects.all()
   return render( request, 'trail_app/state_list.html', {'states':states})

def get_coordinates(zip_code):
   
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": zip_code,
        "key": 'AIzaSyB3QtY3d8TLuX_RJDlgcKsvhPi3XBlL6_U'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")
        return None, None

def state_detail(request, pk):
    # Define the Tomorrow.io API URL with your API key and location coordinates
    state = State.objects.get(id=pk)
    trails = Trail.objects.all().filter(state_id=pk).filter(is_active=True)
    trail_data_list = []
    for trail in trails:

        #latitude, longitude = get_coordinates(trail.zip_code)
        latitude = 38.9301
        longitude = 104.8805
        api_key = 'ae5d1984ae12b5f2f131ae14d16e16c6'
        api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=imperial'
    
    
        source = urllib.request.urlopen(api_url)
        list_of_data = json.loads(source.read())
        data = {
                "temp": str(list_of_data['main']['temp']) + ' °F',
                "humidity": str(list_of_data['main']['humidity']),
                "speed": str(list_of_data['wind']['speed']),
                "main": str(list_of_data['weather'][0]['main']),
                "icon": (list_of_data['weather'][0]['icon']),
        }
        trail.weather = data
        trail_data_list.append(data)
        zipped_data = zip_longest(trails, trail_data_list)
    return render(request, 'trail_app/state_detail.html', {'state': state, 'zipped_data': zipped_data})

@login_required(login_url='login')
def user_state_detail(request, pk):
    # Define the Tomorrow.io API URL with your API key and location coordinates
    state = State.objects.get(id=pk)
    trails = Trail.objects.all().filter(state_id=pk).filter(is_active=True)
    trail_data_list = []
    for trail in trails:

        #latitude, longitude = get_coordinates(trail.zip_code)
        latitude = 38.9301
        longitude = 104.8805
        api_key = 'ae5d1984ae12b5f2f131ae14d16e16c6'
        api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=imperial'
    
    
        source = urllib.request.urlopen(api_url)
        list_of_data = json.loads(source.read())
        data = {
                "temp": str(list_of_data['main']['temp']) + ' °F',
                "humidity": str(list_of_data['main']['humidity']),
                "speed": str(list_of_data['wind']['speed']),
                "main": str(list_of_data['weather'][0]['main']),
                "icon": (list_of_data['weather'][0]['icon']),
        }
        trail.weather = data
        trail_data_list.append(data)
        zipped_data = zip_longest(trails, trail_data_list)
    return render(request, 'trail_app/user_state_detail.html', {'state': state, 'zipped_data': zipped_data})
@login_required(login_url='login')
def createTrail(request, pk):
    state = State.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            trail = form.save(commit=False)  
            trail.state = state
            trail.save()  
            return redirect('state-detail', pk=pk)
    else:
        form = TrailForm()  
    
    context = {'form': form}
    return render(request, 'trail_app/createTrail.html', context)

def trail_detail(request, pk):
   trail = Trail.objects.get(id = pk)
   #latitude, longitude = get_coordinates(trail.zip_code)
   latitude = 38.9301
   longitude = 104.8805
   api_key = 'ae5d1984ae12b5f2f131ae14d16e16c6'
   api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&cnt=3&appid={api_key}&units=imperial'
   trail_data_list = []
   source = urllib.request.urlopen(api_url)
   list_of_data = json.loads(source.read())
   data = {
                "temp": str(list_of_data['main']['temp']) + ' °F',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "speed": str(list_of_data['wind']['speed']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": (list_of_data['weather'][0]['icon']),
    } 
   trail_data_list.append(data)
   return render(request, 'trail_app/trail_detail.html', {'trail': trail, 'trail_data_list' : trail_data_list, 'latitude':latitude, 'longitude':longitude})
