from models.appsettings import AppSettings
from lib.util import *
from os import path

class SettingsManager:

    def __init__(self, app):
        self.app = app
        self.settings = None

    def load(self):
        self.settings = AppSettings()
        self.settings.load_from(path.join(get_app_data_folder(), "AppSettings.json"))

    def save(self):
        self.settings.dump_to(path.join(data_folder(get_app_data_folder), "AppSettings.json"))