import graphene

from . import CreateTodo, DeleteTodo, UpdateTodo, CloseTodo


class Mutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    close_todo = CloseTodo.Field()
