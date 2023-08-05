'''
Root Kivy Application
'''
from kivy.app import App
from kivy.config import Config
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.settings import (
    get_db_connection, installing_kivy_garden_package, get_file_path)


class InvitingContributors(BoxLayout):
    '''
    InvitingContributors class has been imported from main.kv to display a block
    which invites new contributors to the project
    '''


class NewContributorWizard(App):
    '''
    Declaration of Root Kivy App which contains Root Widget
    '''
    @staticmethod
    def get_file_path(path, func=get_file_path):
        return func(path)

    def build(self):
        '''
        Overridding build method of App class to load custom kv file
        '''
        self.load_kv(self.get_file_path('ui/main.kv'))

    def switch_screen_to_dashboard(self):
        '''
        This method helps clear the widget and switch directly to the Dashboard
        '''
        self.root.clear_widgets()
        self.root.add_widget(Dashboard())
        Factory.register('InvitingContributors', cls=InvitingContributors)


def run_application():
    '''
    Setting up things
    '''
    get_db_connection()
    installing_kivy_garden_package('navigationdrawer')

    # Importing modules
    from new_contributor_wizard.modules.dashboard.dashboard import Dashboard
    from new_contributor_wizard.modules.signup.signup import SignUp
    from new_contributor_wizard.modules.signin.signin import SignIn

    # Fixing touch issue with some platforms
    Config.set('input', 'mouse', 'mouse')
    Config.set('graphics', 'minimum_width', 720)
    Config.set('graphics', 'minimum_height', 480)

    # Running Kivy application and building root Widget
    NewContributorWizard().run()


if __name__ == '__main__':
    run_application()
