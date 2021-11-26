import users
import posts
import comments
import todos
import unittest
import objects

class UserTesting(unittest.TestCase):

    def test_get_user(self):
        u = users.Users()
        assert u.get()

    def test_add_user(self):
        u = users.Users()
        assert u.add('asdfag', 'asdfas8172@yahoo.com', 'male', 'active')

    def test_delete_user(self):
        u = users.Users()
        assert u.delete(42)

class PostTesting(unittest.TestCase):

    def test_get_post(self):
        p = posts.Posts()
        assert p.get()

    def test_add_post(self):
        p = posts.Posts()
        assert p.add(49, 'asd1', 'asd1')

    def test_delete_post(self):
        p = posts.Posts()
        assert p.delete(12)

class CommentTesting(unittest.TestCase):

    def test_get_comment(self):
        c = comments.Comments()
        assert c.get()

    def test_add_comment(self):
        c = comments.Comments()
        assert c.add(3, 'asd123', 'asd123@yahoo.com', 'body')

    def test_delete_comment(self):
        c = comments.Comments()
        assert c.delete(39)

class TodoTesting(unittest.TestCase):
    def test_get_todo(self):
        t = todos.Todos()
        assert t.get()

    def test_add_todo(self):
        t = todos.Todos()
        assert t.add(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')

    def test_delete_todo(self):
        t = todos.Todos()
        assert t.delete(26)

class CleanupTesting(unittest.TestCase):

    def test_cleanup(self):
        u = users.Users()
        u.add('asdfag', 'asdfas12833@yahoo.com', 'male', 'active')
        t = todos.Todos()
        t.add(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')
        c = comments.Comments()
        c.add(60, 'asd123', 'asd123@yahoo.com', 'body')
        p = posts.Posts()
        p.add(60, 'asd1', 'asd1')
        objects.Object.cleanup()

if __name__ == '__main__':
    unittest.main()