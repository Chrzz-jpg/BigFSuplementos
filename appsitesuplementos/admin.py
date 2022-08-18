from django.contrib import admin
from .models import Produto, Cliente, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'descricao')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'cpf')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)