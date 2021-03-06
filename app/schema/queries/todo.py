"""
Defines the query and how to interact with
"""

from app.schema.types.todo import TodoListResponseField, TodoResponseField
from app.usecases.todo import read_all_todos, read_todo_by_id


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


def resolve_get_todo(self, info, todo_id: str) -> TodoResponseField:
    todo, is_success = read_todo_by_id(todo_id)
    error_message = "This element does not exist." if not is_success else None

    return TodoResponseField(
        todo=todo, is_success=is_success, error_message=error_message
    )
