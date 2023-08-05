'''
This module contains utility functions
'''
import hashlib
from uuid import uuid4


def generate_uuid():
    '''
    generate_uuid return a universally unique identifier string
    '''
    return str(uuid4())


def clean_email(user_email):
    '''
    clean_email removes unnecessary spaces from Full Name
    '''
    return user_email.strip('\t\n\r ')


def clean_full_name(full_name):
    '''
    clean_full_name removes unnecessary spaces from Full Name
    '''
    full_name = ' '.join(full_name.split())
    return full_name.strip('\t\n\r ')


def hash_password(password):
    '''
    hash_password converts plain text password into sha256 hash
    '''
    return hashlib.sha256(password.encode()).hexdigest()


def clean_timezone(timezone):
    '''
    clean_timezone removes unnessary spaces from the timezone and return a
    lowercase timezone text
    '''
    return timezone.lower().strip(' ')
