from app.repositories.users import add_todo_to_user
from app.usecases.todo import read_todo_by_id
from app.usecases.user.read_user_by_id import read_user_by_id


def assign_todo_to_user(user_id: str, todo_id: str) -> bool:
    user, is_success = read_user_by_id(user_id)
    if not is_success:
        return False

    todo, is_success = read_todo_by_id(todo_id)
    if not is_success:
        return False

    return add_todo_to_user(todo, user)
