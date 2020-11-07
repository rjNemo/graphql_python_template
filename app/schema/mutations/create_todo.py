import graphene

from app.schema.types.todo import TodoResponseField
from app.usecases import create_todo


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(default_value="")

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, title: str):
        todo = create_todo(title)
        return CreateTodo(TodoResponseField(todo=todo))
