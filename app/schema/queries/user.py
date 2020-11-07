from app.schema.types.user import UserListResponseField, UserResponseField
from app.usecases.user import read_all_users, read_user_by_id


def resolve_list_users(self, info):
    users = read_all_users()
    return UserListResponseField(users=users)


def resolve_get_user(self, info, user_id: str):
    user, _ = read_user_by_id(user_id)
    return UserResponseField(user=user)
