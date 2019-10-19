from graphene import ObjectType, Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Article


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['authors', 'title', 'standfirst', 'body', 'created_at', 'frontpage']
        interfaces = (Node,)


class NewsQuery(ObjectType):
    article = Node.Field(ArticleNode)
    articles = DjangoFilterConnectionField(ArticleNode)
