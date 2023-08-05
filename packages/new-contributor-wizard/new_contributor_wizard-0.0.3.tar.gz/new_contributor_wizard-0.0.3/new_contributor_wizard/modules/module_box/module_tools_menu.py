'''
Modules containing Tools classes for Abstraction
'''
from importlib import import_module

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('ui/module_box/tools.kv')


class ToolBox(BoxLayout):
    '''
    ToolBox class to present available tools
    '''


class BackToToolsMenu(BoxLayout):
    '''
    BackToToolsMenu class presents back button and tool title
    '''


class ModuleToolsMenu(BoxLayout):
    '''
    ModuleToolsMenu class to present Tools Menu
    '''

    def __init__(self, root_module_name, tools, **kwargs):
        super(ModuleToolsMenu, self).__init__(**kwargs)

        self.all_tools = {}
        self.removed_tools_menu = None
        self.root_module_name = root_module_name

        if tools:
            for tool in tools:
                tool_key = '_'.join(tool['title'].lower().split())
                self.all_tools[tool_key] = tool
            self.populate_tools_menu()
        self.ids['module_tools_menu'].add_widget(Factory.InvitingContributors())

    def populate_tools_menu(self):
        '''
        populate_tools_menu gathers the information about the tools and
        populates it on the tools menu in GUI
        '''
        difficulty_palette = {
            'Beginner': (0.015, 0.588, 1, 1),
            'Intermediate': (0.2, 0.792, 0.498, 1),
            'Advance': (0.890, 0.090, 0.039, 1),
        }

        for key, value in self.all_tools.items():
            tool_title = value['title']
            tool_difficulty = value["difficulty"]
            tool_color = difficulty_palette[tool_difficulty]
            tool_box_widget = ToolBox()
            tool_box_widget.ids['tool_button'].bind(on_press=self.open_tool)
            tool_box_widget.id = key
            tool_box_widget.canvas.before.children[0].rgba = tool_color
            tool_box_widget.ids['tool_box_title'].text = tool_title
            tool_box_widget.ids['tool_box_difficulty'].text = tool_difficulty
            self.ids['module_tools_menu'].add_widget(tool_box_widget)
            self.import_tool_modules(key)

    def import_tool_modules(self, tool_to_import):
        '''
        import_tool_modules try to import tool_to_import named module and also
        the class ToolToImport
        '''
        module_name = tool_to_import
        class_name = ''.join(tool_to_import.title().split('_'))
        tool_module = import_module(
            'new_contributor_wizard.modules.course_modules.' +
            self.root_module_name + '.tools.' + module_name
        )
        tool_class = getattr(tool_module, class_name)
        self.all_tools[tool_to_import]['module'] = tool_module
        self.all_tools[tool_to_import]['class'] = tool_class

    def open_tool(self, button_object):
        '''
        open_tool creates a new widget with option to get back to the tools menu
        and also imports the selected tool module as the children widget
        '''
        tool_id = button_object.parent.parent.id
        self.removed_tools_menu = self.children[0]
        self.remove_widget(self.children[0])

        box_layout = BoxLayout()
        box_layout.id = 'module_tools_menu'
        box_layout.orientation = 'vertical'

        back_to_tool_menu = BackToToolsMenu()
        tool_id_object = self.all_tools[tool_id]
        back_to_tool_menu.ids['tool_title'].text = tool_id_object['title']
        back_to_tool_menu.ids['tools_menu_button'].bind(
            on_press=self.back_to_tools_menu
        )

        box_layout.add_widget(back_to_tool_menu)
        box_layout.add_widget(self.all_tools[tool_id]['class']())
        self.add_widget(box_layout)

    def back_to_tools_menu(self, button_object):
        '''
        back_to_tools_menu removed the tool widget and replaces tools menu
        '''
        self.remove_widget(button_object)
        self.remove_widget(self.children[0])
        self.add_widget(self.removed_tools_menu)
