from lib.dataobject import DataObject

class AppSettings(DataObject):

    def __init__(self):
        self.DefaultSaveLocation = None
        self.CurrentProfileID = None
        self.Profiles = []