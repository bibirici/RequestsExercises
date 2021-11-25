
class Credentials:
    """
    The class for credentials and URLs
    Attributes:
        users_url = the URL used for users' REST calls
        posts_url = the URL used for posts' REST calls
        comments_url = the URL used for comments' REST calls
        todos_url = the URL used for todos' REST calls
        access_token = token used for authorization (post/delete operations)
        my_headers = header used for requests calls
    """

    base_url = "https://gorest.co.in/public/v1/"
    users_url = base_url + 'users'
    posts_url = base_url + 'posts'
    comments_url = base_url + 'comments'
    todos_url = base_url + 'todos'
    access_token = '58409336e33cd2a7e8f6858c3db7f26b7a2117bcaf56edcdc767c1cf130d9f47'
    my_headers = {'Authorization': 'Bearer ' + access_token}