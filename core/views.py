from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.models import Project, Engineer


# Create your views here.

#   sets who is the user and request to login
def login_user(request):
    return render(request, 'login.html')


#  sets user authentication and login
def login_submit(request):
    if request.POST:
        username = request.POST['Usuário, CPF ou CNPJ']
        password = request.POST['Senha']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
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
    # gotta find a better name then 'show' LOL
    show = User.objects.filter(username=current_user)
    response = {'shows': show}
    return render(request, 'menu.html', response)


def cadastro_legal(request):
    return render(request, 'cadastro-legal.html')


def submit_cadastro_legal(request):
    if request.POST:
        user = request.user
        ANM = request.POST.get('Processo_anm')
        substance = request.POST.get('substance')
        use = request.POST.get('use')
        if Project.objects.filter(ANM=ANM).exists():
            Project.objects.filter(ANM=ANM).update(substance=substance, use=use)
            messages.success(request, 'Processo ANM modificado com sucesso')
            return redirect('/menu/cadastrolegal')
        else:
            Project.objects.create(user=user, ANM=ANM, substance=substance, use=use)
            messages.success(request, 'Processo ANM registrado com sucesso')
            return redirect('/menu/cadastrolegal')
    else:
        return redirect('/menu/cadastrolegal')


def cadastro_tecnico(request):
    return render(request, 'cadastro-tec.html')


def submit_cadastro_tecnico(request):
    pass


def cadastro_operacional(request):
    return render(request, 'cadastro-operacional.html')


def submit_cadastro_operacional(request):
    pass


def cadastro_tec_lavra(request):
    return render(request, 'cadastro-Tec-Lavra.html')


def submit_cadastro_tec_lavra(request):
    pass


def dados_minas(request):
    return render(request, 'dados-minas.html')


def submit_dados_minas(request):
    pass


def dados_minas_info_tec(request):
    return render(request, 'dados-minas-info-tec.html')


def submit_dados_minas_info_tec(request):
    pass


def lavra_prod_bruta(request):
    return render(request, 'Lavra-Prod-Bruta.html')


def submit_lavra_prod_bruta(request):
    pass


def minas_demais_dados(request):
    return render(request, 'Minas-Demais-Dados.html')


def submit_minas_demais_dados(request):
    pass

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
