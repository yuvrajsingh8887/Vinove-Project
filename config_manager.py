import configparser
import os

class ConfigManager:
    def __init__(self, config_file='config/settings.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            self.create_default_config()
        self.config.read(self.config_file)

    def create_default_config(self):
        self.config['DEFAULT'] = {
            'screenshot_interval': '300',  # in seconds
            'upload_interval': '300',      # in seconds
            'duration': '3000',           # in seconds 
            's3_bucket': 'monitoring-agent-vinove',
            's3_access_key': 'AKIA4MEMOS3N5TEAOE3J',
            's3_secret_key': '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',
        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get_setting(self, section, option):
        try:
            value = self.config.get(section, option)
            return value.split(';')[0].strip()
        except configparser.NoOptionError:
            raise ValueError(f"Option '{option}' not found in section '{section}'")

    def set_setting(self, section, option, value):
        self.config.set(section, option, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
