'''
This modules contain classes to query sqlite3 database
'''
from new_contributor_wizard.settings import get_db_connection, USER_INFOMATION_TABLE
from new_contributor_wizard.modules.signin.exceptions import SignInError
from new_contributor_wizard.modules.signin.utils import (
    clean_email, hash_password
)


def sign_in_user(email, password):
    '''
    sign_in_user would try to check for user's email and hashed
    password in the database
    Would result in a UserError if email doesn't exist
    Would result in a PasswordError if password doesn't match
    '''
    connection = get_db_connection()
    db_cursor = connection.cursor()

    cleaned_email = clean_email(email)
    hashed_pass = hash_password(password)

    sign_in_query = 'SELECT * FROM {} WHERE email=?'.format(USER_INFOMATION_TABLE)
    user_info = db_cursor.execute(sign_in_query, (cleaned_email, )).fetchone()

    if not user_info:
        raise SignInError('Email does not exist!')

    elif user_info[2] != hashed_pass:
        raise SignInError('Password is incorrect!')

    return user_info
