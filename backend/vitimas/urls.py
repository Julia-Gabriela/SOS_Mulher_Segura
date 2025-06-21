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
    path('contatos/', views.gerenciar_contatos, name='gerenciar_contatos'),
    path('contatos/adicionar/', views.adicionar_contato, name='adicionar_contato'),
    path('contatos/editar/<int:id_contato>/', views.editar_contato, name='editar_contato'),
    path('contatos/excluir/<int:id_contato>/', views.excluir_contato, name='excluir_contato'),
]
