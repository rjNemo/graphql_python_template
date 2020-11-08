from app.models.todo import Todo
from app.repositories.todos import remove_todo, todo_exists


def delete_todo(todo_id: str) -> Todo:
    if todo_exists(todo_id):
        return remove_todo(todo_id)
