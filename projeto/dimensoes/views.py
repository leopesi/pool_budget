from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect

from .models import ClienteModel, DimensaoModel
from .forms import DimensaoForm, OrcamentoUpdateForm, ClienteForm


def index(request):
    if request.method == 'POST':
        dimensao_form = DimensaoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if dimensao_form.is_valid() and cliente_form.is_valid():
            post = dimensao_form.save(commit=False)
            cliente_post = cliente_form.save()

            post.cliente = cliente_post
            post.usuario = request.user
            post.data = timezone.now()
            post.save()
            return redirect('orcamento-id', pk=post.pk)

        else:
            return HttpResponse('Erro de operação')

    else:
        dimensao_form = DimensaoForm()
        cliente_form = ClienteForm()
        return render(
            request,
            'index.html',
            {'dimensao_form': dimensao_form, 'cliente_form': cliente_form},
        )


class DimensaoBulk(generic.View):
    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = DimensaoModel(produto=produto, preco=10)
            list_produtos.append(p)

        DimensaoModel.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')


# -----------------------ORÇAMENTO------------------------------#


class OrcamentoListView(generic.ListView):
    model = DimensaoModel
    paginate_by = 30   # Exibe uma lista de no máximo 10 itens por vez
    context_object_name = 'lista_orcamento'   # Nome do objeto
    template_name = (
        'dimensoes/orcamento_list.html'  # Nome e caminho do template
    )

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return DimensaoModel.objects.select_related('cliente').get(id=pk)

    # ---------------------------------------------------------


class OrcamentoDetailView(generic.DetailView):
    model = DimensaoModel
    context_object_name = 'lista_orcamento'
    template_name = 'dimensoes/orcamento_detail.html'

    def get_object(
        self, queryset=None
    ):   # Evita o a consulta no BD das foreign-key 'cliente' e 'usuario'
        pk = self.kwargs.get(self.pk_url_kwarg)
        return DimensaoModel.objects.select_related('cliente', 'usuario').get(
            id=pk
        )


class OrcamentoUpdateView(
    generic.UpdateView
):   # todo: Testar o fields com '__all__'
    """
    ------------DEBUG----------------
    import pdb; pdb.set_trace()
    l (mostra o ponto de verificação)
    n (next)
    c (continue)
    ---------------------------------
    """

    model = DimensaoModel
    form_class = OrcamentoUpdateForm
    context_object_name = 'update_orcamento'
    template_name = 'dimensoes/orcamento_update.html'

    def post(self, *args, **kwargs):
        formulario = self.get_form()
        print('**********')
        print(formulario.errors)
        print('**********')
        return super().post(*args, **kwargs)


class OrcamentoDeleteView(generic.DeleteView):
    model = DimensaoModel
    fields = '__all__'
    success_url = reverse_lazy(
        'orcamento'
    )   # Se confirmado o delete, redireciona para a página orcamento.
    context_object_name = 'delete_orcamento'
    # template_name = 'dimensoes/orcamento_list.html'
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# -----------------------CLIENTE------------------------------#


class ClienteListView(generic.ListView):
    model = ClienteModel
    paginate_by = 10
    context_object_name = 'lista_cliente'
    template_name = 'dimensoes/cliente_list.html'


class ClienteCreateView(generic.CreateView):
    model = ClienteModel
    fields = '__all__'
    context_object_name = 'create_cliente'
    template_name = 'dimensoes/cliente_create.html'


class ClienteDetailView(generic.DetailView):
    model = ClienteModel
    context_object_name = 'lista_cliente'
    template_name = 'dimensoes/cliente_detail.html'


class ClienteUpdateView(generic.UpdateView):
    model = ClienteModel
    fields = '__all__'
    context_object_name = 'update_cliente'
    template_name = 'dimensoes/cliente_update.html'


class ClienteDeleteView(generic.DeleteView):
    model = ClienteModel
    fields = '__all__'
    # success_url = reverse_lazy('cliente')
    context_object_name = 'delete_cliente'
    template_name = 'dimensoes/cliente_confirm_delete.html'

    def get_success_url(self):   # Permite personalizar a visualização
        return reverse_lazy('cliente')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
