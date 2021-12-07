from objects import Object

class Todos(Object):

    def __init__(self, user_id, title, due_on, status):
        """
        Constructor for Todos class
        """
        self.url = "https://gorest.co.in/public/v1/todos"
        self.id = None
        self.user_id = user_id
        self.title = title
        self.due_on = due_on
        self.status = status

    def add(self):
        """
        Overrided method which calls parent's method for adding a todo object
        """
        return super().add(user_id = self.user_id, title = self.title, due_on = self.due_on, status = self.status)


