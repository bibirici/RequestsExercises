import objects

class Comments(objects.Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/comments"
        self.keys = ['post_id', 'name', 'email', 'body']

