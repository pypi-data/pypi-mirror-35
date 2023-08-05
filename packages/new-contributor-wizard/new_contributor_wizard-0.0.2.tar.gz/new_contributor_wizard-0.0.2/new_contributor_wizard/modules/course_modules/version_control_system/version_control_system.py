'''
Modules containing Version Control System classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class VersionControlSystem(BoxLayout):
    '''
    VersionControlSystem class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(VersionControlSystem, self).__init__(**kwargs)
        self.module_box = ModuleBox("version_control_system")
        self.add_widget(self.module_box)
