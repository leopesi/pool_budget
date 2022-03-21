def negociacao(modeladmin, request, queryset):
    queryset.update(status='Em negociação')


negociacao.short_description = 'Em negociação'


def contrato(modeladmin, request, queryset):
    queryset.update(status='Contrato')


contrato.short_description = 'Contrato'


def encerrado(modeladmin, request, queryset):
    queryset.update(status='Encerrado')
