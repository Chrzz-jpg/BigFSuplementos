from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios (request):
    return render(request, 'usuarios.html')

def categorias(request):
    return render(request, 'categorias.html')

def produtos(request):
    return render(request, 'produtos.html')

def contato(request):
    return render(request, 'contato.html')

def cart(request):
    return render(request, 'cart.html')