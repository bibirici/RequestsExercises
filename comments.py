from objects import Object

class Comment(Object):

    def __init__(self, post_id, name, email, body):
        """
        Constructor for Comments class
        """
        self.url = Object.base_url + '/comments'
        self.id = None
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def get_create_dictionary(self):
        json_add = {
            'post_id': self.post_id,
            'name': self.name,
            'email': self.email,
            'body': self.body
        }
        return json_add

    def add(self):
        """
        Overrided method which calls parent's method for adding a comment object
        """
        return super().add(post_id = self.post_id, name = self.name, email = self.email, body = self.body)

