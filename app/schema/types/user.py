import graphene

from app.schema.types.response import ResponseField
from app.schema.types.todo import TodoType


class UserType(graphene.ObjectType):
    """User schema type"""

    user_id = graphene.String()
    username = graphene.String()
    tasks = graphene.List(TodoType)


class UserInputType(graphene.InputObjectType):
    """User input object"""

    user_id = graphene.String()
    username = graphene.String()


class UserListResponseField(graphene.ObjectType):
    """User list response object"""

    class Meta:
        interfaces = (ResponseField,)

    users = graphene.List(UserType)


class UserResponseField(graphene.ObjectType):
    """User response object"""

    class Meta:
        interfaces = (ResponseField,)

    user = graphene.Field(UserType)
