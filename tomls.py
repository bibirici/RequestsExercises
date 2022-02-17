import toml
import random
from users import User
from posts import Post
from todos import Todo
from comments import Comment
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
            u1 = User(user.get('name'), user.get('email'), user.get('gender'), user.get('status'))
            added_user = u1.add()
            try:
                user_id = added_user.json()['data']['id']
                todos = user.get('todos',{})
                TOML.create_todos(todos, user_id)
                posts = user.get('posts',{})
                TOML.create_posts(posts, user_id)
            except Exception as err:
                print(f"Can't get id of user: {err}")


    @staticmethod
    def create_posts(posts, uid = None):
        """
        Method that creates posts from a TOML file
        Parameters:
              posts: a TOML file with one or more posts
              uid(optional): id of an created user
              Possible values for uid:
                if uid is not provided, uid is obtained from TOML file,
                uid can be 'random' for a random user
        """
        for post in posts.values():
            if uid == 'random':
                user_id = TOML.get_random_user()
            else:
                user_id = post.get('user_id', uid)
            p1 = Post(user_id, post.get('title'), post.get('body'))
            p1.add()

    @staticmethod
    def create_todos(todos, uid = None):
        """
        Method that creates todos from a TOML file
        Parameters:
              todos: a TOML file with one or more todos
              uid(optional): id of an created user
              Possible values for uid:
                if uid is not provided, uid is obtained from TOML file,
                uid can be 'random' for a random user
        """
        for todo in todos.values():
            if uid == 'random':
                user_id = TOML.get_random_user()
            else:
                user_id = todo.get('user_id', uid)
            t1 = Todo(user_id, todo.get('title'), todo.get('due_on'), todo.get('status'))
            t1.add()

    @staticmethod
    def create_comments(comments):
        """
        Method that creates comments from a TOML file
        Parameters:
              comments: a TOML file with one or more comments
        """
        for comment in comments.values():
            c1 = Comment(comment.get('post_id'), comment.get('name'), comment.get('email'), comment.get('body'))
            c1.add()

    @staticmethod
    def get_random_user():
        """
        Method that returns an id of a random user
        """
        users = [user.get('id') for user in Object.objects if user.get('object') == 'User']
        try:
            user_id = random.choice(users)
        except Exception as err:
            print(err)
        else:
            return user_id


    @staticmethod
    def toml_input(path, t_users = None, p_users = None):
        """
        Method that parses an TOML file and create all the objects in that file
        Parameters:
            path: path to the TOML file
        """
        text = toml.load(path)
        users = text.get('users', {})
        posts = text.get('posts', {})
        todos = text.get('todos', {})
        comments = text.get('comments', {})
        TOML.create_users(users)
        TOML.create_posts(posts, p_users)
        TOML.create_todos(todos, t_users)
        TOML.create_comments(comments)











