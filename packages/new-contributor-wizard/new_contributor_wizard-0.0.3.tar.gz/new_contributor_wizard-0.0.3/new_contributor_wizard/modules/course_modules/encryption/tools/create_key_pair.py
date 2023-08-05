'''
This modules helps display and manage key pairs
'''
import logging

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock

from new_contributor_wizard.modules.course_modules.encryption.tools.exceptions import GPGError
from new_contributor_wizard.modules.course_modules.encryption.tools.services import create_gpg_key_pair
from new_contributor_wizard.modules.course_modules.encryption.tools.validations import (
    validate_email, validate_name, validate_comment, validate_expire_date
)


Builder.load_file('./ui/encryption/create_key_pair.kv')


class CreateKeyPairPopup(Popup):
    '''
    CreateKeyPairPopup displays popup to inform about key creation progress
    '''


class CreateKeyPair(BoxLayout):
    '''
    CreateKeyPair helps integrate UI with helper functions
    '''

    def prompt_error_message(self, label, error_text):
        '''
        Displays error message on the UI on the respective label widget
        '''
        original_text = self.ids[label].text
        self.ids[label].text = error_text
        self.ids[label].color = [1, 0, 0, 1]

        def replace_label(*args):
            '''
            Replacing original text in label
            delay time is defined by args[0]
            '''
            logging.info(
                '\'%s\' changed to \'%s\' after %s seconds',
                error_text,
                original_text,
                args[0]
            )
            self.ids[label].text = original_text
            self.ids[label].color = [0, 0, 0, 1]
        Clock.schedule_once(replace_label, 2)

    def validate(self):
        '''
        Validating user input
        '''
        name = self.ids['input_name'].text
        email = self.ids['input_email'].text
        comment = self.ids['input_comment'].text
        expire_date = self.ids['input_expire_date'].text

        validation_successful = True
        try:
            validate_name(name)
        except GPGError as error:
            validation_successful = False
            self.prompt_error_message(
                'label_name',
                error.message
            )

        try:
            validate_email(email)
        except GPGError as error:
            validation_successful = False
            self.prompt_error_message(
                'label_email',
                error.message
            )

        try:
            validate_comment(comment)
        except GPGError as error:
            validation_successful = False
            self.prompt_error_message(
                'label_comment',
                error.message
            )

        try:
            validate_expire_date(expire_date)
        except GPGError as error:
            validation_successful = False
            self.prompt_error_message(
                'label_expire_date',
                error.message
            )

        return validation_successful

    def creating_key_pair(self):
        '''
        Processing user input to create key pair
        '''
        creating_key_pair_popup = CreateKeyPairPopup()

        def add_button(*args):
            '''
            Add Key fingerprint to label and button
            '''
            creating_key_pair_popup.ids['create_gpg_key_pair_popup_label'].text = args[0]

        if self.validate():
            name = self.ids['input_name'].text
            email = self.ids['input_email'].text
            comment = self.ids['input_comment'].text
            expire_date = self.ids['input_expire_date'].text

            try:
                creating_key_pair_popup.open()
                key_fingerprint = create_gpg_key_pair(
                    name=name,
                    email=email,
                    comment=comment,
                    expire_date=expire_date
                )
                message = 'Key has been created with\n{}\nfingerprint'.format(
                    key_fingerprint)
                add_button(message)
            except GPGError as error:
                add_button(error.message)
