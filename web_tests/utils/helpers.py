import os

import yaml


class Helpers:
    @staticmethod
    def get_config_data(key):
        with open("web_tests/config/config.yaml", "r") as config_file:
            config_data = yaml.safe_load(config_file)
        return config_data[key]

    @staticmethod
    def get_environment_data(key):
        with open("web_tests/config/config.yaml", "r") as config_file:
            config_data = yaml.safe_load(config_file)
        env = config_data['env']
        env_data = config_data['test_data'][env]
        return env_data[key]

    @staticmethod
    def get_formatted_url():
        with open("web_tests/config/config.yaml", "r") as config_file:
            config_data = yaml.safe_load(config_file)
        env = config_data['env']
        env_data = config_data['test_data'][env]
        return f"https://{os.environ.get('user')}:{os.environ.get('password')}@{env_data['base_url'].replace('https://', '')}"
