from typing import Tuple

from app.models.todo import Todo
from app.repositories.todos import get_todo_by_id


def read_todo_by_id(todo_id: str) -> Tuple[Todo, bool]:
    try:
        return get_todo_by_id(todo_id), True
    except IndexError:
        return None, False
