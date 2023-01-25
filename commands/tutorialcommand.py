from lib.command import Command

class TutorialCommand(Command):

    def __init__(self, app):
        super().__init__(app)
        self.primary_command = "tutorial"
        self.description = "Type \"pcm tutorial\" to learn how to use PCM!"

def import_to(command_manager):
    command_manager.add_command(TutorialCommand(command_manager.app))