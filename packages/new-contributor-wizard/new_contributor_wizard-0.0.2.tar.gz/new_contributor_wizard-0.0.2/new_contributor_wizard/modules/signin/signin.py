'''
Class for SignIn Screen
'''
import logging

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from new_contributor_wizard.modules.signin.services import sign_in_user
from new_contributor_wizard.modules.signin.exceptions import SignInError
from new_contributor_wizard.modules.signin.validations import validate_email, validate_password


Builder.load_file('./ui/signin.kv')


class SignIn(BoxLayout, Screen):
    '''
    Declaration of SignIn Screen Class
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
                'SignIn: \'%s\' changed to \'%s\' after %s seconds',
                error_text,
                original_text,
                args[0]
            )
            self.ids[label].text = original_text
            self.ids[label].color = [1, 1, 1, 1]
        Clock.schedule_once(replace_label, 2)

    def validate(self):
        '''
        Validating Email and Password provided by user
        '''
        email_validation = True
        password_validation = True

        user_email = self.ids['user_email'].text
        try:
            validate_email(user_email)
        except SignInError as error:
            self.prompt_error_message(
                'email_label',
                error.message,
            )
            email_validation = False

        password = self.ids['password'].text
        try:
            validate_password(password)
        except SignInError as error:
            self.prompt_error_message(
                'password_label',
                error.message,
            )
            password_validation = False

        return email_validation and password_validation

    def sign_in(self, *args):
        '''
        Signin user in case of successful validation
        Prompting error message to the user otherwise
        '''
        app_object = args[0]
        if self.validate():
            user_email = self.ids['user_email'].text
            user_pass = self.ids['password'].text
            try:
                sign_in_user(
                    email=user_email,
                    password=user_pass
                )
                app_object.switch_screen_to_dashboard()
            except SignInError as error:
                self.prompt_error_message(
                    'email_label',
                    error.message
                )
