from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from Clientes.models import Usuario
from Clientes.models import PerfilImages


# Create your views here.


def index(request):
    return render(request,'index.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirecionar para a página inicial após o login
        else:
            return HttpResponse('Credenciais inválidas')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('index')

    
