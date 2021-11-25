import requests
import credentials
import cleanups
import check

class Comments:
    """ Class for comments' methods """

    @check.Check.check_response
    def add_comment(self, post_id, name, email, body):
        """
        Method that adds a comment
        Parameters:
            post_id: post's id of the comment
            name: user's name of the comment
            email: user's email of the comment
            body: comment's body
        """
        item = {'post_id': post_id, 'name': name, 'email': email, 'body': body}
        try:
            response = requests.post(credentials.Credentials.comments_url, json = item, headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with creating the object')

        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            try:
                cleanups.Cleanup.objects.append({'object': 'comments', 'id': response.json()['data']['id']})
            except:
                print('Response may be empty')
        return response.status_code

    @check.Check.check_response
    def get_comment(self, id=''):
        """
        Method that retrieves a comment or more comments
        Parameters:
            id(optional): comment's id, if not included, method will retrieve all users
        """

        try:
            response = requests.get(f'{credentials.Credentials.comments_url}/{id}')
        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')
        return response.status_code

    @check.Check.check_response
    def delete_comment(self, id):
        """
        Method that deletes a comment
        Parameters:
            id: comment's id
        """

        try:
            response = requests.delete(f'{credentials.Credentials.comments_url}/{id}', headers = credentials.Credentials.my_headers)

        except:
            print('Something went wrong with deleting the object')

        else:
            print(f'DELETE status: {response.status_code}')
        return response.status_code