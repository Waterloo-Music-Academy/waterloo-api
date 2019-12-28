from graphene import ObjectType
from graphene.relay import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django_filters import FilterSet, OrderingFilter

from .models import Review


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = ['authors', 'rating', 'album', 'standfirst', 'body', 'created_at']

    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('frontpage', 'frontpage'),
            ('rating', 'rating')
        )
    )


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        filterset_class = ReviewFilter
        interfaces = (Node,)


class ReviewsQuery(ObjectType):
    review = Node.Field(ReviewNode)
    reviews = DjangoFilterConnectionField(ReviewNode)
