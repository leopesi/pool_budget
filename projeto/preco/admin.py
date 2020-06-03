from django.contrib import admin
from .models import ProdutoModel, ServicoModel


class ProdutoInline(admin.TabularInline):
    model=ProdutoModel

admin.site.register(ProdutoModel)
admin.site.register(ServicoModel)
