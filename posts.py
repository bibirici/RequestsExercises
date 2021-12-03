from objects import Object

class Posts(Object):
    def __init__(self):
        self.url = "https://gorest.co.in/public/v1/posts"

    def add(
            self,
            user_id,
            title,
            body
        ):
        return super().add(
            user_id = user_id,
            title = title,
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




