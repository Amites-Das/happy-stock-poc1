import sys
import os
import configparser


class Configuration:

    def __init__(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(base_dir, 'model_settings.txt'))

    def get_path_constant(self, key):
        # returns local file path
        return self.config.get('local_file_path', key)

    def get_file_name(self, key):
        # returns file names
        return self.config.get('local_file_name', key)
