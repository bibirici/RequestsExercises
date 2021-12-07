from objects import Object

class Users(Object):

    def __init__(self, name, email, gender, status):
        """
        Constructor for Users class
        """
        self.url = "https://gorest.co.in/public/v1/users"
        self.id = None
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def add(self):
        """
        Overrided method which calls parent's method for adding an user object
        """
        return super().add(name = self.name, email = self.email, gender = self.gender, status = self.status)




