import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from app.schema.mutations.mutations import Mutations
from app.schema.queries.todo import TodoQuery

app = FastAPI()
app.add_route(
    "/",
    GraphQLApp(schema=graphene.Schema(query=TodoQuery, mutation=Mutations)))
