from typing import List

from app.models.user import User
from app.repositories.users import get_all_users


def read_all_users() -> List[User]:
    return get_all_users()
