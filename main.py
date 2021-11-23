import requests
import objects
import Requests

a1 = Requests.APIrequests("https://gorest.co.in/public/v1/", '3d987e4a7c44200d76deca198fbef4b2b269c3b052afb6489591a6af7ecc6bb1')
values_users = ['abcde', 'abcde@yahoo.com', 'male', 'active']
values_posts = [14, 'asd1', 'asd1']
values_comments = [14, 'asd123', 'asd123@yahoo.com', 'body']
values_todos = [14, 'title', '2021-12-15T00:00:00.000+05:30', 'pending']
a1.getObject("users", 2504)
a1.getObject("posts")
a1.getObject("comments")
a1.getObject("todos")
a1.deleteObject('users', 2)
a1.deleteObject('posts', 2)
a1.deleteObject('comments', 2)
a1.deleteObject('todos', 2)
a1.postObject('users', values_users)
a1.postObject('posts', values_posts)
a1.postObject('comments', values_comments)
a1.postObject('todos', values_todos)
print(Requests.APIrequests.responses)
print(Requests.APIrequests.operations)
a1.cleanup(Requests.APIrequests.operations)

