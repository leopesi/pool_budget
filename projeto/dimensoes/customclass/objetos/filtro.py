
from .dbs.database import Database

class Filtro():
    def __init__(self, dimensao):
        self.dimensao = dimensao
        self.config = {}
        self.config['filtros'] = Database('filtros')
        self.config['tampa_casa_maquinas'] = Database('tampa_casa_maquinas')

    def dimensionamento_filtro_grupo(self):  # Dimensiona o filtro, baseado no volume dágua, e retorna o ID.
        dimensao = self.dimensao
        filtros = self.config['filtros'].lista()

        for filtro in filtros:
            if dimensao.m3real() < filtro['capacidade maxima']:
                return filtro

        return 'Nao existe filtro com a capacidade adequada cadastrado no sistema'

    def dimensionamento_tampa_casa_de_maquinas_grupo (self): #Dimensiona a tampa da casa de máquinas baseado no ID do Filtro.
        dimensao = self.dimensao
        tampa_casa_maquinas = self.config['tampa_casa_maquinas'].lista()
        filtro = self.dimensionamento_filtro_grupo()

        for chave in tampa_casa_maquinas:
            if filtro['id'] <= 5:
                if chave['id'] == 1:
                    return chave
            elif filtro['id'] >= 6:
                if chave['id'] == 2:
                    return chave
            else:
                return 'Não foi encontrado uma tampa de casa de máquinas adequada para este filtro'

    def quantidade_de_areia_no_filtro (self): # refatorar para possibilitar a inclusão de outros filtros
        dimensao = self.dimensao
        dimensionamento_filtro = self.dimensionamento_filtro_grupo()

        if dimensionamento_filtro['id'] <= 2:
            return 1 #Incluir o atributo "areia" no filtro
        elif dimensionamento_filtro['id'] == 3:
            return 2
        elif dimensionamento_filtro['id'] == 4:
            return 3
        elif dimensionamento_filtro['id'] == 5:
            return 5
        elif dimensionamento_filtro['id'] == 6:
            return 8
        elif dimensionamento_filtro['id'] == 7:
            return 12
        elif dimensionamento_filtro['id'] == 8:
            return 21
        else:
            return 'Error'

