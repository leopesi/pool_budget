from .models import ClienteModel, DimensaoModel, EspessuraModel, FornecedorModel, OrcamentoModel, RevestimentoCalcModel
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    comprimento1 = DimensaoModel.objects.values('comprimento')[0]
    comprimento = int(comprimento1.get('comprimento')) + 1
    espessura = EspessuraModel.objects.all()
    fornecedor = FornecedorModel.objects.all()

    context = {
        'comprimento': comprimento,
        'espessura': espessura,
        'fornecedor': fornecedor,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#-----------------------ORÇAMENTO------------------------------#

class OrcamentoListView(generic.ListView):
    model = OrcamentoModel
    paginate_by = 10
    context_object_name = 'orcamento_lista'
    template_name = 'front/orcamento_lista.html'

class OrcamentoDetailView(generic.DetailView):
    model = OrcamentoModel
    context_object_name = 'orcamento_lista'
    template_name = 'front/orcamento_detalhado.html'

class OrcamentoCreateView(generic.CreateView):
    model = OrcamentoModel
    fields = '__all__'
    context_object_name = 'orcamento_incluir'
    template_name = 'front/orcamento_incluir.html'

class OrcamentoDeleteView(generic.DeleteView):
    model = OrcamentoModel
    fields = '__all__'
    success_url = reverse_lazy('orcamento')
    context_object_name = 'orcamento_confirma_delete.'
    template_name = 'front/orcamento_confirma_delete.html'

#-----------------------REVESTIMENTO------------------------------#
class RevestimentoUpdateView(generic.UpdateView):
    model =  RevestimentoCalcModel
    fields = ['vinil_m2','isomanta_m2','perfil_fixo_m']
    context_object_name = 'revestimento_update'
    template_name = 'front/revestimento_update.html'

class RevestimentoDeleteView(generic.DeleteView):
    model =  RevestimentoCalcModel
    fields = ['vinil_m2','isomanta_m2','perfil_fixo_m']
    context_object_name = 'revestimento_update'
    template_name = 'front/revestimento_update.html'

#-----------------------CLIENTE------------------------------#

class ClienteListView(generic.ListView):
    model = ClienteModel
    paginate_by = 10
    context_object_name = 'cliente_lista'
    template_name = 'front/cliente_lista.html'

class ClienteDetailView(generic.DetailView):
    model = ClienteModel
    context_object_name = 'cliente_lista'
    template_name = 'front/cliente_detalhado.html'

class ClienteUpdateView(generic.UpdateView):
    model = ClienteModel
    fields = '__all__'
    context_object_name = 'cliente_update'
    template_name = 'front/cliente_update.html'