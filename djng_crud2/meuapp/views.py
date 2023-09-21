# produtos_files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def home(request):
    return render(request, 'produtos_files/home.html')

# done
def listar_produtos(request):
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produtos_files/listar_produtos.html', produtos)

# done
def cria_produto(request):
    form = ProdutoForm() 
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    return render(request, 'produtos_files/criar_formulario.html', {'form': form})

    
def atualiza_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos_files/atualiza_produto.html', {'form': form})

        
def deleta_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos_files/deleta_produto.html', {'produto': produto})