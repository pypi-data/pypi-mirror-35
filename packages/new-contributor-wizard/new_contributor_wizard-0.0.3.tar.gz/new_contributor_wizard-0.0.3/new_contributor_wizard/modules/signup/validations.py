'''
This module contains Validation functions
'''
import re

from new_contributor_wizard.modules.signup.exceptions import SignUpError
from new_contributor_wizard.modules.signup.utils import (
    clean_email, clean_full_name, clean_timezone
)


def validate_email(user_email):
    '''
    Validating Email provided to check for proper mail format and
    only alphabets
    '''
    user_email = clean_email(user_email)
    if not re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
        raise SignUpError('Incorrect Format')
    user_email = user_email.strip(' ').split('.')
    for parts in user_email:
        parts = parts.split('@')
        if not all(part.isalpha() for part in parts):
            raise SignUpError('Incorrect Format')
    return True


def validate_first_pass(first_pass):
    '''
    Validating whether or not the first password is submitted by
    the user
    '''
    if not first_pass:
        raise SignUpError('Enter password')
    elif len(first_pass) < 6:
        raise SignUpError('Password is short')
    return True


def validate_confirm_pass(first_pass, confirm_pass):
    '''
    Validating whether both the password submitted by the user
    match each other
    '''
    if first_pass != confirm_pass:
        raise SignUpError('Password is not same')
    return True


def validate_full_name(full_name):
    '''
    Validating whether Full Name is provided by user and is in
    correct alphabet format
    '''
    full_name = clean_full_name(full_name)
    if not full_name:
        raise SignUpError('Enter Full Name')
    for name in full_name.split():
        if not name.isalpha():
            raise SignUpError('Incorrect Format')
    return True


def validate_timezone(timezone):
    '''
    Validating timezone to be in format `UTC+00:00`
    '''
    timezone = clean_timezone(timezone)
    if not timezone:
        raise SignUpError('Enter Timezone')
    else:
        if not re.match(r'utc[+-]\d{2}:\d{2}', timezone):
            raise SignUpError('Invalid Format')
    return True
