'''
This class contains signin module specific exceptions
'''


class SignInError(Exception):
    '''
    SignInError class can be used to raise exception related to
    Sign In module
    '''

    def __init__(self, message):
        self.message = message
        super().__init__(message)
