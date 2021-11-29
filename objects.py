import requests
import time

class Object:
    """
    Parent Class representing an object
    Attributes:
        objects: a list containing dictionaries: {type_of_object, object, id}
        acess_token: token used for authentication for post/delete calls
    """
    objects = []
    access_token = 'f226d8100875a550ed64ddcb80bc1a30f799b7d5621ccc6febf7ff3bc9936965'
    my_headers = {'Authorization': 'Bearer ' + access_token}

    def __init__(self):
        self.url = "https://gorest.co.in/public"

    def check_response(func):
        """
        Method that checks if response is valid. The method is a decorator
        for every REST method
        Parameters:
            func: function that is decorated
        """
        def wrapper(self, **args):
            """
            wrapper method modifies the func function
            Parameters:
                **args: func arguments
            """
            response = func(self, **args)
            if response >= 200 and response < 300:
                print('Status OK\n')
                return True
            else:
                print('Status Failed\n')
                return False
        return wrapper


    @check_response
    def add(self, **item):
        """
        Method that adds an object
        Parameters differ for every type of object:
            Posts: user_id, title, body
            Users: name, email, gender, status
            Comments: post_id, name, email, body
            Todos: user_id, title, due_on, status
        """
        d = {key:value for key, value in item.items()}

        try:
            response = requests.post(self.url, json=d, headers=Object.my_headers)
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
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
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
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
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
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
                response = obj.get("type").delete(obj.get("id"))
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
