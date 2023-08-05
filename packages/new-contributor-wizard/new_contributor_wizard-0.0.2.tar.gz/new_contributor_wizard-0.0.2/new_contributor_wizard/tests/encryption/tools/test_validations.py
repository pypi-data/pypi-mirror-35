import datetime

import pytest

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.validations import (
    validate_name, validate_email, validate_comment, validate_expire_date
)


def test_validate_name():
    # testing for correct name format
    assert validate_name('Shashank Kumar')

    # testing for incorrect name format
    with pytest.raises(GPGError):
        validate_name('')
    with pytest.raises(GPGError):
        validate_name('!S12ank')


def test_validate_email():
    # testing for correct email format
    assert validate_email('ab@se.com')

    # testing for incorrect email format
    with pytest.raises(GPGError):
        validate_email('')
    with pytest.raises(GPGError):
        validate_email('a@a')


def test_validate_comment():
    # testing for correct comment format
    assert validate_comment('this is a comment')

    # testing for incorrect comment format
    with pytest.raises(GPGError):
        validate_comment('')


def test_validate_expire_date():
    now = datetime.datetime.now()
    one_month_from_now = now + datetime.timedelta(days=30)
    # testing for correct expire date
    assert validate_expire_date(one_month_from_now.isoformat().split('T')[0])

    # testing for incorrect expire date
    with pytest.raises(GPGError):
        validate_expire_date(now.isoformat().split('T')[0])
