from django.db import models
from localflavor.br.forms import BRPostalCodeField
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone
from .magic.estruturas.dimensao import Dimensao

class ClienteModel(models.Model):
    """Modelo representando as informações de cadastro do cliente."""

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    estado = models.CharField(max_length=15, blank=True)
    cidade = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=20, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero_casa = models.CharField(max_length=6, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    #cep = BRPostalCodeField(max_length=9, blank=True)
    telefone= models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length = 50, blank=True, help_text='Ex. clinte@gmail.com')

    @property
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        ordering = ['nome', 'sobrenome']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('cliente-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.nome}, {self.sobrenome}'

class DimensaoModel(models.Model):
    cliente = models.ForeignKey(ClienteModel, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    """INPUT da piscina."""
    comprimento = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 8.00', default=0)
    largura = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 4.00', default=0)
    prof_inicial = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 1.20', default=0)
    prof_final = models.CharField(max_length=3, null=False, blank=False, help_text='Ex. 1.40', default=0)
    largura_calcada = models.CharField(max_length=3, null=False, blank=True, default= 1, help_text='Ex. 1.00')

    escolher_espessura = [['0.6', '0.6 mm'],['0.7', '0.7 mm'],['0.8', '0.8 mm'],]
    espessura = models.CharField(max_length=3, choices=escolher_espessura, )

    escolher_fornecedor = [['sodramar', 'Sodramar'], ['viniplas', 'Viniplas'],]
    fornecedor = models.CharField(max_length=8, choices=escolher_fornecedor, )

    '''DIMENSÕES'''
    profundidade_media = models.FloatField(max_length=25, default=0)
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

    """REVESTIMENTO"""
    vinil_m2 = models.CharField(max_length=25)
    isomanta_m2 = models.CharField(max_length=25)
    perfil_fixo_m = models.CharField(max_length=25)

    """MÃO DE OBRA"""
    escavacao = models.CharField(max_length=30, default= 0)
    construcao = models.CharField(max_length=30, default= 0)
    contra_piso = models.CharField(max_length=30, default= 0)
    remocao_terra = models.CharField(max_length=30, default= 0)
    instalacao_vinil = models.CharField(max_length=30, default= 0)

    BUDGET_STATUS = (('Em negociação', 'Em negociação'), ('Contrato', 'Contrato'), ('Encerrado', 'Encerrado'),)
    status = models.CharField(max_length=15, choices=BUDGET_STATUS, blank=True, default='Em negociação', help_text='Status do Orçamento',)
    data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.data = timezone.now()
        self.save()


    array = [0]
    def media(self):  # Função de up-date do field profundidade_media pela função 'dimensoes.profundidade_media()' ou pelo input direto pelo usuário.
        inicial = self.prof_inicial
        final = self.prof_final
        profundidade = self.profundidade_media
        if profundidade == 0:  # Verifica o Field Prof.média e se for == 0, faz input pelo cálculo da média.
            self.array.append(profundidade)  # Guarda o valor atual
            print(f'1° Teste - Prof. Média= {self.profundidade_media} - Array={self.array}')
            self.profundidade_media = float(inicial + final) / 2
            print(self.profundidade_media, self.array[-1])
            self.array.pop(0)
            super().save()
        elif profundidade == self.array[
            -1]:  # Verifica o Field Prof.média e se for igual o último valor guardado, faz input pelo cálculo da média.
            self.array.append(profundidade)
            print(f'2° Teste - Prof. Média= {self.profundidade_media} - Array={self.array}')
            self.profundidade_media = float(inicial + final) / 2
            print(self.profundidade_media, self.array[-1])
            self.array.pop(0)
            super().save()
        elif profundidade != self.array[
            -1]:  # Verifica o Field Prof.média e se for diferente o último valor guardado, faz input pelo Field Prof.média.
            self.array.append(profundidade)
            print(f'3° Teste - Prof. Média= {self.profundidade_media} - Array={self.array}')
            self.profundidade_media = self.profundidade_media
            self.array.pop(0)
            print(self.profundidade_media, self.array[-1])
            super().save()

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('orcamento-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.comprimento}, {self.largura}, {self.prof_inicial},{self.prof_final},{self.largura_calcada}'

class PrecificacaoModel(models.Model):


    margem = models.CharField(max_length=30)
    preco = models.CharField(max_length=30)

    """CONJUNTO FILTRANTE"""
    filtro_preco = models.CharField(max_length=30)
    motobomba_preco = models.CharField(max_length=30)
    tampa_casa_maquinas_preco = models.CharField(max_length=30)
    sacos_areia_preco = models.CharField(max_length=30)

    """ACESSÓRIOS OBRIGATÓRIOS"""
    perfil_rigido_preco = models.CharField(max_length=30)
    ralo_fundo_preco = models.CharField(max_length=30)
    dispositivo_retorno_preco = models.CharField(max_length=30)
    dispositivo_aspiracao_preco = models.CharField(max_length=30)
    dispositivo_nivel_preco = models.CharField(max_length=30)

    """ACESSÓRIOS OPCIONAIS"""
    borda_preco = models.CharField(max_length=30)
    skimmer_preco = models.CharField(max_length=30)
    dispositivo_hidromassagem_preco = models.CharField(max_length=30)
    escada_preco = models.CharField(max_length=30)
    timer_preco = models.CharField(max_length=30)
    capa_termica_preco = models.CharField(max_length=30)
    capa_protecao_preco = models.CharField(max_length=30)

    """KIT ASPIRAÇÂO"""
    peneira_preco = models.CharField(max_length=30)
    mangueira_preco = models.CharField(max_length=30)
    ponteira_preco = models.CharField(max_length=30)
    adaptador_giratorio_preco = models.CharField(max_length=30)
    haste_aluminio_preco = models.CharField(max_length=30)
    rodo_aspirador_preco = models.CharField(max_length=30)
    escova_preco = models.CharField(max_length=30)

    """REVESTIMENTO"""
    vinil_preco = models.CharField(max_length=25)
    isomanta_preco = models.CharField(max_length=25)
    perfil_fixo_preco = models.CharField(max_length=25)

    """MÃO DE OBRA"""
    escavacao_preco = models.CharField(max_length=30, default= 0)
    construcao_preco = models.CharField(max_length=30, default= 0)
    remocao_terra_preco = models.CharField(max_length=30, default= 0)
    colocacao_material_preco = models.CharField(max_length=30, default=0)
    contra_piso_preco = models.CharField(max_length=30, default= 0)
    instalacao_skimmer_preco = models.CharField(max_length=30, default=0)
    instalacao_borda_preco = models.CharField(max_length=30, default=0)
    instalacao_escada_preco = models.CharField(max_length=30, default=0)
    instalacao_capa_termica_preco = models.CharField(max_length=30, default=0)
    instalacao_capa_protecao_preco = models.CharField(max_length=30, default= 0)
    instalacao_tampa_cm_preco = models.CharField(max_length=30, default=0)
    instalacao_vinil_preco = models.CharField(max_length=30, default=0)
    instalacao_filtro_preco = models.CharField(max_length=30, default=0)
    instalacao_motobomba_preco = models.CharField(max_length=30, default=0)

    @property
    def custo(self):
        return f'{self.filtro_preco} /{self.state}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('precificacao-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.filtro_preco}'
