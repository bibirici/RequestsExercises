import unittest

import pytest
import sys
import argparse
import conftest
from objects import Object
from users import User
from posts import Post
from comments import Comment
from todos import Todo
from tomls import TOML

class TestClass():

    @pytest.mark.parametrize('name, email, gender, status',
                             [
                                 ('asd2', 'asdaTEST123bab55512a33s32s1@yahoo.com', 'male', 'active')
                             ]
                             )
    def test_add_new_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert u1.add()
        assert u1.get().json().get('data')['name'] == name
        assert u1.get().json().get('data')['email'] == email
        assert u1.get().json().get('data')['gender'] == gender
        assert u1.get().json().get('data')['status'] == status

    @pytest.mark.parametrize('name, gender, status',
                             [
                                 ('asd2', 'male', 'active'),
                                 ('asd3', 'male', 'active')
                             ]
                             )
    def test_add_user_without_email(self, name, gender, status):
        u1 = User(name, None, gender, status)
        assert not u1.add()

    @pytest.mark.parametrize('name, gender, status',
                             [
                                 ('asd2', 'male', 'active'),
                                 ('asd3', 'male', 'active')
                             ]
                             )
    def test_add_user_without_name(self, name, gender, status):
        u1 = User(name, None, gender, status)
        assert not u1.add()

    @pytest.mark.parametrize('email, gender, status',
                             [
                                 ('skjascnpp928amsk@yahoo.com', 'male', 'active'),
                                 ('AKlskYnwos98@yahoo.com', 'female', 'active')
                             ]
                             )
    def test_add_user_without_gender(self, email, gender, status):
        u1 = User(None, email, gender, status)
        assert not u1.add()

    @pytest.mark.parametrize('name, email, gender',
                             [
                                 ('asd2', 'sdjasfowah213ms@yahoo.com', 'male'),
                                 ('asd3', 'sdjasfowah213fms@yahoo.com', 'female'),
                             ]
                             )
    def test_add_user_without_status(self, name, email, gender):
        u1 = User(name, email, gender, None)
        assert not u1.add()

    @pytest.mark.parametrize('name, email, gender, status',
                                [
                                    ('asd2', 'asdaTEST1234AA@yahoo.com', 'male', 'active'),
                                    ('asd2', 'user@yahoo.com', 'female', 'active')
                                ]
                             )
    def test_add_existing_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert not u1.add()

    @pytest.mark.parametrize('name, email, gender, status',
                                [
                                    ('asd2', 'asdafadsdAA1A5555Assss@yahoo.com', 'male', 'active'),
                                    ('asd3', 'asdafadsdAA1A5555Asaasss@yahoo.com', 'male', 'active')
                                ]
                             )
    def test_delete_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert u1.add()
        assert u1.delete()


    @pytest.mark.parametrize('user_id, title, body',
                                [
                                    (435, 'title', 'body'),
                                    (435, 'title1', 'body1')
                                ]
                            )
    def test_add_post(self, user_id, title, body):
        p1 = Post(user_id, title, body)
        assert p1.add()
        assert p1.get().json().get('data')['user_id'] == user_id
        assert p1.get().json().get('data')['title'] == title
        assert p1.get().json().get('data')['body'] == body

    @pytest.mark.parametrize('title, body',
                             [
                                 ('titlea', 'body11'),
                                 ('title1s', 'body1234')
                             ]
                             )
    def test_add_post_without_uid(self, title, body):
        p1 = Post(None, title, body)
        assert not p1.add()

    @pytest.mark.parametrize('user_id, body',
                             [
                                 (435, 'body2'),
                                 (435, 'body13')
                             ]
                             )
    def test_add_post_without_title(self, user_id, body):
        p1 = Post(user_id, None, body)
        assert not p1.add()

    @pytest.mark.parametrize('user_id, title',
                             [
                                 (435, 'title123'),
                                 (435, 'TITLE123')
                             ]
                             )
    def test_add_post_without_body(self, user_id, title):
        p1 = Post(user_id, title, None)
        assert not p1.add()

    @pytest.mark.parametrize('user_id, title, body',
                                [
                                    (435, 'title11', 'body1'),
                                    (435, 'title12', 'body12')
                                ]
                            )
    def test_delete_post(self, user_id, title, body):
        p1 = Post(user_id, title, body)
        assert p1.add()
        assert p1.delete()

    @pytest.mark.parametrize('user_id, title, due_on, status',
                                [
                                    (435, 'title1asd', '2021-07-07T00:00:00.000+01:30', 'pending')
                                ]
                            )
    def test_add_todo(self, user_id, title, due_on, status):
        t1 = Todo(user_id, title, due_on, status)
        assert t1.add()
        assert t1.get().json().get('data')['user_id'] == user_id
        assert t1.get().json().get('data')['title'] == title
        assert t1.get().json().get('data')['due_on'] == due_on
        assert t1.get().json().get('data')['status'] == status

    @pytest.mark.parametrize('title, due_on, status',
                             [
                                 ('title1', '2021-12-16T00:00:00.000+04:30', 'pending'),
                                 ('title2', '2021-12-16T00:00:00.000+05:30', 'pending')
                             ]
                             )
    def test_add_todo_without_uid(self, title, due_on, status):
        t1 = Todo(None, title, due_on, status)
        assert not t1.add()

    @pytest.mark.parametrize('user_id, due_on, status',
                             [
                                 (435, '2021-12-16T00:00:00.000+04:30', 'pending'),
                                 (435, '2021-11-11T00:00:00.000+02:30', 'pending')
                             ]
                             )
    def test_add_todo_without_title(self, user_id, due_on, status):
        t1 = Todo(user_id, None, due_on, status)
        assert not t1.add()


    @pytest.mark.parametrize('user_id, title, due_on',
                             [
                                 (435, '2021-12-16T00:00:00.000+04:30', 'pending'),
                                 (435, '2021-11-11T00:00:00.000+02:30', 'pending')
                             ]
                             )
    def test_add_todo_without_status(self, user_id, title, due_on):
        t1 = Todo(user_id, title, due_on, None)
        assert not t1.add()


    @pytest.mark.parametrize('user_id, title, due_on, status',
                            [
                                (435, 'title2', '2021-12-18T00:00:00.000+02:30', 'pending'),
                                (435, 'title3', '2021-12-11T00:00:00.000+03:30', 'pending')
                            ]
                            )
    def test_delete_todo(self, user_id, title, due_on, status):
        t1 = Todo(user_id, title, due_on, status)
        assert t1.add()
        assert t1.delete()

    @pytest.mark.parametrize('users', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/users.toml"])
    def test_toml_users(self, users):
        Object.objects.clear()
        TOML.toml_input(users)
        assert len(Object.objects) == 3

    @pytest.mark.parametrize('todos', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/todos.toml"])
    def test_toml_todos(self, todos):
        TOML.toml_input(todos)
        TOML.toml_input(todos, t_users='random')
        assert len(Object.objects) == 6

    @pytest.mark.parametrize('posts', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/posts.toml"])
    def test_toml_posts(self, posts):
        TOML.toml_input(TOML.posts_file)
        TOML.toml_input(TOML.posts_file, p_users='random')
        assert len(Object.objects) == 9

    @pytest.mark.parametrize('users_objects', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/input_file.toml"])
    def test_toml_users_objects(self, users_objects):
        TOML.toml_input(users_objects)
        assert len(Object.objects) == 14





