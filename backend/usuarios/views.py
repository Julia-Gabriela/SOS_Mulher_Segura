# usuarios/views.py

from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def home_vitimas(request):
    return render(request, 'usuarios/home.html')  # ajuste o caminho se necessário

def login_vitima(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(cpf_matricula=cpf, senha=senha)
            return redirect('home_vitimas')
        except Usuario.DoesNotExist:
            messages.error(request, 'CPF/Matrícula ou Senha incorretos.')

    return render(request, 'login/login.html')
def login_view(request):
    return render(request, 'login.html')