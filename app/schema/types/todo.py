import graphene


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


class ResponseField(graphene.ObjectType):
    is_success = graphene.Boolean(default_value=True)
    error_message = graphene.String()


class TodoResponseField(ResponseField):
    todo = graphene.Field(TodoType)


class TodoListResponseField(ResponseField):
    todos = graphene.Field(graphene.List(TodoType))


class CreateTodoResponseField(ResponseField):
    todo = graphene.Field(TodoType)
