import graphene

from app.schema.queries.todo import resolve_get_todo, resolve_list_todos
from app.schema.queries.user import resolve_get_user, resolve_list_users
from app.schema.types.todo import TodoListResponseField, TodoResponseField
from app.schema.types.user import UserListResponseField, UserResponseField


class Query(graphene.ObjectType):

    # Task Queries
    list_todos = graphene.Field(
        TodoListResponseField,
        resolver=resolve_list_todos,
        description="List existing tasks",
    )

    get_todo = graphene.Field(
        TodoResponseField,
        todo_id=graphene.String(required=True),
        resolver=resolve_get_todo,
        description="Retrieve an existing tasks",
    )

    # User Queries
    list_users = graphene.Field(
        UserListResponseField,
        resolver=resolve_list_users,
        description="List registered users",
    )

    get_user = graphene.Field(
        UserResponseField,
        user_id=graphene.String(required=True),
        resolver=resolve_get_user,
        description="Retrieve a registered user",
    )
