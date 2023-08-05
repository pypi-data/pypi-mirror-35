'''
Exceptions module contains exception classes specific to encryption.tools module
'''


class GPGError(Exception):
    '''
    GPGError class can be used to raise exception related to
    User's imput
    '''

    def __init__(self, message):
        self.message = message
        super().__init__(message)
