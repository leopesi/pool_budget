from django import forms
from django.forms import ModelForm
from .models import DimensaoModel, ClienteModel


class ClienteForm(ModelForm):
    model: ClienteModel
    nome = forms.CharField(max_length=3)







class CadastrarUsuario(forms.ModelForm):
    nome = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}),label = 'Nome')
    sobrenome = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'Sobrenome')
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'E-mail')
    confirma_email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'Confirmar E-mail')
    usuario = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'Login')
    senha = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'input_field'}), label = 'Senha')
    confirma_senha = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'input_field'}), label = 'Confirmar senha')

    class Meta:

        fields = ['nome', 'sobrenome', 'email', 'confirma_email', 'usuario', 'senha', 'confirma_senha']

    def clean(self):
        cleaned_data = super().clean()

        senha = cleaned_data.get('senha')
        confirma_senha = cleaned_data.get('confirma_senha')

        email = cleaned_data.get('email')
        confirma_email = cleaned_data['confirma_email']

        if senha != confirma_senha:
            raise forms.ValidationError('Senha não confere! Digite a mesma senha nos campos Senha e Confirmar Senha.')

        if email and confirma_email:
            if email != confirma_email:
                raise forms.ValidationError('E-Mail não confere! Digite o mesmo e-mail nos campos E-mail e Confirma E-mail')

        return cleaned_data