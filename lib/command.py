class Command:

    def __init__(self, app):
        self.app = app

        self.description = "<Default command description>"
        self.usage = "<Default command usage>"
        self.help = None

        self.primary_command = None
        self.aliases = []

        self.other_info = {}

    def execute(self, args):
        pass

    def output(self, message):
        self.app.output(message)