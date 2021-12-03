from objects import Object

class Users(Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/users"

    def add(
            self,
            name,
            email,
            gender,
            status
        ):
        return super().add(
            name = name,
            email = email,
            gender = gender,
            status = status
        )

    def get(
            self,
            id=''
        ):
        return super().get(
            id = id
        )

    def delete(
               self,
               id
        ):
        return super().delete(
            id = id
        )


