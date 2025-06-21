from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from django.utils.dateparse import parse_date
from django.contrib.auth.hashers import make_password
from denuncias.models import Denuncia
from django.contrib.auth import logout


@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            data_nascimento = parse_date(request.POST.get('data_nascimento'))
            telefone = request.POST.get('telefone')
            cep = request.POST.get('cep')
            bairro = request.POST.get('bairro')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            cidade = request.POST.get('cidade')
            uf = request.POST.get('uf')
            senha = request.POST.get('senha')

            if not nome or not cpf or not email or not senha:
                return render(request, 'cadastro/cadastro.html', {
                    'erro': 'Preencha todos os campos obrigatórios.'
                })

            senha_criptografada = make_password(senha)

            Usuario.objects.create(
                cpf=cpf,
                nome=nome,
                email=email,
                senha=senha_criptografada,
                telefone=telefone,
                data_nascimento=data_nascimento,
                cep=cep,
                bairro=bairro,
                numero=numero,
                complemento=complemento,
                cidade = cidade,
                uf = uf
            )

            return redirect('cadastro_finalizado')

        except Exception as e:
            return render(request, 'cadastro/cadastro.html', {
                'erro': f'Ocorreu um erro ao cadastrar: {str(e)}'
            })

    return render(request, 'cadastro/cadastro.html')


def cadastro_finalizado(request):
    return render(request, 'cadastro/cadastro_finalizado.html')

def home_vitima(request):
    cpf = request.session.get('cpf')  
    context = {
        'usuario': {'cpf': cpf} 
    }
    return render(request, 'home_vitima/home_vitima.html', context)

def historico_denuncia(request):
    cpf = request.session.get('cpf')

    if not cpf:
        return render(request, 'erro.html', {'mensagem': 'Usuário não autenticado.'})

    denuncias = Denuncia.objects.filter(cpf=cpf).order_by('-data_hora')

    context = {
        'denuncias': denuncias
    }

    return render(request, 'denuncias/historico_denuncia.html', context)

def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')

def sair(request):
    logout(request)
    return redirect('home') 

def medidas_protetivas(request):
    medidas = [
        {'status': 'Ativa', 'classe': 'ativa'},
        {'status': 'Solicitada', 'classe': 'solicitada'},
        {'status': 'Revogada', 'classe': 'revogada'},
    ]
    return render(request, 'configuracoes/medidas_protetivas.html', {'medidas': medidas})