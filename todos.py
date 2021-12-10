from objects import Object

class Todo(Object):

    def __init__(self, user_id, title, due_on, status):
        """
        Constructor for Todos class
        """
        self.url = Object.base_url + '/todos'
        self.id = None
        self.user_id = user_id
        self.title = title
        self.due_on = due_on
        self.status = status

    def get_create_dictionary(self):
        json_add = {
            'user_id': self.user_id,
            'title': self.title,
            'due_on': self.due_on,
            'status': self.status
        }
        return json_add




