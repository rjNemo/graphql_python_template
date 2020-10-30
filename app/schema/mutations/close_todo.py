import graphene

from app.schema.types.todo import TodoType
from app.usecases.close_todo import close_todo


class CloseTodo(graphene.Mutation):
    class Arguments:
        todo_id = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, todo_id: str):
        todo = close_todo(todo_id)
        return CloseTodo(todo=todo)
