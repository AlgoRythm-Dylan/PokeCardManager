from lib.command import Command

class ProfileCommand(Command):

    def __init__(self, app):
        super().__init__(app)
        self.primary_command = "profile"
        self.description = "Profile manager command"

    def execute(self, args):
        app_args = args[1:]
        if len(app_args) == 0:
            self.output("Available commands: \n> list")
            return
        if app_args[0].lower() == "list":
            self.output(f"You have {len(self.app.profile_manager)} profiles available")

def import_to(command_manager):
    command_manager.add_command(ProfileCommand(command_manager.app))