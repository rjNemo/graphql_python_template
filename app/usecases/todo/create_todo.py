from app.models.todo import Todo
from app.repositories.todos import add_todo


def create_todo(title: str) -> Todo:
    return add_todo(title)
