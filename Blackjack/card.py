class Card:
    def __init__(self, kind: int, suit: int, value: int):
        self.kind = kind
        self.suit = suit
        self.value = value


    def print(self):
        if self.kind < 9:
            print(self.kind+2, end="")
        elif self.kind == 9:
            print("J", end="")
        elif self.kind == 10:
            print("Q", end="")
        elif self.kind == 11:
            print("K", end="")
        else:
            print("A", end="")

        if self.suit == 0:
            print("\u2660")
        elif self.suit == 1:
            print("\u2661")
        elif self.suit == 2:
            print("\u2662")
        elif self.suit == 3:
            print("\u2663")
