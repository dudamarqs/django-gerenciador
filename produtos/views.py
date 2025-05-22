from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        Produto.objects.create(nome=nome, preco=preco, estoque=estoque)
        return redirect('lista_produtos')
    return render(request, 'produtos/form.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        produto.nome = nome
        produto.preco = preco
        produto.estoque = estoque
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'produtos/form.html', {'produto': produto})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})



