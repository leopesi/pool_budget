from django import forms
from django.forms import ModelForm
from .models import DimensaoModel, ClienteModel

class DimensaoForm(ModelForm):

    espessura = forms.CharField(
        widget=forms.RadioSelect(choices=[
        ['0.6', '0.6 mm'],
        ['0.7', '0.7 mm'],
        ['0.8', '0.8 mm'],
    ]))

    fornecedor = forms.CharField(
        widget=forms.RadioSelect(choices=[
        ['sodramar', 'Sodramar'],
        ['viniplas', 'Viniplas'],
    ]))

    comprimento = forms.FloatField(
        label='Comprimento',
        help_text='Ex. 8.00',
        required=True,
    )

    prof_inicial = forms.FloatField(
        label='Prof. Inicial',
        help_text='Ex. 1.20',
        required=True,
    )

    prof_final = forms.FloatField(
        label='Prof. Final',
        help_text='Ex. 1.60',
        required=True,
    )

    largura_calcada = forms.FloatField(
        label='Calçada',
        help_text='Ex. 1.00',
        required=True,
    )

    class Meta:
        model = DimensaoModel
        fields = ( 'comprimento', 'largura', 'prof_inicial', 'prof_final', 'largura_calcada', 'espessura', 'fornecedor')

class OrcamentoUpdateForm(ModelForm):
    class Meta:
        model = DimensaoModel
        exclude = ('cliente', 'preco', 'produto')

class ClienteForm(ModelForm):
    numero_casa = forms.FloatField(
        label='Número',
        required=False,
    )

    class Meta:
        model = ClienteModel
        fields = ('nome',
                  'sobrenome',
                  'estado',
                  'cidade',
                  'bairro',
                  'rua',
                  'numero_casa',
                  'cep',
                  'telefone',
                  'email')

