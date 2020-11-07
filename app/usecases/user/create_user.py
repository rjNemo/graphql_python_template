from app.models.user import User
from app.repositories.users import add_user


def create_user(username: str) -> User:
    return add_user(username)
