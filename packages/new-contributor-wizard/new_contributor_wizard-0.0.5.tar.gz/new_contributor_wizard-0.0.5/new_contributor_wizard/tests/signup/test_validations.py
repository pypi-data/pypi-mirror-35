import pytest

from new_contributor_wizard.modules.signup.exceptions import SignUpError
from new_contributor_wizard.modules.signup.validations import (
    validate_email,
    validate_first_pass,
    validate_confirm_pass,
    validate_full_name,
    validate_timezone
)


def test_validate_email():
    # Validate strip of whitespaces, newlines and tabs
    assert validate_email('abc@shanky.xyz')
    assert validate_email(' abc@shanky.xyz')
    assert validate_email('abc@shanky.xyz ')
    assert validate_email(' abc@shanky.xyz ')

    # check for correct email format
    with pytest.raises(SignUpError):
        validate_email('abcshanky.xyz')
    with pytest.raises(SignUpError):
        validate_email('abc@!shanky.xyz')

    # check for emply email address
    with pytest.raises(SignUpError):
        validate_email('')
    with pytest.raises(SignUpError):
        validate_email(' ')


def test_validate_first_pass():
    # check for valid pass
    assert validate_first_pass('mynewpass')

    # check for empty pass
    with pytest.raises(SignUpError):
        validate_first_pass('')


def test_validate_confirm_pass():
    # check for correct match
    assert validate_confirm_pass('mynewpass', 'mynewpass')

    # check for incorrect match
    with pytest.raises(SignUpError):
        validate_confirm_pass('mynewpass', 'mypass')


def test_validate_full_name():
    # check for correct name format
    assert validate_full_name('Shashank Kumar')

    # check for empty name input
    with pytest.raises(SignUpError):
        validate_full_name('')

    # check for invalid name format
    with pytest.raises(SignUpError):
        validate_full_name('Sanyam ! Khurana')


def test_validate_timezone():
    # check for correct timezone
    assert validate_timezone('UTC+05:30')

    # check for empty timezone
    with pytest.raises(SignUpError):
        validate_timezone('')

    # check for incorrect timezone
    with pytest.raises(SignUpError):
        validate_timezone('utc+')
