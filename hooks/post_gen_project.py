import os
import shutil

try:

    MAIN_PATH = os.path.join('src','main','java')

    TEST_PATH = os.path.join('src','test','java')

    project_name = '{{ cookiecutter.project_name }}'

    package_path = '{{ cookiecutter.package_path }}'

    app_file_name = '{{ cookiecutter.project_name }}' + '.java'

    test_app_file_name = '{{ cookiecutter.project_name }}' + 'Tests.java'

    src_main_path = os.path.join(
        project_name,
        app_file_name
    )

    src_test_path = os.path.join(
        project_name,
        test_app_file_name
    )

    dest_main_path = os.path.join(
        project_name,
        MAIN_PATH, 
        os.sep.join(package_path.split('.')),
        app_file_name)

    dest_test_path = os.path.join(
        project_name,
        TEST_PATH, 
        os.sep.join(package_path.split('.')),
        test_app_file_name)

    print(src_main_path)

    print(dest_main_path)

    print(src_test_path)

    print(dest_test_path)

    shutil.move(src_main_path, dest_main_path)

    shutil.move(src_test_path, dest_test_path)

except:

    exit(1)