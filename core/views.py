from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
# Create your views here.

def login_user(request):
    return render(request, 'html-loginpage.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('Usuário, CPF ou CNPJ')
        password = request.POST.get('Senha')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            redirect('/')
    else
        redirect('/')