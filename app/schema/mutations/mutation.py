import graphene

from app.schema.mutations.todo import CloseTodo, CreateTodo, DeleteTodo, UpdateTodo
from app.schema.mutations.user import (
    AssignTodoToUser,
    CreateUser,
    DeassignTodoToUser,
    DeleteUser,
    UpdateUser,
)


class Mutation(graphene.ObjectType):
    # todos
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    close_todo = CloseTodo.Field()
    # user
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    assign_todo_to_user = AssignTodoToUser.Field()
    deassign_todo_to_user = DeassignTodoToUser.Field()
