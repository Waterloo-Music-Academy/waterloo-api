from graphene import ObjectType
from graphene.relay import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['name', 'bio', 'is_staff', 'articles', 'reviews']
        interfaces = (Node,)


class AccountsQuery(ObjectType):
    user = Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
