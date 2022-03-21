from .dbs.database import Database
from .vinil import Vinil
from .filtro import Filtro
import locale


class Precificacao:
    def __init__(self, dimensao):
        self.dimensao = dimensao
        self.config = {}
        self.config['vinil'] = Database('vinils').lista()
        self.config['perfil_rigido'] = Database('perfil_rigido').lista()
        self.config['areia'] = Database('areia').lista()
        self.config['manta_revestimento'] = Database(
            'manta_revestimento'
        ).lista()
        self.config['mao_de_obra'] = Database('mao_de_obra')

    def moeda(self, valor):
        valor = valor
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(valor, grouping=True, symbol=None)
        return 'R$: %s' % valor

    # *** PRODUTOS ***

    def get_preco_produto(self, produto):
        for chave in self.config[produto]:
            return chave['preco']

    def preco_do_vinil_dimensionado(self, espessura, fornecedor):
        vinil = Vinil(espessura, fornecedor)
        dimensao = self.dimensao
        choose = vinil.choose_thickness()
        return dimensao.m2total() * choose['preco']

    def preco_perfil_rigido_dimensionado(self):
        dimensao = self.dimensao
        for chave in self.config['perfil_rigido']:
            return dimensao.perimetro() * chave['preco']

    def preco_manta_de_revestimento_dimensionado(self):
        dimensao = self.dimensao
        for chave in self.config['manta_revestimento']:
            return dimensao.m2facial() * chave['preco']

    def preco_tampa_casa_maquinas(self):
        dimensao = self.dimensao
        filtro = Filtro(dimensao)
        return filtro.dimensionamento_tampa_casa_de_maquinas_grupo()['preco']

    # *** MÃO DE OBRA***

    def get_preco_mao_de_obra(self, item):
        return self.config['mao_de_obra'].listaitem(item)['preco']

    def preco_escavacao_dimensionado(self):
        dimensao = self.dimensao
        return self.get_preco_mao_de_obra('escavacao') * dimensao.m3total()

    def preco_mao_de_obra_construcao_dimensionado(self):
        dimensao = self.dimensao
        return (
            self.get_preco_mao_de_obra('construcao_piscina')
            * dimensao.m2total()
        )

    def preco_remocao_de_terra_dimensionado(self):
        dimensao = self.dimensao
        return (
            self.get_preco_mao_de_obra('remocao_de_terra') * dimensao.m3total()
        )

    def preco_construcao_calcada(self):
        dimensao = self.dimensao
        return (
            self.get_preco_mao_de_obra('construcao_calcada')
            * dimensao.area_da_calcada()
        )
