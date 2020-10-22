from typing import List

from app.models.todo import Todo

todo_list: List[Todo] = [
    Todo(title='First'),
    Todo(todo_id="ec73296f-e108-46a3-bfb3-b4237cb072ba", title='Second')
]


def get_all_todos() -> List[Todo]:
    return todo_list


def get_todo_by_id(todo_id: str) -> Todo:
    return [todo for todo in todo_list if todo.todo_id == todo_id][0]


def add_todo(title: str) -> Todo:
    todo = Todo(title=title)
    todo_list.append(todo)
    return todo


def edit_todo(todo_id: str, data) -> Todo:
    todo = get_todo_by_id(todo_id)

    if title := data.get("title"):
        todo.title = title
    if is_done := data.get("is_done"):
        todo.is_done = is_done

    return todo


def todo_exists(todo_id: str) -> bool:
    return any([todo.todo_id == todo_id for todo in todo_list])


def remove_todo(todo_id: str) -> Todo:
    todo = get_todo_by_id(todo_id)
    index = todo_list.index(todo)
    return todo_list.pop(index)
