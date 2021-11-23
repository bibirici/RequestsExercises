import requests
import objects

class APIrequests:
    responses = [] #contains operation statuses
    operations = [] #contains id of object and type of object of all succeeded operations
    def __init__(self, URL, token):
        self._URL = URL
        self._token = token

    def getObject(self, obj, id=''):
            try:
                api_url = f'{self._URL}{obj}/{id}'
                response = requests.get(api_url)
                APIrequests.responses.append(response.status_code)

            except:
                print('Something went wrong with object fetching')

            else:
                print(response.json())
                print(f'GET status: {response.status_code}')
                APIrequests.checkResponse(self, response.status_code)

    def deleteObject(self, obj, id):
        try:
            api_url = f"{self._URL}{obj}/{id}?access-token={self._token}"
            response = requests.delete(api_url)
            APIrequests.responses.append(response.status_code)

        except:
            print('Something went wrong with deleting the object')

        else:
            print(f'DELETE status: {response.status_code}')
            APIrequests.checkResponse(self, response.status_code)


    def postObject(self, obj, values):
        try:
            k = objects.APIobjects.objects[obj]
            d = dict.fromkeys(k)
            for i in range(len(k)):
                d[k[i]] = values[i]
            api_url = f"{self._URL}{obj}?access-token={self._token}"
            response = requests.post(api_url, json=d)
            APIrequests.responses.append(response.status_code)

        except:
            print('Something went wrong with creating the object')

        else:
            print(response.json())
            print(f'POST status: {response.status_code}')
            if APIrequests.checkResponse(self, response.status_code):
                APIrequests.operations.append({'object': obj, 'id': response.json()['data']['id']})


    def checkResponse(self, response):
        if response >= 200 and response < 300:
            print('Status OK\n')
            return True
        else:
            print('Status Failed\n')
            return False

    def cleanup(self, objects): #objects is a list containing length 2 lists: [type of object, id]
        nr = 0
        print("Cleanup started")
        print(f'{len(objects)} items to be deleted')
        try:
            for obj in objects:
                api_url = f"{self._URL}{obj['object']}/{obj['id']}?access-token={self._token}"
                response = requests.delete(api_url)
                print(f'Deleting item {objects.index(obj)+1}')
                if APIrequests.checkResponse(self, response.status_code):
                    nr += 1

        except:
            print('Something went wrong with cleanup')

        if nr == len(objects): #if all items have been deleted
            print("Cleanup successful")
            print(f'{nr}/{len(objects)} items deleted')
        else:
            print("Cleanup failed")
            print(f'{nr}/{len(objects)} items deleted')