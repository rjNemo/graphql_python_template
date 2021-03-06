import graphene

from app.schema.types.todo import TodoResponseField
from app.usecases.todo import close_todo


class CloseTodo(graphene.Mutation):
    """Close an existing task"""

    class Arguments:
        todo_id = graphene.String(required=True)

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, todo_id: str):
        todo = close_todo(todo_id)
        return CloseTodo(TodoResponseField(todo=todo))
