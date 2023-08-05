'''
This modules helps display and manage key pairs
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

from new_contributor_wizard.modules.course_modules.encryption.tools.utils import extract_key_uid_info
from new_contributor_wizard.modules.course_modules.encryption.tools.services import (
    list_gpg_all_keys, export_single_key
)


Builder.load_file('./ui/encryption/display_and_manage_key_pair.kv')


class KeyColumnBox(GridLayout):
    '''
    KeyColumnBox helps contain widgets and display them at the center of the box
    '''


class KeyBox(BoxLayout):
    '''
    KeyBox helps contain widgets and display them at the center of the box
    '''


class KeyInfoLabel(Label):
    '''
    KeyInfoLabel helps display key information
    '''


class PublicKeyPopup(Popup):
    '''
    PublicKeyPopup helps display Public Key in UTF-8 inside a popup
    '''


class PrivateKeyPopup(Popup):
    '''
    PrivateKeyPopup helps display Private Key in UTF-8 inside a popup
    '''


class NoKeyPresent(BoxLayout):
    '''
    NoKeyPresent will be displayed in case if no key is present
    '''


class DisplayAndManageKeyPair(BoxLayout):
    '''
    DisplayAndManageKeyPair helps integrate UI with helper functions
    '''

    def __init__(self, **kwargs):
        super(DisplayAndManageKeyPair, self).__init__(**kwargs)
        all_keys = list_gpg_all_keys()
        self.populate_with_keys(
            all_keys['all_public_keys'],
            all_keys['all_private_keys']
        )

    def populate_with_keys(self, all_public_keys, all_private_keys):
        '''
        populate_with_keys displays all the available public and private keys
        '''
        if all_public_keys.items():
            for fingerprint, key_info in all_public_keys.items():
                user_info = extract_key_uid_info(key_info['uids'][0])
                key_column_box = KeyColumnBox()
                key_info_label = KeyInfoLabel(
                    text='\n'.join(user_info.values())
                )
                key_column_box.add_widget(key_info_label)

                # Spliting fingerprint to multiple lines to make it better on the UI
                # pylint: disable=invalid-name
                FINGERPRINT_LENGTH_BY_HALF = len(fingerprint) // 2
                fingerprint_text = fingerprint[:FINGERPRINT_LENGTH_BY_HALF] + '\n' +\
                    fingerprint[FINGERPRINT_LENGTH_BY_HALF:]
                key_info_label = KeyInfoLabel(text=fingerprint_text)
                key_column_box.add_widget(key_info_label)
                key_box = KeyBox()
                key_box.ids['Key_button'].id = fingerprint
                key_box.ids['Key_button'].bind(
                    on_press=self.display_public_key
                )
                key_column_box.add_widget(key_box)
                if fingerprint in all_private_keys.keys():
                    key_box = KeyBox()
                    key_box.ids['Key_button'].id = fingerprint
                    key_box.ids['Key_button'].bind(
                        on_press=self.display_private_key
                    )
                    key_column_box.add_widget(key_box)
                self.ids['scroll_view_box'].add_widget(key_column_box)
        else:
            self.ids['scroll_view_box'].clear_widgets()
            self.ids['scroll_view_box'].add_widget(NoKeyPresent())

    @staticmethod
    def display_public_key(*args):
        '''
        display_public_key helps display public key in plain text to the correspoding
        key fingerprint
        '''
        fingerprint = args[0].id

        public_key_popup = PublicKeyPopup()
        public_key = export_single_key(fingerprint)
        public_key_popup.ids['public_key_text_display'].text = public_key
        public_key_popup.open()

    @staticmethod
    def display_private_key(*args):
        '''
        display_private_key helps display private key in plain text to the correspoding
        key fingerprint and passphrase
        '''
        fingerprint = args[0].id

        def get_private_key(*args):
            '''
            get_private_key calls helper function to get private key in plain text
            '''
            passphrase = args[1]
            if passphrase:
                private_key = export_single_key(fingerprint, passphrase)
                if private_key:
                    private_key_popup.ids['private_key_text_display'].text = private_key
                else:
                    private_key_popup.ids['private_key_text_display'].text = 'Incorrect Passphrase'

        private_key_popup = PrivateKeyPopup()
        private_key_popup.ids['private_key_passphrase_input'].bind(
            text=get_private_key
        )
        private_key_popup.open()
