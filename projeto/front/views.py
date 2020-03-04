from .models import DimensaoModel, EspessuraModel, FornecedorModel, OrcamentoModel
from django.views import generic
from django.shortcuts import render


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


class OrcamentoListView(generic.ListView):
    model = OrcamentoModel
    paginate_by = 10
    context_object_name = 'orcamento_lista'
    template_name = 'front/orcamento_lista.html'

class OrcamentoDetailView(generic.DetailView):
    model = OrcamentoModel
    context_object_name = 'orcamento_lista'
    template_name = 'front/orcamento_detalhado.html'
