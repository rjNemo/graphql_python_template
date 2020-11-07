from typing import Tuple

from app.models.user import User
from app.repositories.users import get_user_by_id


def read_user_by_id(user_id: str) -> Tuple[User, bool]:
    try:
        return get_user_by_id(user_id), True
    except IndexError:
        return None, False
