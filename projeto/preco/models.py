from django.db import models
from django.urls import reverse

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

