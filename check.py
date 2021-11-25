
class Check:

    """ Method that performs a check for all REST calls """
    @staticmethod
    def check_response(func):
        def wrapper(self, *args):
            response = func(self, *args)
            if response >= 200 and response < 300:
                print('Status OK\n')
                return True
            else:
                print('Status Failed\n')
                return False
        return wrapper
