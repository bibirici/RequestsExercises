from objects import Object

class Post(Object):

    def __init__(self, user_id, title, body):
        """
        Constructor for Posts class
        """
        self.id = None
        self.url = Object.base_url + '/posts'
        self.user_id = user_id
        self.title = title
        self.body = body

    def get_create_dictionary(self):
        json_add = {
            'user_id': self.user_id,
            'title': self.title,
            'body': self.body
        }
        return json_add

    def add(self):
        """
        Overrided method which calls parent's method for adding a post object
        """
        return super().add(user_id = self.user_id, title = self.title, body = self.body)






