class Card:
    def __init__(self, suit: int, value: int, card_id: str):
        self.suit = suit
        self.value = value
        self.card_id = card_id

    def print(self):
        print("({}, {}, {})".format(self.suit, self.value, self.card_id))