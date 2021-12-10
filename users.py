from objects import Object

class User(Object):

    def __init__(self, name, email, gender, status):
        """
        Constructor for Users class
        """
        self.url = Object.base_url + '/users'
        self.id = None
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def get_create_dictionary(self):
        json_add = {
            'name': self.name,
            'email': self.email,
            'gender': self.gender,
            'status': self.status
        }
        return json_add






