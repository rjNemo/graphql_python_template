import graphene


class ResponseField(graphene.Interface):
    """Response interface"""

    is_success = graphene.Boolean(default_value=True)
    error_message = graphene.String()
