from django.urls import path, include
from . import views
import os
urlpatterns = [
    path('api/', include('usuarios.urls')),
    path('', views.index, name='sistemas-index'),
]