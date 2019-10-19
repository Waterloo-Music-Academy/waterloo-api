from graphene import ObjectType, Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Genre, Label, Artist, Album


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = ['name', 'artists', 'albums']
        interfaces = (Node,)


class LabelNode(DjangoObjectType):
    class Meta:
        model = Label
        filter_fields = ['name', 'artists', 'albums']
        interfaces = (Node,)


class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = ['name', 'bio', 'deans_list', 'labels', 'genres', 'albums']
        interfaces = (Node,)


class AlbumNode(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = ['name', 'artists', 'genres', 'labels', 'release_date']
        interfaces = (Node,)


class MusicQuery(ObjectType):
    genre = Node.Field(GenreNode)
    genres = DjangoFilterConnectionField(GenreNode)

    label = Node.Field(LabelNode)
    labels = DjangoFilterConnectionField(LabelNode)

    artist = Node.Field(ArtistNode)
    artists = DjangoFilterConnectionField(ArtistNode)

    album = Node.Field(AlbumNode)
    albums = DjangoFilterConnectionField(AlbumNode)
