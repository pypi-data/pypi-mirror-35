'''
Service functions for encryption.tools module
'''
from subprocess import check_output

import gnupg

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.utils import extract_key_uid_info

GNUPG_HOME = 'gnupg_home'
IS_KEY_PRIVATE = True


def create_gnupg_object():
    '''
    Creating and returning GnuPG object
    '''
    gpg_binary_path = check_output(
        'which gpg2', shell=True).decode().strip('\n')
    if gpg_binary_path:
        gpg = gnupg.GPG(gnupghome=GNUPG_HOME, gpgbinary=gpg_binary_path)
        gpg.encoding = 'utf-8'
        return gpg
    raise GPGError('''Please install gpg2 using your Operating System\'s
        package manager''')


def create_gpg_key_pair(name, email, comment, expire_date, passphrase=''):
    '''
    Creating fresh public and private keys and returning key's fingerprint
    '''
    gpg = create_gnupg_object()

    key_length = 1024
    key_type = 'RSA'

    input_data = gpg.gen_key_input(
        key_length=key_length,
        key_type=key_type,
        name_real=name,
        name_comment=comment,
        name_email=email,
        expire_date=expire_date,
        passphrase=passphrase
    )
    key = gpg.gen_key(input_data)
    if key.fingerprint:
        return key.fingerprint
    raise GPGError(message=getattr(key, 'stderr'))


def list_gpg_all_keys():
    '''
    Returning all public and private keys available in keyring
    '''
    gpg = create_gnupg_object()

    # a key_map return a dictionary mapping key and subkey fingerprints to the
    # corresponding key’s dictionary
    return {
        'all_public_keys': gpg.list_keys().key_map,
        'all_private_keys': gpg.list_keys(IS_KEY_PRIVATE).key_map
    }


def export_single_key(key_id, passphrase=None):
    '''
    Returning public or private gpg key in ascii format
    '''
    gpg = create_gnupg_object()

    if passphrase:
        return gpg.export_keys(key_id, IS_KEY_PRIVATE, passphrase=passphrase)
    return gpg.export_keys(key_id)


def encrypt_message(key_id, message):
    '''
    Encrypting a message using a gpg public key
    '''
    gpg = create_gnupg_object()
    encrypted_message_object = gpg.encrypt(message, key_id)
    if encrypted_message_object.ok:
        return str(encrypted_message_object)
    raise GPGError(message=encrypted_message_object.status)


def decrypt_message(message, passphrase):
    '''
    Decrypting a message using private gpg key and passphrase
    '''
    gpg = create_gnupg_object()
    decrypted_message_object = gpg.decrypt(message, passphrase=passphrase)
    if decrypted_message_object.ok:
        return str(decrypted_message_object)
    raise GPGError(message=decrypted_message_object.status)


def create_key_listing_widget(
        message_popup, all_keys, key_box_object, key_column_box_object,
        key_info_label_object
):
    '''
    This function yields a widget with key information everytime it's called
    '''
    for fingerprint, key_info in all_keys.items():
        user_info = extract_key_uid_info(key_info['uids'][0])
        key_column_box = key_column_box_object()

        key_box = key_box_object()
        key_box.ids['Key_button'].id = fingerprint
        key_box.ids['Key_button'].bind(
            on_press=message_popup
        )
        key_column_box.add_widget(key_box)

        key_info_label = key_info_label_object(
            text='\n'.join(user_info.values())
        )
        key_column_box.add_widget(key_info_label)

        # Spliting fingerprint to multiple lines to make it better on the UI
        # pylint: disable=invalid-name
        FINGERPRINT_LENGTH_BY_HALF = len(fingerprint) // 2
        fingerprint_text = fingerprint[:FINGERPRINT_LENGTH_BY_HALF] + '\n' +\
            fingerprint[FINGERPRINT_LENGTH_BY_HALF:]
        key_info_label = key_info_label_object(text=fingerprint_text)
        key_column_box.add_widget(key_info_label)
        yield key_column_box
