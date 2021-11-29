from objects import Object

class Todos(Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/todos"

    def add(self, user_id, title, due_on, status):
        return super().add(user_id = user_id, title = title, due_on = due_on, status = status)

    def get(self, id=''):
        return super().get(id = id)

    def delete(self, id=''):
        return super().delete(id = id)
