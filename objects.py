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
        self.id = None

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
            if 200 <= response.status_code < 300:
                print('Status OK\n')
                return response
            else:
                print('Status Failed\n')
                return False

        return wrapper

    @check_response
    def add(self, **item):
        """
        Method that adds an object
        Parameters differ for every class that inherits this class:
            Posts: user_id, title, body
            Users: name, email, gender, status
            Comments: post_id, name, email, body
            Todos: user_id, title, due_on, status
        """
        d = {key: value for key, value in item.items()}

        try:
            response = requests.post(
                self.url,
                json=d,
                headers=Object.my_headers
            )
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
        except:
            print('Something went wrong with creating the object')
        else:
            print(response.json())
            print(f'Status code: {response.status_code}')
            self.id = response.json()['data']['id']
            try:
                Object.objects.append(
                    {
                        'type': self,
                        'object': self.__class__.__name__,
                        'id': response.json()['data']['id']
                    }
                )
            except:
                print('Response may be empty')
        return response

    @check_response
    def get(self):
        """
        Method that retrieves an object or more objects
        """

        try:
            response = requests.get(f'{self.url}/{self.id}')
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
        except:
            print('Something went wrong with object fetching')

        else:
            print(response.json())
            print(f'GET status: {response.status_code}')
        return response

    @check_response
    def delete(self):
        """
        Method that deletes the current object
        """

        try:
            response = requests.delete(
                f'{self.url}/{self.id}',
                headers=Object.my_headers
            )
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
        except:
            print('Something went wrong with deleting the object')
        else:
            print(f'DELETE status: {response.status_code}')
        return response

    @classmethod
    def get_all(cls):
        for obj in Object.objects:
            if obj.get('object') == cls.__name__ or cls.__name__ == 'Object':
                obj.get('type').get()

    @classmethod
    def cleanup(cls):
        """
        Method that performs a cleanup for all created objects
        """
        nr = 0
        if cls.__name__ != 'Object':
            items = [obj for obj in Object.objects if obj.get('object') == cls.__name__]
        else:
            items = Object.objects
        print("Cleanup started")
        print(f'{len(items)} items to be deleted')
        for obj in items:
            print(f'Deleting item {items.index(obj) + 1}: id = {obj.get("id")}')
            try:
                time.sleep(1)
                response = obj.get('type').delete()
            except:
                print('Something went wrong with deleting the item')
            else:
                if response:
                    nr += 1

        if nr == len(items):
            print("Cleanup successful")
            print(f'{nr}/{len(items)} items deleted\n')
            return True
        else:
            print("Cleanup failed")
            print(f'{nr}/{len(items)} items deleted\n')
            return False
