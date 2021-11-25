import requests
import credentials
import cleanups
import check

class Todos:
    """ Class for todos' methods """

    @check.Check.check_response
    def add_todo(self, user_id, title, due_on, status):
        """
        Method that adds a comment
        Parameters:
            user_id: user's id of the todo
            title: todo title
            due_on: todo due_on date
            status: todo status(pending/completed)
        """

        item = {'user_id': user_id, 'title': title, 'due_on': due_on, 'status': status}
        try:
            response = requests.post(credentials.Credentials.todos_url, json = item, headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with creating the object')
        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            try:
                cleanups.Cleanup.objects.append({'object': 'users', 'id': response.json()['data']['id']})
            except:
                print('Response may be empty')
        return response.status_code

    @check.Check.check_response
    def get_todo(self, id=''):
        """
        Method that retrieves a todo or more todos
        Parameters:
            id(optional): todo's id, if not included, method will retrieve all todos
        """

        try:
            response = requests.get(f'{credentials.Credentials.todos_url}/{id}')
        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')

        return response.status_code

    @check.Check.check_response
    def delete_todo(self, id):
        """
        Method that deletes a todo
        Parameters:
            id: todo's id
        """

        try:
            response = requests.delete(f'{credentials.Credentials.todos_url}/{id}', headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with deleting the object')
        else:
            print(f'DELETE status: {response.status_code}')
        return response.status_code
