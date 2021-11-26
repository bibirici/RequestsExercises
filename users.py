import objects

class Users(objects.Object):
    def __init__(self):
        self.keys = ['name', 'email', 'gender', 'status']
        self.url = "https://gorest.co.in/public/v1/users"


