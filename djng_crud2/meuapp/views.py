# meuapp/views.py
from django.shortcuts import render, redirect
from .models import Produto
#from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'meuapp/lista_produtos.html')

def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        else:
            form = ProdutoForm()
        return render(request, 'meuapp/cria_produto.html', {'form': form})
    
def atualiza_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        else:
            form = ProdutoForm(instance=produto)
            return render(request, 'meuapp/atualiza_produto.html', {'form': form})
        
def delete_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'meuapp/deleta_produto.html', {'produto': produto})