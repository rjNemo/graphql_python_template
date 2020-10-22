from app.repositories.todos import todo_exists, remove_todo


def delete_todo(todo_id: str) -> None:
    if todo_exists(todo_id):
        return remove_todo(todo_id)
