'''
This module contains Validation functions
'''
import re

from new_contributor_wizard.modules.signin.utils import clean_email
from new_contributor_wizard.modules.signin.exceptions import SignInError


def validate_email(user_email):
    '''
    Validating Email provided to check for proper mail format and
    only alphabets
    '''
    user_email = clean_email(user_email)
    if not re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
        raise SignInError('Incorrect Format')
    user_email = user_email.strip(' ').split('.')
    for parts in user_email:
        parts = parts.split('@')
        if not all(part.isalpha() for part in parts):
            raise SignInError('Incorrect Format')
    return True


def validate_password(password):
    '''
    Validating whether or not the password is submitted by
    the user
    '''
    if not password:
        raise SignInError('Enter password')
    return True
