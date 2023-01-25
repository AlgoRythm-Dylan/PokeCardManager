from lib.dataobject import DataObject

CARD_TYPE = {
    "Trainer": "T",
    "Pokemon": "P",
    "Stadium": "S"
}

class Card(DataObject):

    def __init__(self):
        self.Name = None
        self.CardType = None