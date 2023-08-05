'''
Modules containing Way Ahead classes
'''
from kivy.uix.boxlayout import BoxLayout

from new_contributor_wizard.modules.module_box.module_box import ModuleBox


class WayAhead(BoxLayout):
    '''
    WayAhead class for tutorials and tools
    '''

    def __init__(self, **kwargs):
        super(WayAhead, self).__init__(**kwargs)
        self.module_box = ModuleBox("way_ahead")
        self.add_widget(self.module_box)
