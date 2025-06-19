# usuarios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_vitima, name='login_vitima'),
    path('home/', views.home_vitimas, name='home_vitimas'),  
]
