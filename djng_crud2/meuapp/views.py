# produtos_files/views.py
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def home(request):
    return render(request, 'produtos_files/home.html')

def listar_produtos(request):
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produtos_files/lista_produtos.html', produtos)


def cria_produto(request):
    form = ProdutoForm() 
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    return render(request, 'produtos_files/criar_formulario.html', {'form': form})

    
def atualiza_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        else:
            form = ProdutoForm(instance=produto)
            return render(request, 'produtos_files/atualiza_produto.html', {'form': form})
        
def deleta_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos_files/deleta_produto.html', {'produto': produto})