from django.db import models
from localflavor.br.forms import BRPostalCodeField
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class ClienteModel(models.Model):
    """Modelo representando as informações de cadastro do cliente."""

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cidade = models.CharField(max_length=20, blank=True)
    estado = models.CharField(max_length=15, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero_casa = models.CharField(max_length=6, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    #cep = BRPostalCodeField(max_length=9, blank=True)
    telefone= models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length = 50, blank=True, help_text='Ex. clinte@gmail.com')

    class Meta:
        ordering = ['nome', 'sobrenome']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('cliente-detalhado', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.nome}, {self.sobrenome}'

class DimensaoModel(models.Model):
    """Modelo representando as dimensoões de INPUT da piscina."""
    comprimento = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 8.00')
    largura = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 4.00')
    prof_inicial = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 1.20')
    prof_final = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 1.40')
    largura_calcada = models.FloatField(max_length=3, null=False, blank=True, default= 1, help_text='Ex. 1.00')

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('dimensao-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.comprimento}, {self.largura}, {self.prof_inicial},{self.prof_final},{self.largura_calcada}'

class EspessuraModel(models.Model):
    """Modelo representando a espessura do vinil da piscina."""

    teste = models.CharField(max_length=20, blank=True)

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

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('espessura-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.espessura}'

class FornecedorModel(models.Model):
    """Modelo representando o fornecedor do vinil."""
    teste = models.CharField(max_length=20, blank=True)

    escolher_fornecedor = [
        ['sodramar', 'Sodramar'],
        ['viniplas', 'Viniplas'],
    ]

    fornecedor = models.CharField(
        max_length=8,
        choices=escolher_fornecedor,
        help_text='Fornecedor do vinil',
    )

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('fornecedor-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.fornecedor}'

####################################################
class DimensaoCalcModel(models.Model):
    """Modelo representando as dimensões calculadas no backend, a partir da DimensãoModel."""

    largura_calcada = models.FloatField(max_length=5)
    profundidade_media = models.FloatField(max_length=5)
    area_calcada = models.FloatField(max_length=5)
    perimetro = models.FloatField(max_length=5)
    m2_facial = models.FloatField(max_length=5)
    m2_parede = models.FloatField(max_length=5)
    m2_total = models.FloatField(max_length=5)
    m3_total = models.FloatField(max_length=5)
    m3_real = models.FloatField(max_length=5)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('dimensaocalc-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.largura_calcada}, {self.profundidade_media}'

class RevestimentoCalcModel(models.Model):
    """Modelo representando os itens de revestimento, calculadas no backend, a partir da DimensãoModel."""

    vinil_m2 = models.FloatField(max_length=5)
    espessura = models.ForeignKey('EspessuraModel', on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey('FornecedorModel', on_delete=models.SET_NULL, null=True)
    isomanta_m2 = models.FloatField(max_length=5)
    perfil_fixo_m = models.FloatField(max_length=5)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('revestimentocalc-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.vinil_m2}, {self.espessura}'

class FiltranteCalcModel(models.Model):
    """Modelo representando os itens do Conjunto Filtrante, calculadas no backend, a partir da DimensãoModel."""

    filtro = models.CharField(max_length=30)
    motobomba = models.CharField(max_length=30)
    tampa_casa_maquinas = models.CharField(max_length=30)
    sacos_areia = models.CharField(max_length=30)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('filtrantecalc-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.filtro}, {self.motobomba}'

class Mao_obraCalcModel(models.Model):
    """Modelo representando informações de Mão de Obra, calculadas no backend, a partir da DimensãoModel."""

    escavacao = models.CharField(max_length=30)
    construcao = models.CharField(max_length=30)
    contra_piso = models.CharField(max_length=30)
    filtro = models.ForeignKey('FiltranteCalcModel', on_delete=models.PROTECT)
    motobomba = models.CharField(max_length=30)
    remocao_terra = models.CharField(max_length=30)
    instalacao_vinil = models.CharField(max_length=30)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('maoobracalc-detalhe', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.escavacao}, {self.construcao}'

################################################################

class OrcamentoModel(models.Model):
    """Modelo representando o orçamento final apresentado ao usuário da aplicação."""

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey('ClienteModel', on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)

    dimensoes = models.ForeignKey('DimensaoModel', on_delete=models.SET_NULL, null=True)
    dimensoes_calc = models.ForeignKey('DimensaoCalcModel', on_delete=models.SET_NULL, null=True)
    conj_filtrante = models.ForeignKey('FiltranteCalcModel', on_delete=models.SET_NULL, null=True)
    kit_revestimento = models.ForeignKey('RevestimentoCalcModel', on_delete=models.SET_NULL, null=True)
    mao_obra = models.ForeignKey('Mao_obraCalcModel', on_delete=models.SET_NULL, null=True)


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

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('orcamento-detalhado', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.cliente.nome}, {self.cliente.sobrenome}, {self.data}, {self.status}'