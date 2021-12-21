import pytest
import datetime
from objects import Object
from users import User
from posts import Post
from comments import Comment
from todos import Todo
from tomls import TOML

@pytest.fixture
def cleanup_method():
    end_time = datetime.datetime.now()
    yield end_time
    Object.cleanup()

@pytest.fixture
def time_difference():
    current_time = datetime.datetime.now()
    yield current_time
    finish_time = datetime.datetime.now()
    diff = finish_time - current_time
    print(f' Test execution time: {diff}')


class TestAddObjects():
    @pytest.mark.parametrize('name, email, gender, status',
                                [
                                    ('asd2', 'asdaTEST123JkOsp22s1@yahoo.com', 'male', 'active')
                                ]
                             )
    def test_add_new_user(self, name, email, gender, status, time_difference):
        u1 = User(name, email, gender, status)
        assert u1.add()
        assert u1.get().json().get('data')['name'] == name
        assert u1.get().json().get('data')['email'] == email
        assert u1.get().json().get('data')['gender'] == gender
        assert u1.get().json().get('data')['status'] == status
        assert u1.delete()
        assert not u1.get()

    @pytest.mark.parametrize('user_id, title, body',
                                [
                                    (1020, 'title', 'body')
                                ]
                            )
    def test_add_post(self, user_id, title, body, time_difference):
        p1 = Post(user_id, title, body)
        assert p1.add()
        assert p1.get().json().get('data')['user_id'] == user_id
        assert p1.get().json().get('data')['title'] == title
        assert p1.get().json().get('data')['body'] == body
        assert p1.delete()
        assert not p1.get()


    @pytest.mark.parametrize('user_id, title, due_on, status',
                                [
                                    (1020, 'title1asd', '2021-07-07T00:00:00.000+01:30', 'pending')
                                ]
                            )
    def test_add_todo(self, user_id, title, due_on, status, time_difference):
        t1 = Todo(user_id, title, due_on, status)
        assert t1.add()
        assert t1.get().json().get('data')['user_id'] == user_id
        assert t1.get().json().get('data')['title'] == title
        assert t1.get().json().get('data')['status'] == status
        assert t1.delete()
        assert not t1.get()


    @pytest.mark.parametrize('post_id, name, email, body',
                                [
                                    (1071, 'testname', 'testname@yahoo.com', 'testbody')
                                ]
                            )
    def test_add_comment(self, post_id, name, email, body, cleanup_method, time_difference):
        c1 = Comment(post_id, name, email, body)
        assert c1.add()
        assert c1.get().json().get('data')['post_id'] == post_id
        assert c1.get().json().get('data')['name'] == name
        assert c1.get().json().get('data')['email'] == email
        assert c1.get().json().get('data')['body'] == body
        assert c1.delete()
        assert not c1.get()


class TestUser():

    @pytest.mark.parametrize('users', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/users.toml"])
    def test_toml_users(self, users, cleanup_method, time_difference):
        TOML.toml_input(users)
        assert len(Object.objects) == 1

class TestTodo():
    @pytest.mark.parametrize('todos', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/todos.toml"])
    def test_toml_todos(self, todos, cleanup_method, time_difference):
        TOML.toml_input(todos)
        assert len(Object.objects) == 2

class TestPost():
    @pytest.mark.parametrize('posts', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/posts.toml"])
    def test_toml_posts(self, posts, cleanup_method, time_difference):
        TOML.toml_input(posts)
        assert len(Object.objects) == 1

class TestComment():
    @pytest.mark.parametrize('comments', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/comments.toml"])
    def test_toml_posts(self, comments, cleanup_method, time_difference):
        TOML.toml_input(comments)
        assert len(Object.objects) == 1

class TestUsersObjects():
    @pytest.mark.parametrize('users_objects', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/input_file.toml"])
    def test_toml_users_objects(self, users_objects, cleanup_method, time_difference):
        TOML.toml_input(users_objects)
        assert len(Object.objects) == 5


# class TestPerformance():
#     @pytest.mark.parametrize('objects', ["C:/Users/ABibirici/PycharmProjects/APIrequests/TOML/objects.toml"])
#     def test_toml_posts(self, objects, cleanup_method):
#         for i in range(300):
#             TOML.toml_input(objects)
#         assert len(Object.objects) == 900





