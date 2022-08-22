from django.shortcuts import render
from django.core.paginator import Paginator

from appsitesuplementos.models import Categoria, Produto


def index(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    data['categorias'] = Categoria.objects.all()
    paginator = Paginator(data['produtos'], 6)
    pages = request.GET.get('page')
    data['produtos'] = paginator.get_page(pages)
    return render(request, 'index.html', data, )

def usuarios(request):
    return render(request, 'usuarios.html')

def categorias(request):
    return render(request, 'categorias.html')

def produto(request, pk):
    data = {}
    data['produto'] = Produto.objects.get(id=pk)
    data['categorias'] = Categoria.objects.all()
    return render(request, 'produtos.html', data, )

def contato(request):
    return render(request, 'contato.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')
