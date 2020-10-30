from app.models.todo import Todo
from app.repositories.todos import edit_todo, todo_exists


def update_todo(todo_id: str, data) -> Todo:
    if todo_exists(todo_id):
        return edit_todo(todo_id, data)
    return None
