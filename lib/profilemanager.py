class ProfileManager:

    def __init__(self, app):
        self.app = app

    def load(self):
        pass

    def __len__(self):
        return len(self.app.settings_manager.settings.Profiles)

    def new_profile_input(self):
        input("Profile Name: ")