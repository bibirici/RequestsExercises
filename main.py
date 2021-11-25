import users
import posts
import comments
import todos
import cleanups
import unittest

class UserTesting(unittest.TestCase):

    def test_get_user(self):
        u = users.Users()
        assert u.get_user()

    def test_add_user(self):
        u = users.Users()
        assert u.add_user('asdfag', 'asdfas8172@yahoo.com', 'male', 'active')

    def test_delete_user(self):
        u = users.Users()
        assert u.delete_user(42)

class PostTesting(unittest.TestCase):

    def test_get_post(self):
        p = posts.Posts()
        assert p.get_post()

    def test_add_post(self):
        p = posts.Posts()
        assert p.add_post(46, 'asd1', 'asd1')

    def test_delete_post(self):
        p = posts.Posts()
        assert p.delete_post(22)

class CommentTesting(unittest.TestCase):

    def test_get_comment(self):
        c = comments.Comments()
        assert c.get_comment()

    def test_add_comment(self):
        c = comments.Comments()
        assert c.add_comment(3, 'asd123', 'asd123@yahoo.com', 'body')

    def test_delete_comment(self):
        c = comments.Comments()
        assert c.delete_comment(39)

class TodoTesting(unittest.TestCase):
    def test_get_todo(self):
        t = todos.Todos()
        assert t.get_todo()

    def test_add_todo(self):
        t = todos.Todos()
        assert t.add_todo(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')

    def test_delete_todo(self):
        t = todos.Todos()
        assert t.delete_todo(26)

class CleanupTesting(unittest.TestCase):

    def test_cleanup(self):
        cl = cleanups.Cleanup()
        t = todos.Todos()
        t.add_todo(17, 'title', '2021-12-15T00:00:00.000+05:30', 'pending')
        t.add_todo(17, 'title', '2021-11-15T00:00:00.000+05:30', 'completed')
        cl.cleanup()

if __name__ == '__main__':
    unittest.main()