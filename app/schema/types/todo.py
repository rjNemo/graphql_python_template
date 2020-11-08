import graphene

from app.schema.types.response import ResponseField


class TodoType(graphene.ObjectType):
    """Todo Object Type"""

    todo_id = graphene.String()
    title = graphene.String(default_value="")
    is_done = graphene.Boolean(default_value=False)


class TodoInputType(graphene.InputObjectType):
    """Todo Input Object"""

    todo_id = graphene.String()
    title = graphene.String(default_value="")
    is_done = graphene.Boolean(default_value=False)


class TodoResponseField(graphene.ObjectType):
    """Todo response object"""

    class Meta:
        interfaces = (ResponseField,)

    todo = graphene.Field(TodoType)


class TodoListResponseField(graphene.ObjectType):
    """Todos list response object"""

    class Meta:
        interfaces = (ResponseField,)

    todos = graphene.Field(graphene.List(TodoType))
