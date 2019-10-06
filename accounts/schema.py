from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['name', 'bio', 'is_staff', 'articles', 'reviews']
        interfaces = (relay.Node,)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
