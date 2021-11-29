import toml
from users import Users
from posts import Posts
from comments import Comments
from todos import Todos
from objects import Object


class TOML:
    users_file = "C:/Users/ABibirici/TOML/users.toml"
    posts_file = "C:/Users/ABibirici/TOML/posts.toml"
    todos_file = "C:/Users/ABibirici/TOML/todos.toml"
    ids = []

    @staticmethod
    def get_number_of_users():
        text = toml.load(TOML.users_file)
        users = text.get('users')
        return len(users)

    @staticmethod
    def get_number_of_posts():
        text1 = toml.load(TOML.users_file)
        text2 = toml.load(TOML.posts_file)
        users = text1.get('users')
        posts = text2.get('posts')
        return len(users)*len(posts)

    @staticmethod
    def get_number_of_todos():
        text1 = toml.load(TOML.users_file)
        text2 = toml.load(TOML.todos_file)
        users = text1.get('users')
        todos = text2.get('todos')
        return len(users) * len(todos)

    @staticmethod
    def create_users(path = users_file):
        text = toml.load(path)
        u = Users()
        users = text.get('users')
        for user in users:
            u.add(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))

        for obj in Object.objects:
            TOML.ids.append(obj.get('id'))

        return len(TOML.ids)


    @staticmethod
    def create_posts_for_user(path = posts_file):
        posts = 0
        p = Posts()
        text = toml.load(path)
        for id in TOML.ids:
            for post in text.get('posts'):
                posts += 1
                p.add(id, post.get('title'), post.get('body'))

        return posts

    @staticmethod
    def create_todos_for_user(path = todos_file):
        todos = 0
        t = Todos()
        text = toml.load(path)
        for id in TOML.ids:
            for todo in text.get('todos'):
                todos += 1
                t.add(id, todo.get('title'), todo.get('due_on'), todo.get('status'))
        return todos
