import graphene


class ResponseField(graphene.ObjectType):
    is_success = graphene.Boolean(default_value=True)
    error_message = graphene.String()
