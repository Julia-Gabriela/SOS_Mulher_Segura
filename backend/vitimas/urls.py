from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/cadastro_finalizado', views.cadastrar_vitima, name='cadastrar_vitima'),
]
