from django.contrib import admin
from django.urls import path
from . import views
from .views import index, contato

urlpatterns = [
    path('', views.index),
    path('produto/', views.produto),
    path('categorias/', views.categorias),
    path('usuarios/', views.usuarios),
    path('contato/', contato),
]