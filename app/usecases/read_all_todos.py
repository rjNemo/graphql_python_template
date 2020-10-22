from typing import List

from app.models.todo import Todo
from app.repositories.todos import get_all_todos


def read_all_todos() -> List[Todo]:
    return get_all_todos()
