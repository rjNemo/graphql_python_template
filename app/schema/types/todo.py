import graphene

from app.schema.types.response import ResponseField


class TodoType(graphene.ObjectType):
    """
    Query Object Type
    """

    todo_id = graphene.String()
    title = graphene.String(default_value="")
    is_done = graphene.Boolean(default_value=False)


class TodoInputType(graphene.InputObjectType):
    """
    Mutation Input Object Type
    """

    todo_id = graphene.String()
    title = graphene.String(default_value="")
    is_done = graphene.Boolean(default_value=False)


class TodoResponseField(ResponseField):
    todo = graphene.Field(TodoType)


class TodoListResponseField(ResponseField):
    todos = graphene.Field(graphene.List(TodoType))


class CreateTodoResponseField(ResponseField):
    todo = graphene.Field(TodoType)
