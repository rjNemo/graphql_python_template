import graphene

from app.schema.types.todo import TodoListResponseField, TodoResponseField
from .todo import resolve_get_todo, resolve_list_todos
from .user import resolve_list_users, resolve_get_user
from ..types.user import UserListResponseField, UserResponseField


class Query(graphene.ObjectType):
    """Schema Queries"""

    """Task Queries"""
    list_todos = graphene.Field(TodoListResponseField, resolver=resolve_list_todos)

    get_todo = graphene.Field(
        TodoResponseField,
        todo_id=graphene.String(required=True),
        resolver=resolve_get_todo,
    )

    """User Queries"""
    list_users = graphene.Field(UserListResponseField, resolver=resolve_list_users)

    get_user = graphene.Field(
        UserResponseField,
        user_id=graphene.String(required=True),
        resolver=resolve_get_user,
    )
