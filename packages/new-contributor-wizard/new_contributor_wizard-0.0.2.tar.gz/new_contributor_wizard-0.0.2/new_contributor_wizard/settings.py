'''
Initializing application dependencies
- Sqlite3 database
'''
import os
import sqlite3
import logging
from zipfile import ZipFile
from io import BytesIO

import requests

DATABASE_FILE = 'new_contributor_wizard.db'
USER_INFOMATION_TABLE = 'USERS'
LIBRARY_GARDEN_PATH = 'new_contributor_wizard/libs/garden/'


def get_db_connection():
    '''
    Creating connection to the database and schema if required
    '''
    connection = sqlite3.connect(DATABASE_FILE)
    db_cursor = connection.cursor()
    try:
        db_cursor.execute('''
            CREATE TABLE USERS
            (id VARCHAR(36) PRIMARY KEY,
             email UNIQUE,
             password VARCHAR(64),
             fullname TEXT,
             language TEXT,
             timezone TEXT)
        ''')
        connection.commit()
        return connection
    except sqlite3.OperationalError:
        return connection


def installing_kivy_garden_package(package_name):
    '''
    Installing garden package and moving it to LIBRARY_GARDEN_PATH
    '''
    logging.basicConfig(level=logging.INFO)
    if not package_name.startswith('garden.'):
        package_name = 'garden.' + package_name
    url = 'https://github.com/kivy-garden/{}/archive/master.zip'.format(
        package_name
    )

    compact_package_name = package_name.split('garden.')[1]
    root_directory = os.getcwd()
    try:
        existing_garden_packages = os.listdir(
            root_directory + '/' + LIBRARY_GARDEN_PATH
        )
    except FileNotFoundError:
        os.makedirs(LIBRARY_GARDEN_PATH)
        existing_garden_packages = os.listdir(
            root_directory + '/' + LIBRARY_GARDEN_PATH
        )
    if compact_package_name in existing_garden_packages:
        logging.info('Garden: %s exists', compact_package_name)
        return

    logging.info('Garden: Downloading %s ...', url)
    response = requests.get(url)
    if response.status_code != 200:
        logging.info('''Garden: Unable to find the garden package.
                        (error=%s)''', response.status_code)
        return

    data = b''
    for buf in response.iter_content(1024):
        data += buf
    logging.info('Garden: Download done (%s downloaded)', package_name)

    ZipFile(BytesIO(data)).extractall()

    for existing_files_folders in os.listdir(root_directory):
        if 'garden.' in existing_files_folders:
            new_name = root_directory + '/' + LIBRARY_GARDEN_PATH + compact_package_name
            os.rename(existing_files_folders, new_name)
            success_log = compact_package_name + ' relocated to ' + new_name
            logging.info('Garden: %s', success_log)
            break
