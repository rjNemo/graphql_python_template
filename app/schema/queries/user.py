from app.schema.types.user import UserListResponseField, UserResponseField
from app.usecases.user.read_all_users import read_all_users
from app.usecases.user.read_user_by_id import read_user_by_id


def resolve_list_users(self, info):
    users = read_all_users()
    return UserListResponseField(users=users)


def resolve_get_user(self, info, user_id: str):
    user = read_user_by_id(user_id)
    return UserResponseField(user=user)
