from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect

from .models import ClienteModel, DimensaoModel
from .magic.estruturas.dimensao import Dimensao
from .magic.objetos.filtro import Filtro
from .magic.objetos.motor import Motor
from .magic.objetos.vinil import Vinil
from .forms import DimensaoForm, OrcamentoUpdateForm

def index(request):
    if request.method == "POST":
         form = DimensaoForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.usuario = request.user
             post.data = timezone.now()

             dimensoes = Dimensao(float(post.largura), float(post.comprimento), float(post.prof_inicial),float(post.prof_final) , float(post.largura_calcada))
             filtro = Filtro(dimensoes)
             motor = Motor(dimensoes)
             vinil = Vinil(post.espessura, post.fornecedor)

             # DIMENSÕES #
             post.prof_media = dimensoes.profundidade_media()
             post.area_calcada = dimensoes.area_da_calcada()
             post.perimetro = dimensoes.perimetro()
             post.m2_facial = dimensoes.m2facial()
             post.m2_parede = dimensoes.m2parede()
             post.m2_total = dimensoes.m2total()
             post.m3_total = dimensoes.m3total()
             post.m3_real = dimensoes.m3real()

             # KIT DE REVESTIMENTO #
             post.vinil_m2 = dimensoes.m2total()
             post.isomanta_m2 = dimensoes.m2facial()
             post.perfil_fixo_m = dimensoes.perimetro()

             # CONJUNTO FILTRANTE #
             post.filtro = filtro.dimensionamento_filtro_grupo()['marca'].title() + ' ' + filtro.dimensionamento_filtro_grupo()['modelo']
             post.motobomba = motor.dimensionamento_motobomba_grupo()['marca'].title() + ' - ' + motor.dimensionamento_motobomba_grupo()['modelo']
             post.tampa_casa_maquinas = filtro.dimensionamento_tampa_casa_de_maquinas_grupo()['modelo']
             post.sacos_areia = filtro.quantidade_de_areia_no_filtro()

             # MÃO DE OBRA #
             post.escavacao = dimensoes.m3total()
             post.construcao = dimensoes.m2total()
             post.contra_piso = dimensoes.area_da_calcada()
             post.remocao_terra = dimensoes.m3total()
             post.instalacao_vinil = dimensoes.m2total()

             post.save()
             return redirect('orcamento-id', pk=post.pk)
         else:
             return render(request, 'index.html', {'form': form})

    else:
        form = DimensaoForm()
        return render(request, 'index.html', {'form': form})

class DimensaoBulk(generic.View):
    def get(self, request):
        dimensoes = ['profundidade_media','area_calcada','perimetro','m2_facial','m2_parede','m2_total','m3_total','m3_real']
        list_dimensoes = []
        model = DimensaoModel

        for item in model:
            valor = 10
            item = valor
            list_dimensoes.append(item)

            DimensaoModel.objects.bulk_create(list_dimensoes)

            return HttpResponse('Funcionou')

#-----------------------ORÇAMENTO------------------------------#

class OrcamentoListView(generic.ListView):
    model = DimensaoModel
    paginate_by = 30 #Exibe uma lista de no máximo 10 itens por vez
    context_object_name = 'lista_orcamento' #Nome do objeto
    template_name = 'front/orcamento_list.html' #Nome e caminho do template

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return DimensaoModel.objects.select_related('cliente').get(id=pk)

    # ---------------------------------------------------------

class OrcamentoDetailView(generic.DetailView):
    model = DimensaoModel
    context_object_name = 'lista_orcamento'
    template_name = 'front/orcamento_detail.html'

    def get_object(self, queryset=None): # Evita o a consulta no BD das foreign-key 'cliente' e 'usuario'
        pk = self.kwargs.get(self.pk_url_kwarg)
        return DimensaoModel.objects.select_related('cliente', 'usuario').get(id=pk)

class OrcamentoUpdateView(generic.UpdateView): # todo: Testar o fields com '__all__'
    '''
    ------------DEBUG----------------
    import pdb; pdb.set_trace()
    l (mostra o ponto de verificação)
    n (next)
    c (continue)
    ---------------------------------
    '''
    model =  DimensaoModel
    form_class = OrcamentoUpdateForm
    context_object_name = 'update_orcamento'
    template_name = 'front/orcamento_update.html'

    def post(self, *args, **kwargs):
        formulario = self.get_form()
        print('**********')
        print(formulario.errors)
        print('**********')
        return super().post(*args, **kwargs)

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
    #success_url = reverse_lazy('cliente')
    context_object_name = 'delete_cliente'
    template_name = 'front/cliente_confirm_delete.html'

    def get_success_url(self): #Permite personalizar a visualização
        return reverse_lazy('cliente')
