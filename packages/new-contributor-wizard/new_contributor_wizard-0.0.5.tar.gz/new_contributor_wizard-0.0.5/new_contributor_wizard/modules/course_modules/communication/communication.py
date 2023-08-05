'''
Modules containing Communication classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class Communication(BoxLayout):
    '''
    Communication class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(Communication, self).__init__(**kwargs)
        self.module_box = ModuleBox("communication")
        self.add_widget(self.module_box)
