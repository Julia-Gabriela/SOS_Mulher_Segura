from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    # path('', views.alguma_view, name='alguma_view'),
]


def index(request):
    return HttpResponse("Página inicial de utils")