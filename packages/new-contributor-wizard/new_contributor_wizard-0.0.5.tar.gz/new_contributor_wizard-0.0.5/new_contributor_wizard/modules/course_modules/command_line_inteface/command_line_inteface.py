'''
Modules containing CommandLineInterface classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class CommandLineInterface(BoxLayout):
    '''
    CommandLineInterface class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(CommandLineInterface, self).__init__(**kwargs)
        self.module_box = ModuleBox("command_line_inteface")
        self.add_widget(self.module_box)
