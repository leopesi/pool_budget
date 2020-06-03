from django import forms
from django.forms import ModelForm
from .models import ProdutoModel, ServicoModel

class ProdutoForm(ModelForm):
    class Meta:
        model = ProdutoModel
        fields = '__all__'

class ServicoForm(ModelForm):
    class Meta:
        model = ServicoModel
        fields = '__all__'

