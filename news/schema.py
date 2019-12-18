from graphene import ObjectType, Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django_filters import FilterSet, OrderingFilter

from .models import Article


class ArticleFilter(FilterSet):
    class Meta:
        model = Article
        fields = ['authors', 'title', 'standfirst', 'body', 'created_at', 'frontpage']

    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('title', 'title'),
            ('frontpage', 'frontpage')
        )
    )


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filterset_class = ArticleFilter
        interfaces = (Node,)


class NewsQuery(ObjectType):
    article = Node.Field(ArticleNode)
    articles = DjangoFilterConnectionField(ArticleNode)
