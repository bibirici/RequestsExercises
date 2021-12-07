import time

import toml
import random
from users import Users
from posts import Posts
from todos import Todos
from objects import Object

class TOML:

    users_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/users.toml"
    posts_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/posts.toml"
    todos_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/todos.toml"
    input_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/input_file.toml"
    objects_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/objects.toml"


    @staticmethod
    def create_users(users):
        """
        Method that creates users from a TOML file
        Parameters:
              users: a TOML file with one or more users
        """
        for user in users.values():
            u = Users(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))
            user_id = u.add().json()['data']['id']
            todos = user.get('todos',{})
            TOML.create_todos(todos, user_id)
            posts = user.get('posts',{})
            TOML.create_posts(posts, user_id)

    @staticmethod
    def create_posts(posts, uid = None):
        """
        Method that creates posts from a TOML file
        Parameters:
              posts: a TOML file with one or more posts
              uid(optional): id of an created user
              Possible values for uid:
                if uid is not provided, uid is obtained from TOML file,
                uid can be 'r' for a random user
        """
        for post in posts.values():
            if uid == 'r':
                user_id = TOML.get_random_user()
            else:
                user_id = post.get('user_id', uid)
            p = Posts(user_id, post.get('title'), post.get('body'))
            p.add()

    @staticmethod
    def create_todos(todos, uid = None):
        """
        Method that creates todos from a TOML file
        Parameters:
              todos: a TOML file with one or more todos
              uid(optional): id of an created user
              Possible values for uid:
                if uid is not provided, uid is obtained from TOML file,
                uid can be 'r' for a random user
        """
        for todo in todos.values():
            if uid == 'r':
                user_id = TOML.get_random_user()
            else:
                user_id = todo.get('user_id', uid)
            t = Todos(user_id, todo.get('title'), todo.get('due_on'), todo.get('status'))
            t.add()

    @staticmethod
    def get_random_user():
        """
        Method that returns an id of a random user
        """
        users = [user.get('id') for user in Object.objects if user.get('object') == 'Users']
        user_id = random.choice(users)
        return user_id

    @staticmethod
    def toml_input(path):
        """
        Method that parses an TOML file and create all the objects in that file
        Parameters:
            path: path to the TOML file
        """
        text = toml.load(path)
        users = text.get('users', {})
        posts = text.get('posts', {})
        todos = text.get('todos', {})
        TOML.create_users(users)
        TOML.create_posts(posts)
        TOML.create_todos(todos)











