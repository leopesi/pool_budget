from django.contrib import admin
from .models import ClienteModel, DimensaoModel

# Register your models here.
@admin.register(ClienteModel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cidade', 'estado', 'rua', 'numero_casa', 'cep', 'telefone', 'email')

@admin.register(DimensaoModel)
class DimensaoAdmin(admin.ModelAdmin):
    list_display = ('comprimento', 'largura', 'prof_inicial','prof_final', 'largura_calcada')
