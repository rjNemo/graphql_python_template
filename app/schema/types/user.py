import graphene

from app.schema.types.response import ResponseField


class UserType(graphene.ObjectType):
    user_id = graphene.String()
    username = graphene.String()


class UserListResponseField(ResponseField):
    users = graphene.List(UserType)


class UserResponseField(ResponseField):
    user = graphene.Field(UserType)
