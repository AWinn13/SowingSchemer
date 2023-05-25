from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *


def index(request):
    return render(request, "index.html")

# def register(request):


def login(request):
        
    return render(request, "login.html")

def loginUser(request):
    if request.method == 'POST':
        userEmail = User.objects.get(email=request.POST['email'])
        userPassword = User.objects.get(password = request.POST['password'])
        if userEmail:
            redirect('/')
    return redirect('/login')

def register(request):
    errors = User.objects.clean(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/login")
    else:
        if request.method == 'POST':
            request.session['first_name'] = request.POST['first_name']
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = User(
                first_name = first_name,
                last_name = last_name,
                email = email, 
                password = password
            )
            new_user.save()
            return redirect('/', request.session['first_name'])
    return render(request, "login.html")


def gardenjournal(request):
    return render(request, "gardenjournal.html")

def createjournal(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('title')
        date = request.POST.get('date')
        completed = request.POST.get('completed')
        todo = request.POST.get('todo')
        soil_temp = request.POST.get('soilTemp')
        air_temp = request.POST.get('airTemp')
        weather = request.POST.get('weather')
        planted = request.POST.get('planted')
        observation = request.POST.get('observation')

        # Create and save a new instance of the model
        new_entry = GardenJournal(
            title=title,
            date=date,
            completed=completed,
            todo=todo,
            soilTemp=soil_temp,
            airTemp=air_temp,
            weather=weather,
            planted=planted,
            observation=observation
        )
        new_entry.save()
        print(new_entry)
        # Redirect to a success page or the desired URL
        return redirect('/')
    return render(request, "gardenjournal.html")

def seedlingjournal(request):
    return render(request, 'seedlingJournal.html')


