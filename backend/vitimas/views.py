from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Vitima

@csrf_exempt
def cadastrar_vitima(request):
    if request.method == 'POST':
        Vitima.objects.create(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            email=request.POST['email'],
            data_nascimento=request.POST['data_nascimento'],
            telefone=request.POST['telefone'],
            cep=request.POST['cep'],
            bairro=request.POST.get('bairro', ''),
            numero=request.POST['numero'],
            complemento=request.POST.get('complemento', ''),
            senha=request.POST['senha'],  # em produção, nunca salve senha em texto puro
        )
       # return redirect('/cadastro/cadastro_finalizado.html/')  # ou só retorne algo simples
    # Se quiser, pode retornar algo no GET, ou só deixar assim:
    return render(request, 'cadastro/cadastro.html')  # ou pode tirar se não usar template
