import graphene

from app.models.todo import Todo
from app.schema.types.todo import TodoInputType, TodoResponseField
from app.usecases import update_todo


class UpdateTodo(graphene.Mutation):
    class Arguments:
        todo = TodoInputType()

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, todo: Todo):
        res = update_todo(todo.todo_id, todo.__dict__)
        return UpdateTodo(TodoResponseField(todo=res))
