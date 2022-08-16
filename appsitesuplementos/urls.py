from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('produtos/', views.produtos),
    path('categorias/', views.categorias),
    path('usuarios/', views.usuarios),
]