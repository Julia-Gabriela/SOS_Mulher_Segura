
from django.urls import path
from .views import login_view, cadastro_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
]
