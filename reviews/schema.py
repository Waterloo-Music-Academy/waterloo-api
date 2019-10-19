from graphene import ObjectType, Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Review


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        filter_fields = ['authors', 'rating', 'album', 'standfirst', 'body', 'created_at']
        interfaces = (Node,)


class ReviewsQuery(ObjectType):
    review = Node.Field(ReviewNode)
    reviews = DjangoFilterConnectionField(ReviewNode)
