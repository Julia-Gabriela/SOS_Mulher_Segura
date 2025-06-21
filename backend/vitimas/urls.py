from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastro_finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
    path('home_vitima/', views.home_vitima, name='home_vitima'),
    path('historico/', views.historico_denuncia, name='historico_denuncia'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('sair/', views.sair, name='sair'),
    path('medidas_protetivas/', views.medidas_protetivas, name='medidas_protetivas'),
]
