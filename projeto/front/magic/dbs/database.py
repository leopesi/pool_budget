import ast
import json

class Database:
    def __init__(self, tabela):
        self.file = open('./dbs/' + tabela + '.json', 'r')
        self.table = tabela
        self.db = json.dumps(ast.literal_eval(self.file.read()))

    def lista(self):
        return json.loads(self.db)[self.table]

    def listaitem(self, item):
        return json.loads(self.db)[item]