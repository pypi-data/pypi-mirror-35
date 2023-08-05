'''
Class for SignUp Screen
'''
import logging

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from new_contributor_wizard.modules.signup.services import sign_up_user
from new_contributor_wizard.modules.signup.exceptions import SignUpError
from new_contributor_wizard.modules.signup.validations import (
    validate_email, validate_first_pass, validate_confirm_pass,
    validate_full_name, validate_timezone)


Builder.load_file('./ui/signup.kv')


class SignUp(BoxLayout, Screen):
    '''
    Declaration of SignUp Screen Class
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
            self.ids[label].text = original_text
            self.ids[label].color = [1, 1, 1, 1]
            logging.info(
                'SignUp: \'%s\' changed to \'%s\' after %s seconds',
                error_text,
                original_text,
                args[0]
            )
        Clock.schedule_once(replace_label, 2)

    def validate(self):
        '''
        Validating Email, Password and Full Name provided by user
        '''
        email_validation = True
        name_validation = True
        password_validation = True
        timezone_validation = True

        user_email = self.ids['user_email'].text
        try:
            validate_email(user_email)
        except SignUpError as error:
            self.prompt_error_message(
                'email_label',
                error.message,
            )
            email_validation = False

        first_pass = self.ids['first_pass'].text
        try:
            validate_first_pass(first_pass)
        except SignUpError as error:
            self.prompt_error_message(
                'first_pass_label',
                error.message,
            )
            password_validation = False

        confirm_pass = self.ids['confirm_pass'].text
        try:
            validate_confirm_pass(first_pass, confirm_pass)
        except SignUpError as error:
            self.prompt_error_message(
                'confirm_pass_label',
                error.message,
            )
            password_validation = False

        full_name = self.ids['user_full_name'].text
        try:
            validate_full_name(full_name)
        except SignUpError as error:
            self.prompt_error_message(
                'full_name_label',
                error.message,
            )
            name_validation = False

        timezone = self.ids['user_timezone'].text
        try:
            validate_timezone(timezone)
        except SignUpError as error:
            self.prompt_error_message(
                'timezone_label',
                error.message,
            )
            timezone_validation = False

        return email_validation and name_validation and password_validation\
            and timezone_validation

    def sign_up(self, *args):
        '''
        Signing Up user's account in case of successful validation
        Prompting error message to the user otherwise
        '''
        app_object = args[0]
        if self.validate():
            email = self.ids['user_email'].text
            password = self.ids['first_pass'].text
            full_name = self.ids['user_full_name'].text
            language = self.ids['user_language'].text
            timezone = self.ids['user_timezone'].text
            try:
                sign_up_user(
                    email=email,
                    password=password,
                    full_name=full_name,
                    language=language,
                    timezone=timezone
                )
                app_object.switch_screen_to_dashboard()
            except SignUpError as error:
                self.prompt_error_message(
                    'email_label',
                    error.message
                )
