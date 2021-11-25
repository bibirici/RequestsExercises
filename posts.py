import requests
import credentials
import cleanups
import check

class Posts:
    """ Class for posts' methods """

    @check.Check.check_response
    def add_post(self, user_id, title, body):
        """
        Method that adds a post
        Parameters:
            user_id: user's id of this post
            title: post's title
            body: post's body
        """

        item = {'user_id': user_id, 'title': title, 'body': body}
        try:
            response = requests.post(credentials.Credentials.posts_url, json = item, headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with creating the object')
        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            try:
                cleanups.Cleanup.objects.append({'object': 'posts', 'id': response.json()['data']['id']})
            except:
                print('Response may be empty')
        return response.status_code

    @check.Check.check_response
    def get_post(self, id=''):
        """
        Method that retrieves a post or more posts
        Parameters:
            id(optional): post's id, if not included, method will retrieve all posts
        """
        try:
            response = requests.get(f'{credentials.Credentials.posts_url}/{id}')

        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')
        return response.status_code

    @check.Check.check_response
    def delete_post(self, id):
        """
        Method that deletes a post
        Parameters:
            id: post's id
        """

        try:
            response = requests.delete(f'{credentials.Credentials.posts_url}/{id}', headers = credentials.Credentials.my_headers)

        except:
            print('Something went wrong with deleting the object')

        else:
            print(f'DELETE status: {response.status_code}')
        return response.status_code
