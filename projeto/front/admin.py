from django.contrib import admin
from .models import ClienteModel, DimensaoModel, EspessuraModel, FornecedorModel, DimensaoCalcModel, FiltranteCalcModel, RevestimentoCalcModel, Mao_obraCalcModel, EspessuraModel, FornecedorModel, OrcamentoModel

# Register your models here.
@admin.register(ClienteModel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cidade', 'estado', 'rua', 'numero_casa', 'cep', 'telefone', 'email')

@admin.register(DimensaoModel)
class DimensaoAdmin(admin.ModelAdmin):
    list_display = ('comprimento', 'largura', 'prof_inicial','prof_final', 'largura_calcada')

@admin.register(EspessuraModel)
class EspessuraAdmin(admin.ModelAdmin):
    list_display = ('espessura', 'teste')

@admin.register(FornecedorModel)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'teste')

#################################################################################################

@admin.register(DimensaoCalcModel)
class DimensaoCalcAdmin(admin.ModelAdmin):
    list_display = ('largura_calcada', 'profundidade_media', 'area_calcada', 'perimetro', 'm2_facial', 'm2_parede', 'm2_total', 'm3_total', 'm3_real')

@admin.register(FiltranteCalcModel)
class FiltranteCalcAdmin(admin.ModelAdmin):
    list_display = ('filtro', 'motobomba', 'tampa_casa_maquinas', 'sacos_areia')

@admin.register(RevestimentoCalcModel)
class RevestimentoCalcAdmin(admin.ModelAdmin):
    list_display = ('vinil_m2', 'espessura', 'marca', 'isomanta_m2', 'perfil_fixo_m')

@admin.register(Mao_obraCalcModel)
class Mao_obraCalcAdmin(admin.ModelAdmin):
    list_display = ('escavacao', 'construcao', 'contra_piso', 'filtro', 'motobomba', 'remocao_terra', 'instalacao_vinil')

#################################################################################################

@admin.register(OrcamentoModel)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cliente', 'data','dimensoes', 'dimensoes_calc', 'conj_filtrante', 'kit_revestimento', 'mao_obra' )
