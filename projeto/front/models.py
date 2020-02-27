from django.db import models
from localflavor.br.forms import BRPostalCodeField
from django.contrib.auth.models import User

class ClienteModel(models.Model):
    """Modelo representando as informações de cadastro do cliente."""

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero_casa = models.CharField(max_length=100, blank=True)
    cep = BRPostalCodeField(max_length=9, blank=True)
    telefone= models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length = 254, blank=True, help_text='Ex. clinte@gmail.com')

    class Meta:
        ordering = ['nome', 'sobrenome']

    def __str__(self):
        """String representando o objeto."""
        return f'{self.nome}, {self.sobrenome}'

class DimensaoModel(models.Model):
    """Modelo representando as dimensoões da piscina."""
    comprimento = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 8.00')
    largura = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 4.00')
    prof_inicial = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 1.20')
    prof_final = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 1.40')
    largura_calcada = models.CharField(max_length=3, null=False, blank=True, default= 1, help_text='Ex. 1.00')

    def __str__(self):
        """String representando o objeto."""
        return f'{self.comprimento},{self.largura},{self.prof_inicial},{self.prof_final}'

class EspessuraModel(models.Model):
    """Modelo representando a espessura do vinil da piscina."""

    escolher_espessura = [
        ['0.6', '0.6 mm'],
        ['0.7', '0.7 mm'],
        ['0.8', '0.8 mm'],
    ]

    espessura = models.CharField(
        max_length=3,
        choices=escolher_espessura,
        help_text='Espessura do vinil',
    )

    def __str__(self):
        """String representando o objeto."""
        return f'{self.espessura}'

class FornecedorModel(models.Model):
    """Modelo representando o fornecedor do vinil."""

    escolher_fornecedor = [
        ['sodramar', 'Sodramar'],
        ['viniplas', 'Viniplas'],
    ]

    fornecedor = models.CharField(
        max_length=8,
        choices=escolher_fornecedor,
        help_text='Fornecedor do vinil',
    )

    def __str__(self):
        """String representando o objeto."""
        return f'{self.fornecedor}'

class OrcamentoModel(models.Model):
    """Modelo representando o orçamento final apresentado ao usuário da aplicação."""

    dimensoes = models.ForeignKey('DimensaoModel', on_delete=models.SET_NULL, null=True)
    espessura = models.ForeignKey('EspessuraModel', on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey('FornecedorModel', on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey('ClienteModel', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)

    BUDGET_STATUS = (
        ('n', 'Em negociação'),
        ('c', 'Contrato'),
        ('e', 'Encerrado'),
    )

    status = models.CharField(
        max_length=1,
        choices=BUDGET_STATUS,
        blank=True,
        default='n',
        help_text='Status do Orçamento',
    )

    class Meta:
        ordering = ['cliente', 'data']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String representando o objeto."""
        return f'{self.cliente.nome}, {self.cliente.sobrenome}, {self.data}, {self.status}'