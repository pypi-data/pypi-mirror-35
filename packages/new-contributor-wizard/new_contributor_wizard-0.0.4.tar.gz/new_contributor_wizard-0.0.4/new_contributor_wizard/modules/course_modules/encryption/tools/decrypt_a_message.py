'''
This modules helps decrypt a message using private key
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.services import (
    list_gpg_all_keys, decrypt_message, create_key_listing_widget
)


Builder.load_file('./ui/encryption/decrypt_a_message.kv')


class KeyColumnBox(GridLayout):
    '''
    KeyColumnBox helps contain widgets and display them at the center of the box
    '''


class DecryptKeyBox(BoxLayout):
    '''
    DecryptKeyBox helps contain widgets and display them at the center of the box
    '''


class KeyInfoLabel(Label):
    '''
    KeyInfoLabel helps display key information
    '''


class DisplayAndManageKeyPair(BoxLayout):
    '''
    DisplayAndManageKeyPair helps integrate UI with helper functions
    '''


class DecryptMessagePopup(Popup):
    '''
    DecryptMessagePopup helps take encrypted message and passphrase and display
    decrypted message on a popup
    '''


class NoKeyPresentDecrypt(BoxLayout):
    '''
    NoKeyPresentDecrypt will be displayed in case if no key is present
    '''


class DecryptAMessage(BoxLayout):
    '''
    DecryptAMessage integrated UI with helper functions
    '''

    def __init__(self, **kwargs):
        super(DecryptAMessage, self).__init__(**kwargs)
        all_keys = list_gpg_all_keys()
        self.populate_with_keys(all_keys['all_private_keys'])

    def populate_with_keys(self, all_private_keys):
        '''
        populate_with_keys displays all the available private keys that can be
        used to decrypt message
        '''
        if all_private_keys.items():
            for key_column_box in create_key_listing_widget(
                    self.decrypt_message_popup, all_private_keys, DecryptKeyBox,
                    KeyColumnBox, KeyInfoLabel
            ):
                self.ids['scroll_view_box'].add_widget(key_column_box)
        else:
            self.ids['scroll_view_box'].clear_widgets()
            self.ids['scroll_view_box'].add_widget(NoKeyPresentDecrypt())

    @staticmethod
    def decrypt_message_popup(*args):
        '''
        decrypt_message_popup allows user to decrypt a message using passphrase
        and encrypted message
        '''
        decrypt_message_popup_object = DecryptMessagePopup()

        def get_decrypted_message(*args):
            '''
            get_decrypted_message receives all the data from input box in order
            to fetch decrypted message
            '''
            if args:
                encrypted_message = decrypt_message_popup_object.ids['encrypted_message'].text
                passphrase = decrypt_message_popup_object.ids['passphrase_input'].text
                decrypt_message_object = decrypt_message_popup_object.ids['decrypted_message']
            if not passphrase:
                decrypt_message_object.text = 'Enter Passphrase'
            elif encrypted_message:
                try:
                    decrypted_message = decrypt_message(encrypted_message, passphrase)
                    if decrypted_message:
                        decrypt_message_object.text = decrypted_message
                    else:
                        decrypt_message_object.text = 'Incorrect Passphrase'
                except GPGError as error:
                    decrypt_message_object.text = error.message
            else:
                decrypt_message_object.text = ''

        decrypt_message_popup_object.ids['encrypted_message'].bind(
            text=get_decrypted_message
        )
        decrypt_message_popup_object.ids['passphrase_input'].bind(
            text=get_decrypted_message
        )
        if args:
            decrypt_message_popup_object.open()
