from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastro_finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
    path('home_vitima/', views.home_vitima, name='home_vitima'),
    
]
