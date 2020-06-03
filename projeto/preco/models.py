from django.db import models
from django.urls import reverse

class ProdutoModel(models.Model):
    produto = models.CharField(max_length=30)

    custo = models.FloatField(max_length=30)
    margem = models.FloatField(max_length=30)
    preco = models.FloatField(max_length=30)

    fornecedor = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    caracteristica = models.CharField(max_length=30)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('produto-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.produto}'

class ServicoModel(models.Model):

    servico = models.CharField(max_length=30)

    custo = models.FloatField(max_length=30)
    margem = models.FloatField(max_length=30)
    preco = models.FloatField(max_length=30)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('servico-id', args=[str(self.id)])

    def __str__(self):
        """String representando o objeto."""
        return f'{self.servico}'