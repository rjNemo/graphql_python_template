import graphene

from app.schema.types.user import UserResponseField
from app.usecases.user import delete_user


class DeleteUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)

    result = graphene.Field(UserResponseField)

    def mutate(self, info, user_id: str):
        user, is_success = delete_user(user_id)
        error_message = "This user does not exist." if not is_success else None
        return DeleteUser(
            UserResponseField(
                user=user, is_success=is_success, error_message=error_message
            )
        )
