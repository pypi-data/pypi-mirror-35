'''
Exceptions module contains exception classes specific to signup module
'''


class SignUpError(Exception):
    '''
    SignUpError class can be used to raise exception related to
    User's imput
    '''

    def __init__(self, message):
        self.message = message
        super().__init__(message)
