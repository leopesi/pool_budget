from django import forms
from django.forms import ModelForm
from .models import DimensaoModel, ClienteModel


class DimensaoForm(ModelForm):
        class Meta:
            model = DimensaoModel
            fields = ('cliente', 'comprimento', 'largura', 'prof_inicial', 'prof_final', 'largura_calcada', 'espessura', 'fornecedor')

class OrcamentoUpdateForm(ModelForm):
    class Meta:
        model = DimensaoModel
        exclude = ('cliente',)