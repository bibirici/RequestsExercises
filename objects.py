import requests

class Object:
    """
    Parent Class representing an object
    Attributes:
        objects: a list containing dictionaries: {type_of_object, object, id}
        acess_token: token used for authentication for post/delete calls
    """
    objects = []
    access_token = '08ff96950f7b2f2094fcaf9e15fcc3e70170677916fdf997ed25f57eb6f63d73'
    my_headers = {'Authorization': 'Bearer ' + access_token}
    base_url = "https://gorest.co.in/public/v1"

    def __init__(self):
        self.id = None


    def check_response(func):
        """
        Method that checks if response is valid. The method is a decorator
        for every REST method
        Parameters:
            func: function that is decorated
        """

        def wrapper(self, method, json_add=None):
            """
            wrapper method modifies the func function
            Parameters:
                method: request method
                json_add: data that is added for post request
            """
            response = func(self, method, json_add)
            print(f'Status code: {response.status_code}\n')
            if 200 <= response.status_code < 300:
                return response
            else:
                return False

        return wrapper

    def get_create_dictionary(self):
        """
        Method that creates the dictionary for each object
        """
        pass

    @check_response
    def request_method(self, method, json_add=None):
        id = 0
        if method == 'post':
            response = requests.post(
                self.url,
                json=json_add,
                headers=Object.my_headers
            )
        elif method == 'get':
            response = requests.get(f'{self.url}/{self.id}')
        elif method == 'delete':
            response = requests.delete(
                f'{self.url}/{self.id}',
                headers=Object.my_headers
            )
            id = self.id
            url = self.url
        try:
            response
        except requests.exceptions.ConnectionError as err:
            print("Connection Error: ", err)
        except requests.exceptions.HTTPError as err:
            print("HTTP Error: ", err)
        except requests.exceptions.Timeout as err:
            print("Timeout Error: ", err)
        except requests.exceptions.RequestException as err:
            print("An error occured: ", err)
        else:
            if method == 'get' or method == 'post':
                print(response.json())
            else:
                i = 0
                while i < len(Object.objects):
                    if Object.objects[i].get('id') == id and Object.objects[i].get('type').url == url:
                        del Object.objects[i]
                        break
                    else:
                        i += 1

        return response

    def add(self):
        """
        Method that adds an object
        """
        json_add = self.__class__.get_create_dictionary(self)

        response = Object.request_method(self, 'post', json_add)

        try:
            self.id = response.json()['data']['id']
            Object.objects.append(
                {
                    'type': self,
                    'object': self.__class__.__name__,
                    'id': response.json()['data']['id']
                }
            )
        except Exception as err:
            print(f"ID doesn't exist: {err}")

        return response

    def get(self):
        """
        Method that retrieves the current object
        """
        response = Object.request_method(self, 'get')
        return response

    def delete(self):
        """
        Method that deletes the current object
        """
        response = Object.request_method(self, 'delete')

        return response

    @classmethod
    def get_all(cls):
        """
        This method retrieves all created objects
        """
        for obj in Object.objects:
            if obj.get('object') == cls.__name__ or cls.__name__ == 'Object':
                obj.get('type').get()

    @classmethod
    def cleanup(cls):
        """
        Method that performs a cleanup for all created objects
        """
        nr = 0
        i = 0
        Object.objects.sort(key = lambda x: x.get('object'))
        print("\nCleanup started")
        print(f'{len(Object.objects)} items to be deleted')
        items = len(Object.objects)
        while len(Object.objects) > 0:
            print(f'Deleting item with id = {Object.objects[0].get("id")}')
            response = Object.objects[0].get('type').delete()
            i += 1
            if response:
                nr += 1

        if nr == items:
            print("Cleanup successful")
            print(f'{nr}/{items} items deleted\n')
            return True
        else:
            print("Cleanup failed")
            print(f'{nr}/{items} items deleted\n')
            return False

