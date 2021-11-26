import requests

class Object:
    """
    Parent Class representing an object
    Attributes:
        objects: a list containing dictionaries: {type_of_object, object, id}
        acess_token: token used for authentication for post/delete calls
    """
    objects = []
    access_token = '58409336e33cd2a7e8f6858c3db7f26b7a2117bcaf56edcdc767c1cf130d9f47'
    my_headers = {'Authorization': 'Bearer ' + access_token}

    def check_response(func):
        """
        Method that checks if response is valid. The method is a decorator
        for every REST method
        Parameters:
            func: function that is decorated
        """
        def wrapper(self, *args):
            """
            wrapper method modifies the func function
            Parameters:
                *args: func arguments
            """
            response = func(self, *args)
            if response >= 200 and response < 300:
                print('Status OK\n')
                return True
            else:
                print('Status Failed\n')
                return False
        return wrapper


    @check_response
    def add(self, *item):
        """
        Method that adds an object
        Parameters differ for every type of object:
            Posts: user_id, title, body
            Users: name, email, gender, status
            Comments: post_id, name, email, body
            Todos: user_id, title, due_on, status
        """
        values = [el for el in item]
        d = {self.keys[i] : values[i] for i in range(len(self.keys))}
        try:
            response = requests.post(self.url, json=d, headers=Object.my_headers)
        except:
            print('Something went wrong with creating the object')
        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            try:
                Object.objects.append({'type':self, 'object': self.__class__.__name__, 'id': response.json()['data']['id']})
            except:
                print('Response may be empty')
        return response.status_code

    @check_response
    def get(self, id=''):
        """
        Method that retrieves an object or more objects
        Parameters:
            id(optional): object's id, if not included, method will retrieve all objects
        """

        try:
            response = requests.get(f'{self.url}/{id}')
        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')
        return response.status_code

    @check_response
    def delete(self, id):
        """
        Method that deletes an object
        Parameters:
            id: user's id
        """

        try:
            response = requests.delete(f'{self.url}/{id}', headers=Object.my_headers)
        except:
            print('Something went wrong with deleting the object')
        else:
            print(f'DELETE status: {response.status_code}')
        return response.status_code

    @staticmethod
    def cleanup():
        """
        Method that performs a cleanup for all created objects
        """
        nr = 0
        print("Cleanup started")
        print(f'{len(Object.objects)} items to be deleted')
        for obj in Object.objects:
            url = f'{obj.get("type").url}/{obj.get("id")}'
            try:
                response = requests.delete(url, headers=Object.my_headers)
            except:
                print('Something went wrong with deleting the item')
            else:
                print(f'Deleting item {Object.objects.index(obj) + 1}')
                nr += 1
        print (Object.objects)
        if nr == len(Object.objects):
            print("Cleanup successful")
            print(f'{nr}/{len(Object.objects)} items deleted\n')
            return True
        else:
            print("Cleanup failed")
            print(f'{nr}/{len(Object.objects)} items deleted\n')
            return False
