import time

import toml
import random
from users import Users
from posts import Posts
from todos import Todos
from objects import Object


class TOML:
    users_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/users.toml"
    users_objects_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/users_objects.toml"
    posts_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/posts.toml"
    todos_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/todos.toml"
    input_file = "C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/input_file.toml"

    @staticmethod
    def get_number_of_objects(path):
        text = toml.load(path)
        users = text.get('users')
        posts = text.get('posts')
        todos = text.get('todos')
        if users:
            objects = len(users)
            for user in users:
                if user.get('todos'):
                    objects += 1
                if user.get('posts'):
                    objects += 1
        else:
            if posts:
                objects = len(text.get('posts'))
            elif todos:
                objects = len(text.get('todos'))
        return objects

    @staticmethod
    def delete_users():
        for obj in Object.objects:
            if obj.get("object") == "Users":
                id = obj.get("id")
                u = Users()
                u.delete(id)

    @staticmethod
    def toml_input(path):
        text = toml.load(path)
        users = text.get('users')
        nr = 0
        if users:
            for i in range(len(users)):
                u = Users()
                posts = users[i].get('posts')
                todos = users[i].get('todos')
                id = u.add(users[i].get('name'), users[i].get('email'), users[i].get('gender'), users[i].get('status')).json()['data']['id']
                if id:
                    nr += 1
                if posts:
                    p = Posts()
                    p.add(id, posts.get('title'), posts.get('body'))
                    nr += 1
                if todos:
                    t = Todos()
                    t.add(id, todos.get('title'), todos.get('due_on'), todos.get('status'))
                    nr += 1
        else:
            posts = text.get('posts')
            todos = text.get('todos')
            if posts:
                p = Posts()
                for i in range(len(posts)):
                    p.add(posts[i].get('user_id'), posts[i].get('title'), posts[i].get('body'))
                    nr += 1
            if todos:
                t = Todos()
                for i in range(len(todos)):
                    t.add(todos[i].get('user_id'), todos[i].get('title'), todos[i].get('due_on'), todos[i].get('status'))
                    nr += 1
        TOML.delete_users()
        return nr




