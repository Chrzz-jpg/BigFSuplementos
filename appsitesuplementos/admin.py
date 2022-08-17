from django.contrib import admin
from .models import Produtos, Cliente

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'descricao')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'cpf')

admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Cliente, ClienteAdmin)