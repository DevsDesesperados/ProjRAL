from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

#   sets who is the user and request to login
def login_user(request):
    return render(request,'login.html')

#  sets user authentication and login
def login_submit(request):
    if request.POST:
        username = request.POST['Usuário, CPF ou CNPJ']
        password = request.POST['Senha']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect('/')
    else:
        return redirect('/')

# makes user logout
def logout_user(request):
    logout(request)
    return redirect('/')

#   sets login url
@login_required(login_url='/login/')

#  sets menu page
def menu(request):

    # show the username in specified space in the menu
    current_user = request.user
    #gotta find a better name then 'show' LOL
    show = User.objects.filter(username=current_user)
    response = {'shows':show}
    return render(request, 'menu.html', response)

def cadastro_legal(request):
    return render(request, 'cadastro-legal.html')

def cadastro_tecnico(request):
    return render(request, 'cadastro-tec.html')

def cadastro_operacional(request):
    return render(request, 'cadastro-operacional.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")