import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware

from app.schema.mutations.mutations import Mutations
from app.schema.queries.todo import TodoQuery

origins = ["*"]
methods = ["*"]
headers = ["*"]


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=methods,
        allow_headers=headers,
    )
    app.add_route(
        "/", GraphQLApp(schema=graphene.Schema(query=TodoQuery, mutation=Mutations))
    )

    return app
