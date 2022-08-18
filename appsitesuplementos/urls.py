from django.urls import path
from . import views
from .views import cart, contato

urlpatterns = [
    path('', views.index),
    path('produtos/', views.produtos),
    path('categorias/', views.categorias),
    path('usuarios/', views.usuarios),
    path('contato/', contato),
    path('cart/', cart),
]