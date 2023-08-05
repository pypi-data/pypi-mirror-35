'''
Modules containing Encryption classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class Encryption(BoxLayout):
    '''
    Encryption class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(Encryption, self).__init__(**kwargs)
        self.module_box = ModuleBox("encryption")
        self.add_widget(self.module_box)
