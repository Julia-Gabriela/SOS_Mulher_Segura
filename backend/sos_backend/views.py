from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def cadastro_view(request):
    return render(request, 'cadastro/cadastro.html')