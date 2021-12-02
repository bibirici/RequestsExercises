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
    created_users = []

    @staticmethod
    def delete_users():
        u = Users()
        for id in TOML.created_users:
            u.delete(id)

    @staticmethod
    def get_number_of_users():
        text = toml.load(TOML.users_file)
        users = text.get('users')
        return len(users)

    @staticmethod
    def get_number_of_users_objects():
        text = toml.load(TOML.users_objects_file)
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
    def create_users():
        text = toml.load(TOML.users_file)
        u = Users()
        users = text.get('users')
        Object.objects.clear()
        time.sleep(1)
        for user in users:
            u.add(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))
        TOML.created_users = [obj.get('id') for obj in Object.objects]
        return len(TOML.created_users)

    @staticmethod
    def create_users_objects():
        nr = 0
        lst = ['posts', 'todos']
        text = toml.load(TOML.users_objects_file)
        users = text.get('users')
        objects = text.get('objects')
        obj = random.choice(lst)
        item = random.randint(0, len(objects.get(obj)) - 1)
        Object.objects.clear()
        if obj == 'posts':
            p = Posts()
            u = Users()
            for user in users:
                u.add(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))
            TOML.created_users = [obj.get('id') for obj in Object.objects]
            for id in TOML.created_users:
                if p.add(id, objects['posts'][item].get('title'), objects['posts'][item].get('body')):
                    nr += 1
            time.sleep(3)
            TOML.delete_users()
        elif obj == 'todos':
            t = Todos()
            u = Users()
            for user in users:
                u.add(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))
            TOML.created_users = [obj.get('id') for obj in Object.objects]
            for id in TOML.created_users:
                if t.add(id, objects['todos'][item].get('title'), objects['todos'][item].get('due_on'), objects['todos'][item].get('status')):
                    nr += 1
            time.sleep(3)
            TOML.delete_users()
        Object.objects.clear()
        return nr


    @staticmethod
    def create_posts_for_user():
        posts = 0
        p = Posts()
        text = toml.load(TOML.posts_file)
        TOML.created_users = [obj.get('id') for obj in Object.objects]
        for id in TOML.created_users:
            for post in text.get('posts'):
                if p.add(id, post.get('title'), post.get('body')):
                    posts += 1
        return posts


    @staticmethod
    def create_todos_for_user():
        todos = 0
        t = Todos()
        text = toml.load(TOML.todos_file)
        for id in TOML.created_users:
            for todo in text.get('todos'):
                if t.add(id, todo.get('title'), todo.get('due_on'), todo.get('status')):
                    todos += 1
        return todos
