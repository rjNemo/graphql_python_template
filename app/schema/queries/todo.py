from typing import List

import graphene

from app.models.todo import Todo
from app.schema.types.todo import TodoType, TodoResponseField
from app.usecases import read_all_todos, read_todo_by_id


class TodoQuery(graphene.ObjectType):
    """
    Defines the query and how to interact with
    """
    list_todos = graphene.Field(graphene.List(TodoType))

    def resolve_list_todos(self, info) -> List[Todo]:
        return read_all_todos()

    get_todo = graphene.Field(TodoResponseField,
                              todo_id=graphene.String(required=True))

    def resolve_get_todo(self, info, todo_id: str) -> TodoResponseField:
        todo, is_success = read_todo_by_id(todo_id)
        error_message = "This element does not exist." if not is_success else None

        return TodoResponseField(todo=todo,
                                 is_success=is_success,
                                 error_message=error_message)
