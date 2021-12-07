from users import Users
from posts import Posts
from comments import Comments
from todos import Todos
import unittest
import pytest
from objects import Object
from tomls import TOML
import time

class TestClass():


    def test_add_user(self):
        u = Users('asd1', 'asdafadsdAAA33d@yahoo.com', 'male', 'active')
        assert u.add()

    def test_get_user(self):
        u = Users('asd2', 'asdafadsdAA1@yahoo.com', 'male', 'active')
        u.add()
        assert u.get()

    def test_delete_user(self):
        u = Users('asd3', 'asdafaddsAAs1@yahoo.com', 'male', 'active')
        u.add()
        assert u.delete()

    def test_toml1(self):
        TOML.toml_input(TOML.posts_file)

    def test_toml2(self):
        TOML.toml_input(TOML.todos_file)

    def test_cleanup(self):
        assert Object.cleanup()







