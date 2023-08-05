'''
This module contains services to be utilized by the application
'''
import sqlite3

from new_contributor_wizard.settings import get_db_connection, USER_INFOMATION_TABLE
from new_contributor_wizard.modules.signup.exceptions import SignUpError
from new_contributor_wizard.modules.signup.utils import (
    generate_uuid, clean_email, clean_full_name, hash_password, clean_timezone
)


def sign_up_user(email, password, full_name, language, timezone):
    '''
    sign_up_user creates connection with the sqlite3 database,
    calls methods to clean up full_name, convert password into
    hash and query database to save user's information.
    Would result in a False statement if the Email is already
    present.
    '''
    connection = get_db_connection()
    db_cursor = connection.cursor()

    user_info = {
        'table_name': USER_INFOMATION_TABLE,
        'user_id': generate_uuid(),
        'email': clean_email(email),
        'password': hash_password(password),
        'full_name': clean_full_name(full_name),
        'language': language,
        'timezone': clean_timezone(timezone),
    }

    try:
        sign_up_query = '''
            INSERT INTO {table_name} VALUES
             ('{user_id}',
              '{email}',
              '{password}',
              '{full_name}',
              '{language}',
              '{timezone}')
         '''.format(**user_info)
        db_cursor.execute(sign_up_query)
        connection.commit()
    except sqlite3.IntegrityError:
        raise SignUpError('Email already exists')
    return True
