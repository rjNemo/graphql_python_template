import graphene

from app.schema.types.user import UserResponseField
from app.usecases.user.create_user import create_user


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    result = graphene.Field(UserResponseField)

    def mutate(self, info, username: str):
        user = create_user(username)
        return CreateUser(UserResponseField(user=user))
