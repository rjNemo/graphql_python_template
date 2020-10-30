import graphene

from app.schema.types.todo import TodoResponseField, TodoListResponseField
from app.usecases import read_all_todos, read_todo_by_id


class TodoQuery(graphene.ObjectType):
    """
    Defines the query and how to interact with
    """

    list_todos = graphene.Field(TodoListResponseField)

    def resolve_list_todos(self, info) -> TodoListResponseField:
        try:
            todos = read_all_todos()
            is_success = True
            error_message = None
        except Exception as e:
            error_message = str(e)
            is_success = False
            todos = None

        return TodoListResponseField(
            todos=todos, is_success=is_success, error_message=error_message
        )

    get_todo = graphene.Field(TodoResponseField, todo_id=graphene.String(required=True))

    def resolve_get_todo(self, info, todo_id: str) -> TodoResponseField:
        todo, is_success = read_todo_by_id(todo_id)
        error_message = "This element does not exist." if not is_success else None

        return TodoResponseField(
            todo=todo, is_success=is_success, error_message=error_message
        )
