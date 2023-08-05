'''
Validation functions for encryption.tools module
'''
import re
from datetime import datetime as dt

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.utils import (
    clean_email, clean_name
)


def validate_name(name):
    '''
    Validating whether Full Name is provided by user and is in
    correct alphabet format
    '''
    cleaned_name = clean_name(name)
    if not cleaned_name:
        raise GPGError('Enter Full Name')
    for part_name in cleaned_name.split():
        if not part_name.isalpha():
            raise GPGError('Incorrect Format')
    return True


def validate_email(email):
    '''
    Validating Email provided to check for proper mail format and
    only alphabets
    '''
    cleaned_email = clean_email(email)
    if not re.match(r'[^@]+@[^@]+\.[^@]+', cleaned_email):
        raise GPGError('Incorrect Format')
    cleaned_email = cleaned_email.strip(' ').split('.')
    for parts in cleaned_email:
        parts = parts.split('@')
        if not all(part.isalpha() for part in parts):
            raise GPGError('Incorrect Format')
    return True


def validate_comment(comment):
    '''
    Validating comment provided by the user for any unnecessary symbols
    '''
    if not comment:
        raise GPGError('Enter Comment')
    return True


def validate_expire_date(date):
    '''
    Validating date for correct format from one of the following
    YYYY-MM-DD
    '''
    if not re.match(r'(\d){4}-(\d){2}-(\d){2}', date):
        raise GPGError('Invalid Format')
    try:
        datetime_object = dt.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise GPGError('Invalid Format')

    if datetime_object < dt.now():
        raise GPGError('Date should be of future')
    return True
