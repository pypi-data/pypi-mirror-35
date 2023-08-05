from new_contributor_wizard.modules.signin.utils import clean_email


def test_clean_email():
    # checking strip operation on email
    assert clean_email('abc@shanky.xyz ') == 'abc@shanky.xyz'
    assert clean_email(' abc@shanky.xyz ') == 'abc@shanky.xyz'
    assert clean_email('abc@shanky.xyz   ') == 'abc@shanky.xyz'
    assert clean_email('\nabc@shanky.xyz ') == 'abc@shanky.xyz'
