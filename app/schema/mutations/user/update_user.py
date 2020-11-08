import graphene

from app.models.user import User
from app.schema.types.user import UserInputType, UserResponseField
from app.usecases.user import update_user


class UpdateUser(graphene.Mutation):
    """Update user information"""

    class Arguments:
        user = UserInputType()

    result = graphene.Field(UserResponseField)

    def mutate(self, info, user: User):
        res, is_success = update_user(user.user_id, vars(user))
        error_message = "This user does not exist." if not is_success else None
        return UpdateUser(
            UserResponseField(
                user=res, is_success=is_success, error_message=error_message
            )
        )
