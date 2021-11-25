import requests
import credentials

class Cleanup:
    objects = []
    """
    Method that performs a cleanup for all created objects
    Parameters:
        operations: a list containing dictionaries: {object, id_of_object}
    """
    def cleanup(self):
        nr = 0
        print("Cleanup started")
        print(f'{len(Cleanup.objects)} items to be deleted')
        for obj in Cleanup.objects:
            try:
                response = requests.delete(f'{credentials.Credentials.base_url}/{obj.get("object")}/{id}',
                                           headers=credentials.Credentials.my_headers)
            except:
                print('Something went wrong with deleting the item')
            else:
                print(f'Deleting item {Cleanup.objects.index(obj) + 1}')
                nr += 1

        if nr == len(Cleanup.objects):
            print("Cleanup successful")
            print(f'{nr}/{len(Cleanup.objects)} items deleted')
            return True
        else:
            print("Cleanup failed")
            print(f'{nr}/{len(Cleanup.objects)} items deleted')
            return False
