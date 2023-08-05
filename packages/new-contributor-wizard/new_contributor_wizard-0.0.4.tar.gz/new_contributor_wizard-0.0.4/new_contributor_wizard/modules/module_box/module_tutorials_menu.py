'''
Modules containing Tutorials classes for Abstraction
'''
import os

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.parsers import tutorial_parser


Builder.load_file('./ui/module_box/tutorials.kv')


class TutorialBox(BoxLayout):
    '''
    TutorialBox class to present available Tutorials
    '''


class BackToTutorialsMenu(BoxLayout):
    '''
    BackToTutorialsMenu class presents back button and Tutorial title
    '''


class ModuleTutorialsMenu(BoxLayout):
    '''
    ModuleTutorialsMenu class to present Tutorials Menu
    '''

    def __init__(self, root_module_name, tutorials, **kwargs):
        super(ModuleTutorialsMenu, self).__init__(**kwargs)

        self.all_tutorials = {}
        self.removed_tutorials_menu = None
        self.root_module_name = root_module_name

        if tutorials:
            for tutorial in tutorials:
                tutorial_key = '_'.join(tutorial['title'].lower().split())
                self.all_tutorials[tutorial_key] = tutorial
            self.populate_tutorials_menu()
        self.ids['module_tutorials_menu'].add_widget(Factory.InvitingContributors())

    def populate_tutorials_menu(self):
        '''
        populate_tutorials_menu gathers the information about the tutorials and
        populates it on the tutorials menu in GUI
        '''
        difficulty_palette = {
            'Beginner': (0.015, 0.588, 1, 1),
            'Intermediate': (0.2, 0.792, 0.498, 1),
            'Advance': (0.890, 0.090, 0.039, 1),
        }

        for key, value in self.all_tutorials.items():
            tutorial_title = value['title']
            tutorial_difficulty = value["difficulty"]
            tutorial_color = difficulty_palette[tutorial_difficulty]
            tutorial_box_widget = TutorialBox()
            tutorial_box_widget.ids['tutorial_button'].bind(
                on_press=self.open_tutorial)
            tutorial_box_widget.id = key  # pylint: disable=invalid-name
            tutorial_box_widget.canvas.before.children[0].rgba = tutorial_color
            tutorial_box_widget.ids['tutorial_box_title'].text = tutorial_title
            t_d = tutorial_difficulty
            tutorial_box_widget.ids['tutorial_box_difficulty'].text = t_d
            self.ids['module_tutorials_menu'].add_widget(tutorial_box_widget)

    def get_tutorial_modules(self, tutorial_to_import):
        '''
        return requested tutorial by calling get_tutorial_widget of
        tutorial_parser
        '''
        tutorial_to_import_path = os.path.join('new_contributor_wizard',
                                               'modules', 'course_modules',
                                               self.root_module_name,
                                               'tutorials', tutorial_to_import)
        return tutorial_parser.get_tutorial_widget(tutorial_to_import_path)

    def open_tutorial(self, button_object):
        '''
        Opens selected tutorial from the Menu
        '''
        tutorial_id = button_object.parent.parent.id
        self.removed_tutorials_menu = self.children[0]
        self.remove_widget(self.children[0])

        box_layout = BoxLayout()
        box_layout.id = 'module_tutorials_menu'  # pylint: disable=invalid-name
        box_layout.orientation = 'vertical'

        back_to_tutorial_menu = BackToTutorialsMenu()
        back_to_tutorial_menu.ids['tutorial_title'].text = self.all_tutorials[tutorial_id]['title']
        back_to_tutorial_menu.ids['tutorials_menu_button'].bind(
            on_press=self.back_to_tutorials_menu
        )

        box_layout.add_widget(back_to_tutorial_menu)
        box_layout.add_widget(self.get_tutorial_modules(tutorial_id))
        self.add_widget(box_layout)

    def back_to_tutorials_menu(self, button_object):
        '''
        back_to_tutorials_menu removes the tutorial widget and replaces tutorials menu
        '''
        self.remove_widget(button_object)
        self.remove_widget(self.children[0])
        self.add_widget(self.removed_tutorials_menu)
