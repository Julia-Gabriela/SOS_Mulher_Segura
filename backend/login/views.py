from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from vitimas.models import Usuario

def login_view(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(cpf=cpf)
            if check_password(senha, usuario.senha):
                # Login bem-sucedido
                return redirect('home_vitima')  # <-- Redireciona para a home_vitima
            else:
                messages.error(request, 'Senha incorreta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'CPF não encontrado.')

    return render(request, 'login/login.html')
