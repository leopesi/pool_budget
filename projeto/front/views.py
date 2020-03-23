from .models import ClienteModel, DimensaoModel
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ClienteForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    comprimento1 = DimensaoModel.objects.values('comprimento')[0]
    comprimento = int(comprimento1.get('comprimento')) + 1


    context = {
        'comprimento': comprimento,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#-----------------------ORÇAMENTO------------------------------#

class OrcamentoListView(generic.ListView):
    model = DimensaoModel
    paginate_by = 10 #Exibe uma lista de no máximo 10 itens por vez
    context_object_name = 'lista_orcamento' #Nome do objeto
    template_name = 'front/orcamento_list.html' #Nome e caminho do template

class OrcamentoCreateView(generic.CreateView):
    model = DimensaoModel
    fields = '__all__'
    context_object_name = 'create_orcamento'
    template_name = 'front/orcamento_create.html'

class OrcamentoDetailView(generic.DetailView):
    model = DimensaoModel
    context_object_name = 'lista_orcamento'
    template_name = 'front/orcamento_detail.html'

class OrcamentoUpdateView(generic.UpdateView):
    model =  DimensaoModel
    fields = ["status",
              "comprimento",
              "largura",
              "prof_inicial",
              "prof_final",
              "largura_calcada",
              "espessura",
              "fornecedor",
              "profundidade_media",
              "area_calcada",
              "perimetro",
              "m2_facial",
              "m2_parede",
              "m2_total",
              "m3_total",
              "m3_real",
              "filtro",
              "motobomba",
              "tampa_casa_maquinas",
              "sacos_areia",
              "vinil_m2",
              "isomanta_m2",
              "perfil_fixo_m",
              "escavacao",
              "construcao",
              "instalacao_vinil",
              ]
    context_object_name = 'update_orcamento'
    template_name = 'front/orcamento_update.html'

class OrcamentoDeleteView(generic.DeleteView):
    model = DimensaoModel
    fields = '__all__'
    success_url = reverse_lazy('orcamento') #Se confirmado o delete, redireciona para a página orcamento
    context_object_name = 'delete_orcamento'
    template_name = 'front/orcamento_confirm_delete.html'

#-----------------------CLIENTE------------------------------#

class ClienteListView(generic.ListView):
    model = ClienteModel
    paginate_by = 10
    context_object_name = 'lista_cliente'
    template_name = 'front/cliente_list.html'

class ClienteCreateView(generic.CreateView):
    model = ClienteModel
    fields = '__all__'
    context_object_name = 'create_cliente'
    template_name = 'front/cliente_create.html'

class ClienteDetailView(generic.DetailView):
    model = ClienteModel
    context_object_name = 'lista_cliente'
    template_name = 'front/cliente_detail.html'

class ClienteUpdateView(generic.UpdateView):
    model = ClienteModel
    fields = '__all__'
    context_object_name = 'update_cliente'
    template_name = 'front/cliente_update.html'

class ClienteDeleteView(generic.DeleteView):
    model = ClienteModel
    fields = '__all__'
    success_url = reverse_lazy('cliente')
    context_object_name = 'delete_cliente'
    template_name = 'front/cliente_confirm_delete.html'