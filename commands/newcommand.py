from lib.command import Command

class NewCommand(Command):

    def __init__(self, app):
        super().__init__(app)
        self.primary_command = "new"
        self.description = "\"New\" command - create new objects such as profiles"

def import_to(command_manager):
    command_manager.add_command(NewCommand(command_manager.app))