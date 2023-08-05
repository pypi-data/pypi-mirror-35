'''
Modules containing How To Use classes
'''
import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from new_contributor_wizard.modules.parsers import tutorial_parser


Builder.load_file('./ui/how_to_use.kv')


class HowToUse(BoxLayout):
    '''
    HowToUser class for introduction on how to user New
    Contributor Wizard
    '''

    def __init__(self, **kwargs):
        super(HowToUse, self).__init__(**kwargs)
        tutorial_to_import_path = os.path.join('new_contributor_wizard',
                                               'modules', 'course_modules',
                                               'how_to_use', 'how_to_use')
        self.add_widget(
            tutorial_parser.get_tutorial_widget(tutorial_to_import_path))
