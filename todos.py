import objects

class Todos(objects.Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/todos"
        self.keys = ['user_id', 'title', 'due_on', 'status']

