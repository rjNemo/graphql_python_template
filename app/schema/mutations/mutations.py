import graphene

from . import CreateTodo, DeleteTodo, UpdateTodo, CloseTodo, CreateUser


class Mutations(graphene.ObjectType):
    # todos
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    close_todo = CloseTodo.Field()
    # user
    create_user = CreateUser.Field()
