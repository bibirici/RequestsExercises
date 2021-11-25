import requests
import credentials
import cleanups
import check


class Users:
    """ Class for users' methods """

    @check.Check.check_response
    def add_user(self, name, email, gender, status):
        """
        Method that adds a user
        Parameters:
            name: user's name
            email: user's email
            gender: user's gender(male/female)
            status: user's status(inactive/active)
        """

        item = {'name': name, 'email': email, 'gender': gender, 'status': status}
        try:
            response = requests.post(credentials.Credentials.users_url, json = item, headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with creating the object')
        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            try:
                cleanups.Cleanup.cleanups.append({'object': 'users', 'id': response.json()['data']['id']})
            except:
                print('Response may be empty')
        return response.status_code

    @check.Check.check_response
    def get_user(self, id=''):
        """
        Method that retrieves an user or more users
        Parameters:
            id(optional): user's id, if not included, method will retrieve all users
        """

        try:
            response = requests.get(f'{credentials.Credentials.users_url}/{id}')
        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')
        return response.status_code

    @check.Check.check_response
    def delete_user(self, id):
        """
        Method that deletes an user
        Parameters:
            id: user's id
        """

        try:
            response = requests.delete(f'{credentials.Credentials.users_url}/{id}', headers = credentials.Credentials.my_headers)
        except:
            print('Something went wrong with deleting the object')
        else:
            print(f'DELETE status: {response.status_code}')
        return response.status_code
