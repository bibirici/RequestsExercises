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
    def create_user(
            name,
            email,
            gender,
            status
        ):
        u = Users()
        user = u.add(
            name,
            email,
            gender,
            status
        )
        id = user.json()['data']['id']
        return id

    @staticmethod
    def create_post(
            user_id,
            title,
            body
        ):
        p = Posts()
        p.add(
            user_id,
            title,
            body
        )

    @staticmethod
    def create_todo(
            id,
            title,
            due_on,
            status
        ):
        t = Todos()
        t.add(
            id,
            title,
            due_on,
            status
        )

    @staticmethod
    def toml_input(path):
        text = toml.load(path)
        users = text.get('users')
        if users:
            for i in range(len(users)):
                posts = users[i].get('posts')
                todos = users[i].get('todos')
                id = TOML.create_user(
                    users[i].get('name'),
                    users[i].get('email'),
                    users[i].get('gender'),
                    users[i].get('status')
                )
                if posts:
                    TOML.create_post(
                        id,
                        posts.get('title'),
                        posts.get('body')
                    )
                if todos:
                    TOML.create_todo(
                        id,
                        todos.get('title'),
                        todos.get('due_on'),
                        todos.get('status')
                    )
        else:
            posts = text.get('posts')
            todos = text.get('todos')
            if posts:
                for i in range(len(posts)):
                    TOML.create_post(
                        posts[i].get('user_id'),
                        posts[i].get('title'),
                        posts[i].get('body')
                    )
            if todos:
                for i in range(len(todos)):
                    TOML.create_todo(
                        todos[i].get('user_id'),
                        todos[i].get('title'),
                        todos[i].get('due_on'),
                        todos[i].get('status')
                    )
        #TOML.delete_users()

    @staticmethod
    def create_object(
            path,
            id = ''
        ):
        text = toml.load(path)
        posts = text.get('posts')
        todos = text.get('todos')
        if not id:
            users = [user.get('id') for user in Object.objects if user.get('object') == 'Users']
            user = random.randint(0, len(users) - 1)
            id = users[user]

        for i in range(len(posts)):
            posts[i].update({'user_id': id})
        for i in range(len(todos)):
            todos[i].update({'user_id': id})
        with open(path, "w") as toml_file:
            toml.dump(text, toml_file)
        TOML.toml_input(TOML.objects_file)









