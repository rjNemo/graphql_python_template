import graphene

from app.schema.mutations.todo import CreateTodo, DeleteTodo, CloseTodo, UpdateTodo
from app.schema.mutations.user import CreateUser, UpdateUser, DeleteUser


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