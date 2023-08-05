import pytest
import sqlite3

from new_contributor_wizard.modules.signup.services import sign_up_user
from new_contributor_wizard.modules.signup.exceptions import SignUpError
from new_contributor_wizard.settings import (
    DATABASE_FILE,
    USER_INFOMATION_TABLE,
    get_db_connection
)


def setup():
    get_db_connection()


def testing_setting_constants():
    # testing application constants
    assert DATABASE_FILE
    assert USER_INFOMATION_TABLE


def test_signup_operation():
    # test values
    user_info = {
        'email': 'abc@shanky.xyz',
        'password': 'mynewpass',
        'full_name': 'Shashank Kumar',
        'language': 'English',
        'timezone': 'UTC+5:30',
    }

    # testing valid signup
    assert sign_up_user(**user_info)

    # testing invalid signup
    with pytest.raises(SignUpError):
        sign_up_user(**user_info)


def teardown():
    # deleting test values
    connection = sqlite3.connect(DATABASE_FILE)
    db_cursor = connection.cursor()
    db_cursor.execute('''
        DELETE FROM USERS WHERE USERS.email='abc@shanky.xyz'
    ''')
    connection.commit()
    connection.close()
