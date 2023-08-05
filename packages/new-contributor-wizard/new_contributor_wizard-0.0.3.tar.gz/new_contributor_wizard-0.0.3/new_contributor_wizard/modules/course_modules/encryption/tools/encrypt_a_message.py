'''
This module helps encrypt a message using public key
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

from new_contributor_wizard.modules.course_modules.encryption.tools.services import (
    list_gpg_all_keys, encrypt_message, create_key_listing_widget
)


Builder.load_file('./ui/encryption/encrypt_a_message.kv')


class KeyColumnBox(GridLayout):
    '''
    KeyColumnBox helps contain widgets and display them at the center of the box
    '''


class EncryptKeyBox(BoxLayout):
    '''
    EncryptKeyBox helps contain widgets and display them at the center of the
    box
    '''


class KeyInfoLabel(Label):
    '''
    KeyInfoLabel helps display key information
    '''


class DisplayAndManageKeyPair(BoxLayout):
    '''
    DisplayAndManageKeyPair helps integrate UI with helper functions
    '''


class EncryptMessagePopup(Popup):
    '''
    EncryptMessagePopup helps encrypt plain text into encrypted message
    '''


class NoKeyPresentEncrypt(BoxLayout):
    '''
    NoKeyPresentEncrypt will be displayed in case if no key is present
    '''


class EncryptAMessage(BoxLayout):
    '''
    EncryptAMessage integrated UI with helper functions
    '''

    def __init__(self, **kwargs):
        super(EncryptAMessage, self).__init__(**kwargs)
        all_keys = list_gpg_all_keys()
        self.populate_with_keys(all_keys['all_public_keys'])

    def populate_with_keys(self, all_public_keys):
        '''
        populate_with_keys displays all available public keys
        '''
        if all_public_keys.items():
            for key_column_box in create_key_listing_widget(
                    self.encrypt_message_popup, all_public_keys, EncryptKeyBox,
                    KeyColumnBox, KeyInfoLabel
            ):
                self.ids['scroll_view_box'].add_widget(key_column_box)
        else:
            self.ids['scroll_view_box'].clear_widgets()
            self.ids['scroll_view_box'].add_widget(NoKeyPresentEncrypt())

    @staticmethod
    def encrypt_message_popup(*args):
        '''
        encrypt_message_popup allows user to encrypt a message from plain text
        '''
        fingerprint = args[0].id
        encrypt_message_popup_object = EncryptMessagePopup()

        def get_encrypted_message(*args):
            '''
            get_encrypted_message receives all the data from input box in order
            to fetch encrypted message
            '''
            plain_message = args[1]
            if plain_message:
                encrypted_message = encrypt_message(fingerprint, plain_message)
                encrypt_message_popup_object.ids['encrypted_message'].text = encrypted_message
            else:
                encrypt_message_popup_object.ids['encrypted_message'].text = ''

        encrypt_message_popup_object.ids['plain_message'].bind(
            text=get_encrypted_message
        )

        encrypt_message_popup_object.open()
