# -*- coding: utf-8 -*-
from .dbs.database import Database


class Vinil:
    def __init__(self, espessura, fornecedor):
        self.espessura = espessura
        self.fornecedor = fornecedor
        self.config = {}
        self.config['vinil'] = Database('vinils').lista()

    def vinil_grupo(self):
        return

    def escolha_fornecedor(self):
        fornecedor = self.fornecedor
        variavel = []
        for chave in self.config['vinil']:
            if chave['fornecedor'] == fornecedor:
                variavel.append(chave)
        return variavel

    def choose_thickness(self):
        espessura = self.espessura
        for chave in self.escolha_fornecedor():
            if chave['espessura'] == espessura:
                return chave
