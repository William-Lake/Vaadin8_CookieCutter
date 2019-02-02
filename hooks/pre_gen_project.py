import os
import shutil

try:

    MAIN_PATH = os.path.join('src','main','java')

    TEST_PATH = os.path.join('src','test','java')

    package_path = '{{ cookiecutter.package_path }}'

    print(os.sep.join(package_path.split('.')))

    full_main_path = os.path.join(
        MAIN_PATH, 
        os.sep.join(package_path.split('.')))

    full_test_path = os.path.join(
        TEST_PATH, 
        os.sep.join(package_path.split('.')))

    print(full_main_path)

    print(full_test_path)

    os.makedirs(full_main_path)

    os.makedirs(full_test_path)

except:

    exit(1)