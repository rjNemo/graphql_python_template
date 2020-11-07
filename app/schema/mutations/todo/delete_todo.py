import graphene

from app.schema.types.todo import TodoResponseField
from app.usecases import delete_todo


class DeleteTodo(graphene.Mutation):
    class Arguments:
        todo_id = graphene.String(required=True)

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, todo_id: str):
        todo = delete_todo(todo_id)
        return DeleteTodo(TodoResponseField(todo=todo))