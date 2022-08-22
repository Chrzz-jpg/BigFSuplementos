from django.urls import path
from . import views
from .views import cart, contato, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('produto/<int:pk>', views.produto),
    path('categorias/', views.categorias),
    path('usuarios/', views.usuarios),
    path('contato/', contato),
    path('cart/', cart),
    path('about/', about),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)