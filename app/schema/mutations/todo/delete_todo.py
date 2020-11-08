import graphene

from app.schema.types.todo import TodoResponseField
from app.usecases.todo import delete_todo


class DeleteTodo(graphene.Mutation):
    """Delete an existing task"""

    class Arguments:
        todo_id = graphene.String(required=True)

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, todo_id: str):
        todo = delete_todo(todo_id)
        return DeleteTodo(TodoResponseField(todo=todo))
