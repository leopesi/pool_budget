from django.contrib import admin
from .models import ClienteModel, DimensaoModel
from .actions import negociacao, contrato, encerrado

# Register your models here.
@admin.register(ClienteModel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cidade',  'rua', 'numero_casa', 'telefone', 'email')
    list_filter = ('nome', 'cidade', 'bairro', )

@admin.register(DimensaoModel)
class DimensaoAdmin(admin.ModelAdmin):
    readonly_fields = ('data','cliente')
    fieldsets = (
        ('Cabeçalho',{
            'fields': ('cliente','status','data')
          }),
        ('Formulário', {
            'fields': ('espessura', 'fornecedor', 'comprimento', 'largura', 'prof_inicial','prof_final', 'largura_calcada')
        }),
        ('Dimensões Calculadas', {
            'classes': ('collapse',),
            'fields': (
            'profundidade_media', 'area_calcada', 'perimetro', 'm2_facial', 'm2_parede', 'm2_total', 'm3_total',
            'm3_real',)
        }),
        ('Conjunto Filtrante', {
            'classes': ('collapse',),
            'fields': (
            'filtro', 'motobomba', 'tampa_casa_maquinas', 'sacos_areia')
        }),

    )

    list_display = ('cliente', 'status', 'data', 'medidas')
    actions = [negociacao, contrato, encerrado]



    def medidas(self, obj):
        if obj.comprimento and obj.largura and obj.profundidade_media:
            return str(round(float(obj.comprimento),1)) + ' x ' + str(round(float(obj.largura),1)) + ' x ' + str(round(float(obj.profundidade_media),1))
        else:
            return 'Sem medidas'
    medidas.short_description = 'Medidas'

    list_filter = ('usuario', 'status', 'cliente', 'cliente__bairro','data',)
    search_fields = ('cliente',)

admin.site.site_header = "Painel de Controle"
admin.site.index_title = "Configurações"
admin.site.site_title = " "