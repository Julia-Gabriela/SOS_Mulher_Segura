from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def cadastro_view(request):
    return render(request, 'cadastro/cadastro.html')
def contato(request):
    return render(request, 'contato.html')
def sobre(request):
    return render(request, 'sobre.html')
def registrar_denuncia(request):
    return render(request, 'registrar_denuncia.html')
def home_vitima(request):
    return render(request, 'home_vitima.html')
def denuncia_enviada(request):
    return render(request, 'denuncias/denuncia_enviada.html')