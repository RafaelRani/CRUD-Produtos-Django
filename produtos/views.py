from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # só tem acesso às views se estiver logado
from .models import Produto
from .forms import ProdutoForm


@login_required  # só tem acesso a essa view se estiver logado
def produtos_list(request):
    pesquisa = request.GET.get('pesquisa', None)

    # Se o form de pesquisa conter algum termo:
    if pesquisa:
        # busca por: descrição OU marca OU categoria OU preço contendo o termo pesquisado:
        produtos = Produto.objects.filter(descricao__icontains=pesquisa) | Produto.objects.filter(marca__icontains=pesquisa) | Produto.objects.filter(categoria__icontains=pesquisa) | Produto.objects.filter(preco__icontains=pesquisa)
        #[campo]__icontains: prsquisa em case insensitivo, contendo o termo como substring
    else:
        # retorna todos os itens da tabela ordenados por id de forma decrescente
        produtos = Produto.objects.all().order_by('-id')

    return render(request, 'produtos_list.html', {'produtos': produtos, 'pesquisa': pesquisa})


@login_required
def produtos_new(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_form.html', {'form': form})


@login_required
def produtos_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produtos_list')

    return render(request, 'produtos_form.html', {'form': form, 'update': True})


@login_required
def produtos_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('produtos_list')
