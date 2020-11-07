from app.models import User, Todo
from app.repositories.users import add_todo_to_user, remove_todo_from_user
from app.usecases.todo import read_todo_by_id
from app.usecases.user.read_user_by_id import read_user_by_id


def is_todo_assigned_to_user(user: User, todo: Todo) -> bool:
    return any([task == todo for task in user.tasks])


def assign_todo_to_user(user_id: str, todo_id: str) -> bool:
    user, is_success = read_user_by_id(user_id)
    if not is_success:
        return False

    todo, is_success = read_todo_by_id(todo_id)
    if not is_success:
        return False

    if is_todo_assigned_to_user(user, todo):
        return False

    return add_todo_to_user(todo, user)


def deassign_todo_to_user(user_id: str, todo_id: str) -> bool:
    user, is_success = read_user_by_id(user_id)
    if not is_success:
        return False

    todo, is_success = read_todo_by_id(todo_id)
    if not is_success:
        return False

    if not is_todo_assigned_to_user(user, todo):
        return False

    return remove_todo_from_user(todo, user)
