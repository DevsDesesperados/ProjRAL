from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.models import Project, Engineer, CadastroOperacional,CadastroTecnico
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

@login_required(login_url='/login/')

def cadastro_legal(request):
    return render(request, 'cadastro-legal.html')

@login_required(login_url='/login/')

def submit_cadastro_legal(request):
    if request.POST:
        user = request.user
        ANM = request.POST.get('Processo_anm')
        substance = request.POST.get('substance')
        use = request.POST.get('use')
        if Project.objects.filter(ANM=ANM).exists():
            Project.objects.filter(ANM=ANM).update(substance=substance,use=use)
            messages.success(request,'Processo ANM modificado com sucesso')
            return redirect('/menu/cadastrolegal')
        else:
            Project.objects.create(user=user, ANM=ANM, substance=substance, use=use)
            messages.success(request, 'Processo ANM registrado com sucesso')
            return redirect('/menu/cadastrolegal')
    else:
        return redirect('/menu/cadastrolegal')

@login_required(login_url='/login/')

def cadastro_tecnico(request):
    return render(request, 'cadastro-tec.html')

def submit_cadastro_tecnico(request):
    if request.POST:
        cpf = request.POST.get('CPF')
        occupation = request.POST.get('Profissão')
        occupation_number = request.POST.get('Número1')
        jurisdiction = request.POST.get('jurisdiction')
        elaboration_number = request.POST.get('Número2')
        ral_jurisdiction = request.POST.get('Jurisdição')
        elaboration_date = request.POST.get('Data')
        public_authorization = request.POST.get('option')
        if Engineer.objects.filter(cpf=cpf).exists():
            cpf2= Engineer.objects.get(cpf=cpf)
            CadastroTecnico.objects.create(cpf=cpf2, occupation=occupation,occupation_number=occupation_number,jurisdiction=jurisdiction,elaboration_number=elaboration_number,elaboration_date=elaboration_date,ral_jurisdiction=ral_jurisdiction,public_authorization=public_authorization)
            messages.success(request, 'Cadastro técnico registrado com sucesso')
            return redirect('/menu/cadastrotecnico')
    else:
        return redirect('/menu/cadastrotecnico')


@login_required(login_url='/login/')

def cadastro_operacional(request):
    user = request.user
    anm_related = Project.objects.get(user=user)
    anm_process = anm_related.ANM
    record = CadastroOperacional.objects.filter(ANM=anm_process)
    context = {'records':record}
    return render(request, 'cadastro-operacional.html', context)

def submit_cadastro_operacional(request):
    if request.POST:
        ANM_submit = request.POST.get('Process_anm')
        operational_situation = request.POST.get('ANO-BASE')
        reason = request.POST.get('Virtude')
        if Project.objects.filter(ANM=ANM_submit).exists():
            ANM= Project.objects.get(ANM=ANM_submit)
            CadastroOperacional.objects.create(ANM=ANM, operational_situation=operational_situation, reason=reason)
            messages.success(request, 'Cadastro operacional registrado com sucesso')
            return redirect('/menu/cadastrooperacional')
    else:
        return redirect('/menu/cadastrooperacional')

def cadastrotec_lavra(request):
    return render(request, 'cadastro-Tec-Lavra.html')

def dados_minas(request):
    return render(request,'Dados-Minas-Info-Tec.html')

def demaisdados_minas(request):
    return render(request,'Minas-Demais-Dados.html')

def lavra_producaobruta(request):
    return render(request,'Lavra-Prod-Bruta.html')

def proj_producaobruta(request):
    return render(request,'Projeção-Prod-Bruta.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")