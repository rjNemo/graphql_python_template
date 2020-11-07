import graphene

from app.schema.types.response import ResponseField
from app.usecases.user import assign_todo_to_user


class AssignTodoToUser(graphene.Mutation):
    class Arguments:
        todo_id = graphene.String()
        user_id = graphene.String()

    result = graphene.Field(ResponseField)

    def mutate(self, info, todo_id: str, user_id: str):
        is_success = assign_todo_to_user(user_id=user_id, todo_id=todo_id)
        error_message = "Cannot assign todo to user." if not is_success else None

        return AssignTodoToUser(
            ResponseField(is_success=is_success, error_message=error_message)
        )
