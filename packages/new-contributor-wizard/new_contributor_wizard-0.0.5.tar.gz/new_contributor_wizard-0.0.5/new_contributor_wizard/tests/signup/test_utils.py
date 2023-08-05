from new_contributor_wizard.modules.signup.utils import (
    generate_uuid,
    clean_email,
    clean_full_name,
    clean_timezone
)


def test_generate_uuid():
    # testing uuid length
    assert len(generate_uuid()) == 36

    # testing uuid format
    assert len(generate_uuid().split('-')) == 5


def test_clean_email():
    # testing clearning of spaces, tabs and newlines
    assert clean_email('abc@shanky.xyz ') == 'abc@shanky.xyz'
    assert clean_email(' abc@shanky.xyz ') == 'abc@shanky.xyz'
    assert clean_email('abc@shanky.xyz   ') == 'abc@shanky.xyz'
    assert clean_email('\nabc@shanky.xyz ') == 'abc@shanky.xyz'


def test_clean_full_name():
    # testing cleaning of spaces, tabs and newlines
    assert clean_full_name('Shashank    Kumar') == 'Shashank Kumar'
    assert clean_full_name('  Shashank    Kumar') == 'Shashank Kumar'
    assert clean_full_name('Shashank    Kumar  ') == 'Shashank Kumar'
    assert clean_full_name('  Shashank    Kumar  ') == 'Shashank Kumar'


def test_clean_timezone():
    # testing cleaning of spaces, tabs and lowercasing of timezone
    assert clean_timezone('UTC+00:00') == 'utc+00:00'
    assert clean_timezone('UtC+00:00     ') == 'utc+00:00'
    assert clean_timezone('     Utc-11:11') == 'utc-11:11'
