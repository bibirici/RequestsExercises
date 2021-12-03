from objects import Object

class Comments(Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/comments"

    def add(
            self,
            post_id,
            name,
            email,
            body
        ):
        return super().add(
            post_id = post_id,
            name = name,
            email = email,
            body = body
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
               id=''
        ):
        return super().delete(
            id = id
        )
