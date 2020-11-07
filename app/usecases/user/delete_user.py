from typing import Tuple

from app.models.user import User
from app.repositories.users import user_exists, remove_user


def delete_user(user_id: str) -> Tuple[User, bool]:
    if not user_exists(user_id):
        return None, False

    return remove_user(user_id), True
