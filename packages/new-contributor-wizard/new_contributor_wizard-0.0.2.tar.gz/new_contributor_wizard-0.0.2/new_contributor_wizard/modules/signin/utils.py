'''
This module contains utility functions
'''
import hashlib


def clean_email(user_email):
    '''
    clean_email removes unnecessary spaces from Full Name
    '''
    return user_email.strip('\t\n\r ')


def hash_password(password):
    '''
    hash_password converts plain text password into sha256 hash
    '''
    return hashlib.sha256(password.encode()).hexdigest()
