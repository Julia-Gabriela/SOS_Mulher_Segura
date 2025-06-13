from django.urls import path
from . import views
import os
urlpatterns = [
    path('', views.index, name='sistemas-index'),
]