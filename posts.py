from objects import Object

class Posts(Object):

    def __init__(self, user_id, title, body):
        """
        Constructor for Posts class
        """
        self.url = "https://gorest.co.in/public/v1/posts"
        self.id = None
        self.user_id = user_id
        self.title = title
        self.body = body

    def add(self):
        """
        Overrided method which calls parent's method for adding a post object
        """
        return super().add(user_id = self.user_id, title = self.title, body = self.body)






