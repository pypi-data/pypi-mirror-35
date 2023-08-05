import pytest

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.services import (
    GNUPG_HOME,
    create_gnupg_object,
    create_gpg_key_pair,
    list_gpg_all_keys,
    export_single_key,
    encrypt_message,
    decrypt_message,
)


def test_create_gnupg_object():
    gpg = create_gnupg_object()
    assert gpg.gnupghome == GNUPG_HOME


def test_create_gpg_key_pair():
    data = {
        'name': 'Mr. Shashank Kumar',
        'comment': 'My first key pair',
        'email': 'shashankkumar@gmail.com',
        'passphrase': 'justanotherpass',
        'expire_date': '2020-12-12',
    }
    # checking for key pair creation
    assert create_gpg_key_pair(**data)


def test_list_all_keys():
    keys = list_gpg_all_keys()

    # checking for all the public and private key pair present
    assert keys['all_public_keys'].items()
    assert keys['all_private_keys'].items()


def test_export_single_key():
    # checking public and private key export
    assert export_single_key('shashankkumar@gmail.com')
    assert export_single_key('shashankkumar@gmail.com',
                             passphrase='justanotherpass')

    # validating incorrect export of non existing keys
    assert not export_single_key('shanky@shanky.xyz')
    assert not export_single_key('sanyamkhurana@gmail.com')


def test_encrypt_message():
    message = 'Will meet you on tomorrow at 9AM near Rajiv Chauk Metro Station'
    # checking for correct encryption
    assert encrypt_message('shashankkumar@gmail.com',
                           message=message)
    assert encrypt_message('shashankkumar@gmail.com', message='')

    # checking for invalid encryption
    with pytest.raises(GPGError):
        encrypt_message('shanky@shanky.xyz', message=message)


def test_decrypt_message():
    message = 'Will meet you on tomorrow at 9AM near Rajiv Chauk Metro Station'
    encrypted_message = encrypt_message('shashankkumar@gmail.com',
                                        message=message)

    # checking for valid decryption
    assert message == decrypt_message(encrypted_message,
                                      passphrase='justanotherpass')

    # checking for invalid decryption
    with pytest.raises(GPGError):
        decrypt_message(message, passphrase='oldpass')
