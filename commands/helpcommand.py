from lib.command import Command

class HelpCommand(Command):

    def __init__(self, app):
        super().__init__(app)
        self.description = "The help command"
        self.primary_command = "help"
        self.usage = "> help\n> help <command?>"
        self.aliases = ["?"]

    def execute(self, args):
        if len(args) == 1:
            self.do_default_help()
            return

        command_name = args[1].lower()
        command = self.app.command_manager.find_command(command_name)
        if command == None:
            self.app.output(f"Could not find command \"{command_name}\"")
            return
        self.app.output(f"Help for command \"{command_name}\":\n")
        if command.description != None:
            self.app.output(f"Description: {command.description}")
        if command.usage != None:
            self.app.output(f"Usage:\n{command.usage}")
        self.app.output(f"Primary command: {command.primary_command}")
        if len(command.aliases) > 0:
            self.app.output(f"Aliases: {', '.join(command.aliases)}")

    def do_default_help(self):
        self.app.output("== Help & Info ==")
        self.app.output("PokeCardManager, or PCM, allows you to manage " +
                        "notable cards in your Pokemon deck\n")
        self.app.output("This help command can be run with the name of " +
                        "another command to get info about that command.\n" +
                        "Since you ran this command without arguments, " +
                        "you will get generic application information\n")
        self.app.output("Commands available to you: \n")
        for command in self.app.command_manager.commands:
            self.app.output(f"> {command.primary_command} ({command.description})")

def import_to(command_manager):
    command_manager.add_command(HelpCommand(command_manager.app))