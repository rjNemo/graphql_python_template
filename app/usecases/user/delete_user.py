from typing import Tuple

from app.models.user import User
from app.repositories.users import remove_user, user_exists


def delete_user(user_id: str) -> Tuple[User, bool]:
    if not user_exists(user_id):
        return None, False

    return remove_user(user_id), True
