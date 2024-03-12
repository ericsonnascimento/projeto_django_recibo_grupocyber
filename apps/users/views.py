from django.shortcuts import render

# Create your views here.

def users(request):
    return render(request, 'users/users.html')

def index(request):
    return render(request, 'users/login.html')