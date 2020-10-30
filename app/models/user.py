from uuid import uuid4


class User:
    def __init__(self, user_id: str = None, username: str = "X"):
        self.user_id = user_id or uuid4()
        self.username = username
        self.tasks = []
