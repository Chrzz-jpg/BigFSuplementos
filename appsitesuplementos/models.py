from django.db import models

from django.db import models

class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    categoria = models.CharField('Categoria', max_length=50)
    descricao = models.CharField('Descrição do produto', max_length=500)


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    cpf = models.CharField('CPF do cliente', max_length=20)