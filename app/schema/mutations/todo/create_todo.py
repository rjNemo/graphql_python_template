import graphene

from app.schema.types.todo import TodoResponseField
from app.usecases.todo import create_todo


class CreateTodo(graphene.Mutation):
    """Create a new task."""

    class Arguments:
        title = graphene.String(required=True)

    result = graphene.Field(TodoResponseField)

    def mutate(self, info, title: str):
        todo = create_todo(title)
        return CreateTodo(TodoResponseField(todo=todo))
