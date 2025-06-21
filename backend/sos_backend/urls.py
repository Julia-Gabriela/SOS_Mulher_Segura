"""
URL configuration for sos_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    path('denuncias/', include('denuncias.urls')),
    path('contatos/', include('contatos.urls')),
    path('historico/', include('historico.urls')),
    path('medidas/', include('medidas_protetivas.urls')),
"""
from django.contrib import admin
from django.urls import path, include
from sistema.views import frontend_index 
from django.conf.urls.static import static
from django.conf import settings
import os
from django.views.generic import TemplateView
from sos_backend.settings import BASE_DIR
from sistema.views import cadastro_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('vitimas/', include('vitimas.urls')),
    path('sistema/', include('sistema.urls')),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', include('login.urls')),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('denuncias/', include('denuncias.urls')),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])