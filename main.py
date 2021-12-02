from users import Users
from posts import Posts
from comments import Comments
from todos import Todos
import unittest
import pytest
from objects import Object
from tomls import TOML
import time

# class UserTesting(unittest.TestCase):
#
#     def test_get_user(self):
#         u = Users()
#         assert u.get()
#
#     def test_add_user(self):
#         u = Users()
#         assert u.add('asdfag', 'asdfas8172@yahoo.com', 'male', 'active')
#
#     def test_delete_user(self):
#         u = Users()
#         assert u.delete(42)
#
# class PostTesting(unittest.TestCase):
#
#     def test_get_post(self):
#         p = Posts()
#         assert p.get()
#
#     def test_add_post(self):
#         p = Posts()
#         assert p.add(50, 'asd', 'asd')
#
#     def test_delete_post(self):
#         p = Posts()
#         assert p.delete(60)
#
# class CommentTesting(unittest.TestCase):
#
#     def test_get_comment(self):
#         c = Comments()
#         assert c.get()
#
#     def test_add_comment(self):
#         c = Comments()
#         assert c.add(3, 'asd123', 'asd123@yahoo.com', 'body')
#
#     def test_delete_comment(self):
#         c = Comments()
#         assert c.delete(39)
#
# class TodoTesting(unittest.TestCase):
#     def test_get_todo(self):
#         t = Todos()
#         assert t.get()
#
#     def test_add_todo(self):
#         t = Todos()
#         assert t.add(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')
#
#     def test_delete_todo(self):
#         t = Todos()
#         assert t.delete(26)
#
# class CleanupTesting(unittest.TestCase):
#
#     def test_cleanup(self):
#         time.sleep(1)
#         u = Users()
#         u.add('asdfag', 'asdfas12833@yahoo.com', 'male', 'active')
#         t = Todos()
#         t.add(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')
#         c = Comments()
#         c.add(60, 'asd123', 'asd123@yahoo.com', 'body')
#         p = Posts()
#         p.add(60, 'asd1', 'asd1')
#         time.sleep(1)
#         Object.cleanup()
#         time.sleep(1)

class TestTOML:

    def test_users_toml(self):
        users = TOML.create_users()
        assert users == TOML.get_number_of_users()

    def test_posts_toml(self):
        posts = TOML.create_posts_for_user()
        assert posts == TOML.get_number_of_posts()

    def test_todos_toml(self):
        todos = TOML.create_todos_for_user()
        assert todos == TOML.get_number_of_todos()

    def test_users_objects_toml(self):
        t = TOML.create_users_objects()
        u = TOML.get_number_of_users_objects()
        assert t == u

    def test_users_objects_toml1(self):
        t = TOML.create_users_objects()
        u = TOML.get_number_of_users_objects()
        assert t == u


