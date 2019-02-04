import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from .models import Cliente



class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente
        filter_fields = {"nome": ["icontains"]}
        interfaces = (graphene.Node,)


class Query(graphene.AbstractType):
    clientes = DjangoFilterConnectionField(ClienteType)

    allclientes = graphene.List(ClienteType)

    def resolve_allclientes(self, info, **kwargs):
        return Cliente.objects.all()

    def resolve_clientes(self, info, **kwargs):
        return Cliente.objects.all()
