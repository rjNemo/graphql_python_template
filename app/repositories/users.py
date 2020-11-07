from typing import List

from app.models import Todo, User

jane = User("id", "Jane Doe")
jane.tasks = [Todo(title="Test")]
user_list: List[User] = [jane, User(username="John Doe")]


def get_all_users() -> List[User]:
    return user_list


def get_user_by_id(user_id: str) -> User:
    return [user for user in user_list if user.user_id == user_id][0]


def add_user(username: str) -> User:
    user = User(username=username)
    user_list.append(user)
    return user


def edit_user(user_id: str, data: dict) -> User:
    user = get_user_by_id(user_id)

    if username := data.get("username"):
        user.username = username

    return user


def user_exists(user_id: str) -> bool:
    return any([user.user_id == user_id for user in user_list])


def remove_user(user_id: str) -> User:
    user = get_user_by_id(user_id)
    index = user_list.index(user)
    return user_list.pop(index)


def add_todo_to_user(todo: Todo, user: User) -> bool:
    user.tasks.append(todo)
    return True
