'''
Helps parse tutorials using json files and build widgets accordingly for the UI
'''
import os
import json
import logging

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window


Builder.load_file('./ui/parsers/tutorial_parser.kv')

# Filename of the Tutorial JSON used to build the Kivy GUI
TUTORIAL_JSON = ''


class LessonScreenManager(ScreenManager):
    '''
    LessonScreenManager is used to handle multiple lessons of a tutorial
    '''


class LessonScreen(Screen):
    '''
    LessonScreen is used to define single screen for the LessonScreenManager
    '''


class LessonContent(BoxLayout):
    '''
    LessonContent is used to hold different lesson objects
    '''


class LessonNavigation(BoxLayout):
    '''
    LessonNavigation is used to create navigation bar for the screen in order to
    switch from one lesson to another
    '''


class PreviousLessonButton(Button):
    '''
    PreviousLessonButton is used to switch to previous lesson
    '''


class NextLessonButton(Button):
    '''
    NextLessonButton is used to  switch to next lesson
    '''


class LessonHeader(BoxLayout):
    '''
    LessonHeader is used to show Lesson number
    '''


class LessonTextBox(BoxLayout):
    '''
    LessonTextBox is used to display text type content
    '''


class LessonQuestionBox(BoxLayout):
    '''
    LessonQuestionBox is used to display question type content
    '''


class LessonImageBox(BoxLayout):
    '''
    LessonImageBox is used to display image type content
    '''


class LessonCodeBox(BoxLayout):
    '''
    LessonCodeBox is used to display code type content
    '''


def get_tutorial_widget(tutorial_to_import_path):
    '''
    get_tutorial_widget imports json tutorial and try to build widget tree for the UI
    '''
    lesson_screen_manager = LessonScreenManager()

    global TUTORIAL_JSON  # pylint: disable=global-statement
    TUTORIAL_JSON = os.path.join(
        os.path.dirname(os.path.realpath(__file__)).split('new_contributor_wizard')[0],
        tutorial_to_import_path + '.json')

    with open(TUTORIAL_JSON) as data:
        tutorial = json.load(data)

    lesson_no = 0
    for lesson in tutorial:
        lesson_no += 1
        lesson_screen = LessonScreen(name=str(lesson_no))

        lesson_content = LessonContent()
        lesson_header = LessonHeader()
        lesson_header.ids['lesson_header_label'].text = 'Lesson ' + str(
            lesson_no)
        lesson_content.ids['scroll_tutorial_content_box'].add_widget(
            lesson_header)

        for content_part in lesson['lesson']:
            lesson_content_widget = get_tutorial_content_widget(content_part)
            lesson_content.ids['scroll_tutorial_content_box'].add_widget(
                lesson_content_widget)

        lesson_navigation = get_lesson_navigation(lesson_screen_manager,
                                                  tutorial, lesson_no)

        lesson_content.ids['scroll_tutorial_content_box'].add_widget(
            lesson_navigation)
        lesson_screen.add_widget(lesson_content)
        lesson_screen_manager.add_widget(lesson_screen)

    return lesson_screen_manager


def get_lesson_navigation(lesson_screen_manager, tutorial, lesson_no):
    '''
    get_lesson_navigation builds and return navigation buttons for a lesson
    '''
    lesson_navigation = LessonNavigation()
    if lesson_no > 1:
        previous_lesson_button = PreviousLessonButton()

        def navigate_backward(button_object):
            '''
            navigate_backward navigates screen to previous lesson of the tutorial
            '''
            lesson_screen_manager.transition.direction = 'right'
            lesson_screen_manager.current = button_object.id

        previous_lesson_button.id = str(lesson_no - 1)  # pylint: disable=invalid-name
        previous_lesson_button.bind(on_press=navigate_backward)
        lesson_navigation.add_widget(previous_lesson_button)
    else:
        lesson_navigation.add_widget(FloatLayout())

    if not lesson_no < len(tutorial):
        lesson_navigation.add_widget(FloatLayout())
    else:
        next_lesson_button = NextLessonButton()

        def navigate_forward(button_object):
            '''
            navigate_forward navigates screen to next lesson of the tutorial
            '''
            lesson_screen_manager.transition.direction = 'left'
            lesson_screen_manager.current = button_object.id

        next_lesson_button.id = str(lesson_no + 1)  # pylint: disable=invalid-name
        next_lesson_button.bind(on_press=navigate_forward)
        lesson_navigation.add_widget(next_lesson_button)

    return lesson_navigation


def log_error_message(error_message):
    '''
    Log error message in case of any error in building Kivy GUI
    '''
    global TUTORIAL_JSON  # pylint: disable=global-statement
    logging.info(
        'Tutorial Parser: File - %s : Error - %s',
        TUTORIAL_JSON,
        error_message)


