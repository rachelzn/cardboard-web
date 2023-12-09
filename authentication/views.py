import json
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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
def register_flutter(request):
    if request.method == 'POST':
        try:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            if not username or not password:
                return JsonResponse({'message': 'Username and password are required.'}, status=400)
            
            # Additional validation checks can be added here (e.g., password strength, existing user check)
            
            user = User.objects.create(username=username, password=make_password(password))
            return JsonResponse({'message': 'User registered successfully.'}, status=201)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)
