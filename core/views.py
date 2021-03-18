from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
    return render(request,'login.html')

@login_required(login_url='/login/')
def menu(request):
    return render(request, 'menu.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")