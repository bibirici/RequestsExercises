import pytest
from objects import Object
from users import User
from posts import Post
from comments import Comment
from todos import Todo
from tomls import TOML

class TestClass():

    @pytest.mark.parametrize('name, email, gender, status',
                             [
                                 ('asd2', 'asdaTEST1234AsAA121@yahoo.com', 'male', 'active')
                             ]
                             )
    def test_add_new_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert u1.add()
        assert u1.get()

    @pytest.mark.parametrize('name, gender, status',
                             [
                                 ('asd2', 'male', 'active')
                             ]
                             )
    def test_add_user_without_email(self, name, gender, status):
        u1 = User(name, None, gender, status)
        assert not u1.add()

    @pytest.mark.parametrize('name, email, gender, status',
                                [
                                    ('asd2', 'asdaTEST1234AA@yahoo.com', 'male', 'active')
                                ]
                             )
    def test_add_existing_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert u1.add() == False

    @pytest.mark.parametrize('name, email, gender, status',
                                [
                                    ('asd2', 'asdafadsdAA1AAssss@yahoo.com', 'male', 'active')
                                ]
                             )
    def test_delete_user(self, name, email, gender, status):
        u1 = User(name, email, gender, status)
        assert u1.add()
        assert u1.delete()

    @pytest.mark.parametrize('user_id, title, body',
                                [
                                    (46, 'title', 'body')
                                ]
                            )
    def test_add_post(self, user_id, title, body):
        p1 = Post(user_id, title, body)
        assert p1.add()
        assert p1.get()

    @pytest.mark.parametrize('title, body',
                             [
                                 ('title', 'body')
                             ]
                             )
    def test_add_post_without_uid(self, title, body):
        p1 = Post(None, title, body)
        assert p1.add() == False

    @pytest.mark.parametrize('user_id, body',
                             [
                                 (46, 'body')
                             ]
                             )
    def test_add_post_without_title(self, user_id, body):
        p1 = Post(user_id, None, body)
        assert p1.add() == False

    @pytest.mark.parametrize('user_id, title, body',
                                [
                                    (46, 'title1', 'body1')
                                ]
                            )
    def test_delete_post(self, user_id, title, body):
        p1 = Post(user_id, title, body)
        assert p1.add()
        assert p1.delete()

    @pytest.mark.parametrize('user_id, title, due_on, status',
                                [
                                    (46, 'title1', '2021-12-15T00:00:00.000+04:30', 'pending')
                                ]
                            )
    def test_add_todo(self, user_id, title, due_on, status):
        t1 = Todo(user_id, title, due_on, status)
        assert t1.add()
        assert t1.get()

    @pytest.mark.parametrize('title, due_on, status',
                             [
                                 ('title1', '2021-12-15T00:00:00.000+04:30', 'pending')
                             ]
                             )
    def test_add_todo_without_uid(self, title, due_on, status):
        t1 = Todo(None, title, due_on, status)
        assert t1.add() == False

    @pytest.mark.parametrize('user_id, due_on, status',
                             [
                                 (46, '2021-12-15T00:00:00.000+04:30', 'pending')
                             ]
                             )
    def test_add_todo_without_title(self, user_id, due_on, status):
        t1 = Todo(user_id, None, due_on, status)
        assert t1.add() == False

    @pytest.mark.parametrize('user_id, title, due_on, status',
                            [
                                (46, 'title2', '2021-12-18T00:00:00.000+02:30', 'pending')
                            ]
                            )
    def test_delete_todo(self, user_id, title, due_on, status):
        t1 = Todo(user_id, title, due_on, status)
        assert t1.add()
        assert t1.delete()


    def test_toml1(self):
        TOML.toml_input(TOML.todos_file, t_users="random")
        assert len(Object.objects) == 3

    def test_toml1(self):
        TOML.toml_input(TOML.users_file)
        TOML.toml_input(TOML.posts_file, p_users="random")
        assert len(Object.objects) == 6

    def test_toml2(self):
        Object.objects.clear()
        TOML.toml_input(TOML.input_file)
        assert len(Object.objects) == 5








