from objects import Object

class Comments(Object):

    def __init__(self, post_id, name, email, body):
        """
        Constructor for Comments class
        """
        self.url = "https://gorest.co.in/public/v1/comments"
        self.id = None
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def add(self):
        """
        Overrided method which calls parent's method for adding a comment object
        """
        return super().add(post_id = self.post_id, name = self.name, email = self.email, body = self.body)

