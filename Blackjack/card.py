class Card:
    def __init__(self, suit: int, value: int):
        self.suit = suit
        self.value = value


    def print(self):
        print("({}, {})".format(self.suit, self.value))