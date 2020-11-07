import graphene

from app.schema.types.response import ResponseField
from app.schema.types.todo import TodoType


class UserType(graphene.ObjectType):
    user_id = graphene.String()
    username = graphene.String()
    tasks = graphene.List(TodoType)


class UserInputType(graphene.InputObjectType):
    user_id = graphene.String()
    username = graphene.String()


class UserListResponseField(ResponseField):
    users = graphene.List(UserType)


class UserResponseField(ResponseField):
    user = graphene.Field(UserType)
