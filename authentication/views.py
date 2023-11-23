import json
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


@csrf_exempt
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!",
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account deactivated."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please re-check your username or password."
        }, status=401)


@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "You are logged out."
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = UserCreationForm({"username": data['username'], "password1": data['password1'], "password2": data['password2']})
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "Registration sucessful!"
            }, status=200)
        else:
            test = messages.get_messages(request)

            return JsonResponse({
                "status": False,
                "message": "Registration failed. Please check the provided information.",
            }, status=401)

'''
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Registration successful!",
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Registration failed. Please check the provided information.",
            }, status=400)
'''