def get_text_widget(content_part):
    '''
    get_text_widget will build a widget tree to display text type content
    of the tutorial
    '''
    if 'content' in content_part:
        text = content_part['content']
    else:
        text = '[color=d3d3d3]Empty Text Was Provided Here![/color]'
        log_error_message('Empty Text Was Provided')
    lesson_box = LessonTextBox()
    lesson_box.ids['lesson_label'].text = text

    def change_lesson_label(*args):
        '''
        change_lesson_label changes dimensions of label and
        it's parent with every change of width of Window
        '''
        window_width = args[1]
        lesson_box.ids['lesson_label'].width = window_width
        lesson_box.ids['lesson_label'].texture_update()
        lesson_box.ids['lesson_label'].padding = [20, 0]
        lesson_box.height = lesson_box.ids['lesson_label'].texture_size[1]

    change_lesson_label(Window, Window.width)
    Window.bind(width=change_lesson_label)
    return lesson_box


def get_question_widget(content_part):
    '''
    get_question_widget will build a widget tree to display question type content
    of the tutorial
    '''
    question_box = LessonQuestionBox()
    if 'content' in content_part:
        if 'question' in content_part['content']:
            question = content_part['content']['question']
        else:
            question = '[color=d3d3d3]Empty Question Was Provided Here![/color]'
            log_error_message('Empty Question Was Provided')
    else:
        question = '[color=d3d3d3]Empty Question Was Provided Here![/color]'
        log_error_message('Empty Question Was Provided')
    question_box.ids['lesson_question_label'].text = question

    if 'hint' in content_part['content']:
        hint = content_part['content']['hint']
        question_box.ids['lesson_question_input'].hint_text = hint

    def on_answer_change(*_):
        '''
        on_answer_change resets validation messages when user changes answer
        '''
        question_box.ids['lesson_answer_validation'].text = ''

    question_box.ids['lesson_question_input'].bind(text=on_answer_change)

    def on_submit_answer(*_):
        '''
        on_submit_answer is triggered when answer is submitted with and
        validated accordingly
        '''
        if 'answer' in content_part['content']:
            answer = content_part['content']['answer']
        else:
            answer = ''
        question_box_object = question_box.ids['lesson_answer_validation']
        if question_box.ids['lesson_question_input'].text == answer:
            question_box_object.color = [0, 1, 0, 1]
            question_box_object.text = 'Your answer is correct!'
        else:
            question_box_object.color = [1, 0, 0, 1]
            question_box_object.text = 'Your answer is incorrect!'

    question_box.ids['lesson_submit_answer'].bind(on_press=on_submit_answer)
    return question_box


def get_image_widget(content_part):
    '''
    get_image_widget will build a widget tree to display image type content
    of the tutorial
    '''
    if 'content' in content_part:
        if content_part['content']:
            content_url = content_part['content']
            lesson_image_box = LessonImageBox()
            if content_url.lower().startswith('http'):
                image_object = AsyncImage(source=content_url)
            else:
                image_object = Image(source=content_url)
            lesson_image_box.add_widget(image_object)

            def change_lesson_image_box(*args):
                '''
                change_lesson_image_box changes dimensions of image box
                with every change of width of Window
                '''
                window_width = args[1]
                if window_width / 2 < 350:
                    lesson_image_box.height = 350
                elif window_width / 2 > 500:
                    lesson_image_box.height = 500
                else:
                    lesson_image_box.height = window_width / 2

            change_lesson_image_box(Window, Window.width)
            Window.bind(width=change_lesson_image_box)
            return lesson_image_box

    lesson_error_box = LessonTextBox()
    error_message = '[color=d3d3d3]Invalid Image URL Provided Here![/color]'
    lesson_error_box.ids['lesson_label'].text = error_message
    log_error_message('Invalid Image URL Provided!')

    def change_lesson_error_label(*args):
        '''
        change_lesson_error_label changes dimensions of label and
        it's parent with every change of width of Window
        '''
        window_width = args[1]
        lesson_error_box.ids['lesson_label'].width = window_width
        lesson_error_box.ids['lesson_label'].texture_update()
        lesson_error_box.ids['lesson_label'].padding = [20, 0]
        lesson_error_box.height = lesson_error_box.ids['lesson_label'].texture_size[1]

    change_lesson_error_label(Window, Window.width)
    Window.bind(width=change_lesson_error_label)
    return lesson_error_box


def get_code_widget(content_part):
    '''
    get_code_widget will build a widget tree to display code type content
    of the tutorial
    '''
    lesson_code_box = LessonCodeBox()
    if 'content' in content_part:
        code = content_part['content']
    else:
        code = '[color=d3d3d3]Invalid Code Provided Here![/color]'
        log_error_message('Invalid Code Provided!')
    lesson_code_box.ids['lesson_code_block'].text = code
    return lesson_code_box


def get_tutorial_content_widget(content_part):
    '''
    get_tutorial_content_widget
    '''
    if content_part['type'] == 'text':
        return get_text_widget(content_part)

    if content_part['type'] == 'question':
        return get_question_widget(content_part)

    if content_part['type'] == 'image':
        return get_image_widget(content_part)

    if content_part['type'] == 'code':
        return get_code_widget(content_part)

    lesson_box = LessonTextBox()
    error_message = '[color=d3d3d3]Invalid Content Type Provided Here![/color]'
    lesson_box.ids['lesson_label'].text = error_message
    log_error_message('Invalid Content Type Provided!')
    return lesson_box
