'''
Dashboard module includes classes to showcase Dashboard with different courseware and settings
'''
import logging

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
try:
    from new_contributor_wizard.libs.garden.navigationdrawer import NavigationDrawer
except ImportError:
    logging.info('Dashboard: Install navigationdrawer from garden')

from new_contributor_wizard.modules.course_modules.blog.blog import Blog
from new_contributor_wizard.modules.course_modules.command_line_inteface.command_line_inteface import\
    CommandLineInterface
from new_contributor_wizard.modules.course_modules.communication.communication import Communication
from new_contributor_wizard.modules.course_modules.encryption.encryption import Encryption
from new_contributor_wizard.modules.course_modules.how_to_use.how_to_use import HowToUse
from new_contributor_wizard.modules.course_modules.version_control_system.version_control_system\
    import VersionControlSystem
from new_contributor_wizard.modules.course_modules.way_ahead.way_ahead import WayAhead


Builder.load_file('./ui/dashboard.kv')


class Dashboard(BoxLayout, Screen):
    '''
    Dashboard class to integrate courseware and settings
    '''
