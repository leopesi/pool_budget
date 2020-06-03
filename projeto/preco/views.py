from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import ProdutoModel, ServicoModel
from .forms import ProdutoForm, ServicoForm

#-----------------------PRODUTO------------------------------#

def add_produto(request):
    print('*** 1 ***')
    if request.method == "GET":
        print('GET')
    if request.method == "POST":
        print('*** 2 ***')
        form = ProdutoForm(request.POST)
        if form.is_valid():
            print('*** 3 ***')
            post = form.save(commit=False)
            post.save()

            return redirect('produto',  pk=post.pk)
        else:
            print('*** 4 ***')
            return HttpResponse('Erro de operação')
    else:
        print('*** 5 ***')
        form = ProdutoForm()
        return render(request, 'produto_create.html', {'form': form})

class ProdutoListView(ListView):
    model = ProdutoModel
    context_object_name = 'lista_produto'
    template_name = 'produto_list.html'

class ProdutoDetailView(DetailView):
    model = ProdutoModel
    context_object_name = 'lista_produto'
    template_name = 'produto_detail.html'

class ProdutoUpdateView(UpdateView):
    model = ProdutoModel
    fields = '__all__'
    context_object_name = 'update_produto'
    template_name = 'produto_update.html'

class ProdutoDeleteView(DeleteView):
    model = ProdutoModel
    fields = '__all__'
    success_url = reverse_lazy('produto')
    context_object_name = 'delete_produto'
    #template_name = 'front/cliente_confirm_delete.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

