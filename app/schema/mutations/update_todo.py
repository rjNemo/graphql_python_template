import graphene

from app.models.todo import Todo
from app.schema.types.todo import TodoInputType, TodoType
from app.usecases import update_todo


class UpdateTodo(graphene.Mutation):
    class Arguments:
        todo = TodoInputType()

    todo = graphene.Field(TodoType)

    def mutate(self, info, todo: Todo):
        res = update_todo(todo.todo_id, todo.__dict__)
        return UpdateTodo(todo=res)