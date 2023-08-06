import tempfile
from distutils.dir_util import copy_tree
from os.path import join
from .pom import Pom
from .settings import Settings
from .file_service import *
from .maven_service import *


def publish(input_directory, username, password, bucket_name):
    with tempfile.TemporaryDirectory() as temp_dir:
        # copy input to a temporary directory
        copy_tree(input_directory, temp_dir)
        # rewrite pom
        pom_path = join(temp_dir, 'pom.xml')
        original_pom_content = get_file_content(pom_path)
        pom = Pom(original_pom_content, bucket_name)
        write_file_content(pom_path, pom.tostring())
        # write settings
        settings_path = join(temp_dir, 'settings.xml')
        settings = Settings(username, password)
        write_file_content(settings_path, settings.tostring())
        # maven deploy
        deploy(temp_dir, settings_path)



