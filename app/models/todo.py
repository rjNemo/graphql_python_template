from uuid import uuid4


class Todo:
    def __init__(self, title: str, todo_id: str = None, is_done: bool = False):
        self.todo_id = todo_id or str(uuid4())
        self.title = title
        self.is_done = is_done

    def __repr__(self):
        return f"Todo: {self.todo_id}, {self.title}, {self.is_done}"
