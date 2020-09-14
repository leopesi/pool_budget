import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import ClienteModel, DimensaoModel

# Create a GraphQL type for the actor model
class ClienteType(DjangoObjectType):
    nome_completo = graphene.String(source='nome_completo')
    class Meta:
        model = ClienteModel
        fields = '__all__'


# Create a GraphQL type for the movie model
class DimensaoType(DjangoObjectType):
    class Meta:
        model = DimensaoModel

# Create a Query type
class Query(ObjectType):
    cliente = graphene.Field(ClienteType, id=graphene.Int())
    dimensao = graphene.Field(DimensaoType, id=graphene.Int())
    clientes = graphene.List(ClienteType)
    dimensoes = graphene.List(DimensaoType)

    def resolve_cliente(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ClienteModel.objects.get(pk=id)
        return None

    def resolve_dimensao(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return DimensaoModel.objects.get(pk=id)

        return None

    def resolve_clientes(self, info, **kwargs):
        return ClienteModel.objects.all()

    def resolve_dimensoes(self, info, **kwargs):
        return DimensaoModel.objects.all()

class ClienteInput(graphene.InputObjectType):
    id = graphene.ID()
    nome = graphene.String()
    sobrenome = graphene.String()
    estado = graphene.String()
    cidade = graphene.String()
    bairro = graphene.String()
    rua = graphene.String()
    numero_casa = graphene.String()
    cep = graphene.String()
    telefone = graphene.String()
    email = graphene.String()

class DimensaoInput(graphene.InputObjectType):
    id = graphene.ID()
    comprimento = graphene.Float()
    largura = graphene.Float()
    prof_inicial = graphene.Float()
    prof_final = graphene.Float()
    largura_calcada = graphene.Float()
    cliente = graphene.List(ClienteInput)
    espessura = graphene.String()
    fornecedor = graphene.String()


# Create mutations for actors
class CreateCliente(graphene.Mutation):
    class Arguments:
        input = ClienteInput(required=True)

    ok = graphene.Boolean()
    cliente = graphene.Field(ClienteType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        cliente_instance = ClienteModel(nome=input.nome,
                                        sobrenome=input.sobrenome,
                                        estado=input.estado,
                                        cidade=input.cidade,
                                        bairro=input.bairro,
                                        rua=input.rua,
                                        numero_casa=input.numero_casa,
                                        cep=input.cep,
                                        telefone=input.telefone,
                                        email=input.email,
                                        )
        cliente_instance.save()
        return CreateCliente(ok=ok, cliente=cliente_instance)

class UpdateCliente(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ClienteInput(required=True)

    ok = graphene.Boolean()
    cliente = graphene.Field(ClienteType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        cliente_instance = ClienteModel.objects.get(pk=id)
        if cliente_instance:
            ok = True
            cliente_instance.nome = input.nome
            cliente_instance.save()
            return UpdateCliente(ok=ok, cliente=cliente_instance)
        return UpdateCliente(ok=ok, cliente=None)

# Create mutations for movies
class CreateDimensao(graphene.Mutation):
    class Arguments:
        input = DimensaoInput(required=True)

    ok = graphene.Boolean()
    dimensao = graphene.Field(DimensaoType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        clientes = []
        for cliente_input in input.clientes:
          cliente = ClienteModel.objects.get(pk=cliente_input.id)
          if cliente is None:
            return CreateDimensao(ok=False, dimensao=None)
          clientes.append(cliente)
        dimensao_instance = DimensaoModel(
          comprimento=input.comprimento,
          largura=input.largura
          )
        dimensao_instance.save()
        dimensao_instance.cliente.set(clientes)
        return CreateDimensao(ok=ok, dimensao=dimensao_instance)

class UpdateDimensao(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = DimensaoInput(required=True)

    ok = graphene.Boolean()
    dimensao = graphene.Field(DimensaoType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        dimensao_instance = DimensaoModel.objects.get(pk=id)
        if dimensao_instance:
            ok = True
            clientes = []
            for cliente_input in input.dimensoes:
              cliente = ClienteModel.objects.get(pk=cliente_input.id)
              if cliente is None:
                return UpdateDimensao(ok=False, dimensao=None)
              clientes.append(cliente)
            dimensao_instance.comprimento=input.title
            dimensao_instance.largura=input.year
            dimensao_instance.save()
            dimensao_instance.cliente.set(clientes)
            return UpdateDimensao(ok=ok, dimensao=dimensao_instance)
        return UpdateDimensao(ok=ok, dimensao=None)

class Mutation(graphene.ObjectType):
    create_cliente = CreateCliente.Field()
    update_cliente = UpdateCliente.Field()
    create_dimensao = CreateDimensao.Field()
    update_dimensao = UpdateDimensao.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)