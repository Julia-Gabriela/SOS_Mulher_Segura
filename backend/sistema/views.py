from django.shortcuts import render
from django.urls import path
from . import views
from django.http import HttpResponse
import os
from django.conf import settings

urlpatterns = [
    # path('', views.alguma_view, name='alguma_view'),
]

def index(request):
    return HttpResponse("Página inicial do sistema")

def frontend_index(request):
    file_path = os.path.join(settings.BASE_DIR, 'frontend', 'index.html')
    with open(file_path, encoding='utf-8') as f:
        return HttpResponse(f.read())
def cadastro_view(request):
    return render(request, 'cadastro/cadastro.html')