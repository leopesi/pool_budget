# -*- coding: utf-8 -*-
from .filtro import Filtro
from .dbs.database import Database

class Motor():
    def __init__(self, dimensao):
        self.dimensao = dimensao
        self.materiais = []
        self.config = {}
        self.config['motores'] = Database('motores')

    def add_materiais(self, material):
        self.materiais.append(material)

    def dimensionamento_motobomba_grupo(self):  # Relaciona a motobomba adequada para o filtro, baseado no ID do filtro.
        dimensao = self.dimensao
        motobomba = self.config['motores'].lista()
        filtro = Filtro(dimensao)
        dime_filtro = filtro.dimensionamento_filtro_grupo()

        for chave in motobomba:
            if dime_filtro['id'] <= 2:
                if chave['id'] == 1:
                    return chave
            elif dime_filtro['id'] == 3:
                if chave['id'] == 2:
                    return chave
            elif dime_filtro['id'] == 4:
                if chave['id'] == 3:
                    return chave
            elif dime_filtro['id'] == 5:
                if chave['id'] == 4:
                    return chave
            elif dime_filtro['id'] == 6:
                if chave['id'] == 5:
                    return chave
            elif dime_filtro['id'] == 7:
                if chave['id'] == 6:
                    return chave
            elif dime_filtro['id'] == 8:
                if chave['id'] == 7:
                    return chave
            else:
                return 'Nao existe motobomba com a capacidade adequada cadastrado no sistema'