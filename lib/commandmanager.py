import importlib
import commands
from lib.util import get_py_module_names

class CommandManager:

    def __init__(self, app):
        self.app = app
        self.commands = []

    def discover(self):
        module_names = get_py_module_names(commands)
        for module_name in module_names:
            module = importlib.import_module(f"commands.{module_name}")
            module.import_to(self)

    def add_command(self, command):
        self.commands.append(command)
    
    def find_command(self, name):
        for command in self.commands:
            if command.primary_command == name:
                return command
        for command in self.commands:
            if name in command.aliases:
                return command
        return None

    def execute(self, argv):
        app_args = argv[1:] # Cut off system-provided arg
        if len(app_args) == 0:
            self.app.output("Required argument: <command>. Try \"pcm help\"")
            return
        command_name = app_args[0].lower()
        command = self.find_command(command_name)
        if command == None:
            self.app.output(f"Could not find command \"{command_name}\"")
        else:
            command.execute(app_args)