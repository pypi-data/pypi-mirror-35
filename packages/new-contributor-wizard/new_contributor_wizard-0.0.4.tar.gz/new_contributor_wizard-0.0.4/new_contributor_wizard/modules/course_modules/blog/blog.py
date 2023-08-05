'''
Modules containing Blog classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class Blog(BoxLayout):
    '''
    Blog class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(Blog, self).__init__(**kwargs)
        self.module_box = ModuleBox("blog")
        self.add_widget(self.module_box)
