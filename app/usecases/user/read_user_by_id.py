from app.models.user import User
from app.repositories.users import get_user_by_id


def read_user_by_id(user_id: str) -> User:
    return get_user_by_id(user_id)
