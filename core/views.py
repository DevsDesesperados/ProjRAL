from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#   sets who is the user and request to login
def login_user(request):
    return render(request,'login.html')

#   sets login url
@login_required(login_url='/login/')

#  sets menu page
def menu(request):
    return render(request, 'menu/menu.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")