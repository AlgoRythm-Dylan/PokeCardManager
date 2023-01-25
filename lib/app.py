from lib.settingsmanager import SettingsManager
from lib.commandmanager import CommandManager
from lib.profilemanager import ProfileManager

class PCMApp:

    def __init__(self):
        self.settings_manager = SettingsManager(self)
        self.command_manager = CommandManager(self)
        self.profile_manager = ProfileManager(self)
        self.args = None
        self.silenced = False

    def start(self, args):
        self.args = args
        self.settings_manager.load()
        self.profile_manager.load()    
        self.command_manager.discover()
        self.command_manager.execute(args)

    def output(self, message):
        if not self.silenced:
            print(message)

    def save(self):
        self.settings_manager.save()