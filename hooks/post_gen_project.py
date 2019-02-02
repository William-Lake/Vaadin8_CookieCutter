import os
import shutil

MAIN_PATH = os.path.join('src','main','java')

TEST_PATH = os.path.join('src','test','java')

PROJECT_NAME = '{{ cookiecutter.project_name }}'

PACKAGE_PATH = '{{ cookiecutter.package_path }}'

APP_FILE_NAME = PROJECT_NAME + '.java'

TEST_APP_FILE_NAME = PROJECT_NAME + 'Tests.java'

UI_FILE_NAME = 'PrimaryUI.java'

REST_CLIENT_FILE_NAME = 'RestClient.java'

MAIN_DIR = os.path.join(
    MAIN_PATH, 
    os.sep.join(PACKAGE_PATH.split('.')))

TEST_DIR = os.path.join(
    TEST_PATH, 
    os.sep.join(PACKAGE_PATH.split('.')))

UI_DIR = os.path.join(
    MAIN_DIR,
    'ui'
)

REST_DIR = os.path.join(
    MAIN_DIR,
    'rest'
)


def make_dirs_move_file(path_to_make, file_name):

    try:

        os.makedirs(path_to_make)

        shutil.move(
            file_name, 
            os.path.join(
                path_to_make,
                file_name
            )
        )

    except Exception as e:

        print(str(e))

        exit(1)

try:

    '''
    Create dirs for main/test files.
    Move main/test files
    If the user wants the UI files
        create dir
        move file
    else
        delete file
    If the user wants the RestClient files
        create dir
        move file
    '''

    make_dirs_move_file(
        MAIN_DIR,
        APP_FILE_NAME
    )

    make_dirs_move_file(
        TEST_DIR,
        TEST_APP_FILE_NAME
    )

    if '{{ cookiecutter.ui_class_generation }}' == 'Yes':

        make_dirs_move_file(
            UI_DIR,
            UI_FILE_NAME
        )

    else: os.remove(UI_FILE_NAME)

    if '{{ cookiecutter.restclient_class_generation }}' == 'Yes':

        make_dirs_move_file(
            REST_DIR,
            REST_CLIENT_FILE_NAME
        )

    else: os.remove(REST_CLIENT_FILE_NAME)

except Exception as e:

    print(str(e))

    exit(1)