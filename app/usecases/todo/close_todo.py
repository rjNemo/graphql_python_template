from app.models.todo import Todo
from app.repositories.todos import get_todo_by_id, todo_exists


def close_todo(todo_id: str) -> Todo:
    if not todo_exists(todo_id):
        return None

    todo = get_todo_by_id(todo_id)
    todo.is_done = True
    return todo
