import graphene

from app.schema.types.todo import TodoType
from app.usecases import create_todo


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(default_value="")

    todo = graphene.Field(TodoType)

    def mutate(self, info, title: str):
        todo = create_todo(title)
        return CreateTodo(todo=todo)
