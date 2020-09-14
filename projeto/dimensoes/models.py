from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone
from .customclass.estruturas.dimensao import Dimensao
from .customclass.objetos.filtro import Filtro
from .customclass.objetos.motor import Motor

class ClienteModel(models.Model):
    """Modelo representando as informações de cadastro do cliente."""

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    estado = models.CharField(max_length=15, blank=True)
    cidade = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=20, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero_casa = models.CharField(max_length=10, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    telefone = models.IntegerField(blank=True, default=0)
    email = models.EmailField(max_length = 50, blank=True, help_text='Ex. clinte@gmail.com')

    @property
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        ordering = ['nome', 'sobrenome']

    def get_absolute_url(self):
        """Returns the url to access a particular instance."""
        return reverse('cliente-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.nome}, {self.sobrenome}'

class DimensaoModel(models.Model):
    cliente = models.ForeignKey(ClienteModel, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    """INPUT da piscina."""
    comprimento = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 8.00', default=0)
    largura = models.FloatField(max_length=5, null=False, blank=False, help_text='Ex. 4.00', default=0)
    prof_inicial = models.FloatField(max_length=5)
    prof_final = models.FloatField(max_length=3, null=False, blank=False, help_text='Ex. 1.40', default=0)
    largura_calcada = models.FloatField(max_length=3, null=False, blank=True, default= 1, help_text='Ex. 1.00')
    espessura = models.CharField(max_length=3)
    fornecedor = models.CharField(max_length=8)

    '''DIMENSÕES'''
    profundidade_media = models.CharField(max_length=25, null=False, blank=False, default= 0)
    area_calcada = models.CharField(max_length=25)
    perimetro = models.CharField(max_length=25)
    m2_facial = models.CharField(max_length=25)
    m2_parede = models.CharField(max_length=25)
    m2_total = models.CharField(max_length=25)
    m3_total = models.CharField(max_length=25)
    m3_real = models.CharField(max_length=25)

    """CONJUNTO FILTRANTE"""
    filtro = models.CharField(max_length=30)
    motobomba = models.CharField(max_length=30)
    tampa_casa_maquinas = models.CharField(max_length=30)
    sacos_areia = models.CharField(max_length=30)

    #BUDGET_STATUS = (('Em negociação', 'Em negociação'), ('Contrato', 'Contrato'), ('Encerrado', 'Encerrado'),)
    status = models.CharField(max_length=15, choices=(('Em negociação', 'Em negociação'), ('Contrato', 'Contrato'), ('Encerrado', 'Encerrado')), blank=True, default='Em negociação', help_text='Status do Orçamento',)
    data = models.DateTimeField(blank=True, null=True)

    def prof_media(self, *args, **kwargs):
        dimensoes = Dimensao(self.largura,
                             self.comprimento,
                             self.prof_inicial,
                             self.prof_final,
                             self.largura_calcada)
        filtro = Filtro(dimensoes)
        motor = Motor(dimensoes)
        self.profundidade_media = dimensoes.profundidade_media()
        self.area_calcada = dimensoes.area_da_calcada()
        self.perimetro = dimensoes.perimetro()
        self.m2_facial = dimensoes.m2facial()
        self.m2_parede = dimensoes.m2parede()
        self.m2_total = dimensoes.m2total()
        self.m3_total = dimensoes.m3total()
        self.m3_real = dimensoes.m3real()
        self.filtro = filtro.dimensionamento_filtro_grupo()['marca'].title() + ' ' + \
                      filtro.dimensionamento_filtro_grupo()['modelo']
        self.motobomba = motor.dimensionamento_motobomba_grupo()['marca'].title() + ' - ' + \
                      motor.dimensionamento_motobomba_grupo()['modelo']
        self.tampa_casa_maquinas = filtro.dimensionamento_tampa_casa_de_maquinas_grupo()['modelo']
        self.sacos_areia = filtro.quantidade_de_areia_no_filtro()

        super(DimensaoModel, self).save(*args, **kwargs)
        return self.profundidade_media


    def publish(self):
        self.data = timezone.now()
        self.save()

    def get_absolute_url(self):
        """Returns the url to access a detailed."""
        return reverse('orcamento-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.comprimento}, {self.largura}, {self.prof_inicial},{self.prof_final},{self.largura_calcada}'

