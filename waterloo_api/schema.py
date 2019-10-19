import graphene

import accounts.schema
import music.schema
import news.schema
import reviews.schema


class RootQuery(accounts.schema.AccountsQuery, music.schema.MusicQuery,
                news.schema.NewsQuery, reviews.schema.ReviewsQuery, graphene.ObjectType):
    node = graphene.relay.Node.Field()


schema = graphene.Schema(query=RootQuery)
