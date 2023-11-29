from graphql_auth.schema import UserQuery

from graphene_app.mutations import *
from .Ingles.queries import Query as InglesQuery
from .Espannol.queries import Query as EspannolQuery
from .mutations import AuthMutation


class Query(EspannolQuery, InglesQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
