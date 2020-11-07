from typing import Tuple

from app.models.user import User
from app.repositories.users import user_exists, edit_user


def update_user(user_id: str, data: dict) -> Tuple[User, bool]:
    if not user_exists(user_id=user_id):
        return None, False

    return edit_user(user_id, data), True
