from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_denuncia, name='registrar_denuncia'),
    path('enviada/', views.denuncia_enviada, name='denuncia_enviada'),
]
