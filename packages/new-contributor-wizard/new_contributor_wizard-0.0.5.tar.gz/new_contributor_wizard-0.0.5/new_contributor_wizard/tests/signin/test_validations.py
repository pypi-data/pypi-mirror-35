import pytest

from new_contributor_wizard.modules.signin.exceptions import SignInError
from new_contributor_wizard.modules.signin.validations import (
    validate_email,
    validate_password
)


def test_validate_email():
    # validating stip operation and correct email format
    assert validate_email('abc@shanky.xyz')
    assert validate_email(' abc@shanky.xyz')
    assert validate_email('abc@shanky.xyz ')
    assert validate_email(' abc@shanky.xyz ')

    # validating incorrect email format
    with pytest.raises(SignInError):
        assert not validate_email('abcshanky.xyz')
    with pytest.raises(SignInError):
        assert not validate_email('abc@!shanky.xyz')

    # validating empty email input
    with pytest.raises(SignInError):
        assert not validate_email('')
    with pytest.raises(SignInError):
        assert not validate_email(' ')


def test_validate_password():
    # validating correct email format
    assert validate_password('mynewpass')

    # validating empty password input
    with pytest.raises(SignInError):
        assert not validate_password('')
