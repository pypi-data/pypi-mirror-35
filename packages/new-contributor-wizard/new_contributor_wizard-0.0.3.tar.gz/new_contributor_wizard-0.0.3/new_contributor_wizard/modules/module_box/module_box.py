'''
Modules containing ModuleBox classes
'''
import os
import json

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from new_contributor_wizard.modules.module_box.module_tools_menu import ModuleToolsMenu
from new_contributor_wizard.modules.module_box.module_tutorials_menu import ModuleTutorialsMenu


Builder.load_file('./ui/module_box/module_box.kv')


class ModuleBox(BoxLayout):
    '''
    ModuleBox class for tutorials and tools
    '''

    def __init__(self, root_module_name, **kwargs):
        super(ModuleBox, self).__init__(**kwargs)

        module_data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)).split('new_contributor_wizard')[0],
            'new_contributor_wizard/data/module_data.json')
        with open(module_data_path) as data:
            json_data = json.loads(data.read())
            for data in json_data:
                if root_module_name in data.keys():
                    self.module_data = data[root_module_name]
                    break

        module_title = ' '.join(
            [name.capitalize() for name in root_module_name.split('_')])
        self.ids['module_title'].text = module_title
        self.ids['module_description'].text = self.module_data['description']

        self.all_options = {
            'tutorials': ModuleTutorialsMenu(
                root_module_name=root_module_name,
                tutorials=self.module_data["tutorials"]),
            'tools': ModuleToolsMenu(
                root_module_name=root_module_name,
                tools=self.module_data["tools"]),
        }
        self.all_options_items = list(self.all_options.keys())

    def enable_option(self, option_to_enable):
        '''
        enable_menu function focuses on concerned menu items or settings which
        is clicked and removes focus from all other menu items and settings
        '''
        if 'module_details_box' in self.ids:
            self.ids['module_content_box'].remove_widget(
                self.ids['module_content_box'].children[0])
            del(self.ids['module_details_box'])

        option_to_enable_widget = self.ids[option_to_enable + '_box']
        widget_canvas = option_to_enable_widget.canvas
        option_to_enable_color = widget_canvas.before.children[0].rgba
        if option_to_enable_color != [1, 1, 1, 1]:
            self.ids[option_to_enable + '_box'].canvas.before.children[0].rgba\
                = [1, 1, 1, 1]
            self.ids[option_to_enable].color = (0, 0, 0, 1)

            # removing enabled option from the list in order to disable all
            # other options
            options_to_disable = self.all_options_items[:]
            options_to_disable.remove(option_to_enable)

            for option in options_to_disable:
                self.ids[option + '_box'].canvas.before.children[0].rgba =\
                    [0, 0, 0, 1]
                self.ids[option].color = (1, 1, 1, 1)
                self.ids['module_content_box'].remove_widget(
                    self.all_options[option]
                )

            self.ids['module_content_box'].add_widget(
                self.all_options[option_to_enable]
            )
