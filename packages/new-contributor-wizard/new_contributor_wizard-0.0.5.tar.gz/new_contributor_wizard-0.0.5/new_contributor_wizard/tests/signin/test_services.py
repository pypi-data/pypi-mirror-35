import pytest

from new_contributor_wizard.modules.signin.services import sign_in_user
from new_contributor_wizard.modules.signin.exceptions import SignInError
from new_contributor_wizard.settings import (
    get_db_connection
)
from new_contributor_wizard.modules.signin.utils import (
    clean_email,
    hash_password
)


def setup():
    # inserting test values to the database
    connection = get_db_connection()
    db_cursor = connection.cursor()
    cleaned_email = clean_email('shanky@shanky.xyz')
    hashed_password = hash_password('mynewpass')
    db_cursor.execute('''
        INSERT INTO USERS (email, password) VALUES ('{}', '{}')
    '''.format(cleaned_email, hashed_password)
    )
    connection.commit()


def test_sign_in():
    # checking valid login
    email = 'shanky@shanky.xyz'
    password = 'mynewpass'
    user_info = sign_in_user(
        email=email,
        password=password
    )
    assert user_info

    # checking invalid login for no account
    email = 'shashankkumarkushwaha@gmail.com'
    password = 'mynewpass'
    with pytest.raises(SignInError):
        sign_in_user(
            email=email,
            password=password
        )

    # checking invalid login for incorrect password
    email = 'shanky@shanky.xyz'
    password = 'myoldpass'
    with pytest.raises(SignInError):
        sign_in_user(
            email=email,
            password=password
        )


def teardown():
    # deleting test values from the database
    connection = get_db_connection()
    db_cursor = connection.cursor()
    db_cursor.execute('''
        DELETE FROM USERS WHERE USERS.email='shanky@shanky.xyz'
    ''')
    connection.commit()
    connection.close()
