from card import Card
import random


class Deck:
    def __init__(self, cards, deck_id="Custom"):
        self.cards = cards
        self.deck_id = deck_id


    def draw(self):
        card = self.cards[0]
        self.cards.append(self.cards.pop(0))
        return card


    def swap(self, pos_1, pos_2):
        self.cards[pos_1], self.cards[pos_2] = self.cards[pos_2], self.cards[pos_1]


    def suit_count(self, suit):
        counter = 0
        for card in self.cards:
            if card.suit == suit:
                counter += 1
        return counter


    def rank_count(self, value):
        counter = 0
        for card in self.cards:
            if card.value == value:
                counter += 1
        return counter

    
    def stir(self):
        bottom = len(self.cards)
        for _ in range(17):
            pos_1 = int(random.random()*bottom)
            pos_2 = int(random.random()*bottom)

            if pos_1 != pos_2:
                self.swap(pos_1, pos_2)

###########################################################

class BuildDeck:
    def create_deck(self, default: bool, deck_id="Custom", size=52):
        deck = []

        if default:
            deck = self.__default_deck("Default")
        else:
            remaining = size % 52
            def_decks = int(size / 52)

            for _ in range(def_decks):
                deck += self.__default_deck(deck_id)

            deck += self.__spec_deck(deck_id, remaining) 

        return deck


    def __default_deck(self, deck_id="Custom"):
        id = self.__generate_id(deck_id)
        curr = 0
        deck = []

        for i in range(13):
            power = 0
            
            if i + 2 <= 10:
                power = i + 2
            elif i != 12:
                power = 10
            else:
                power = 11

            deck += Card(0, power, id[curr]))
            deck += Card(1, power, id[curr+1]))
            deck += Card(2, power, id[curr+2]))
            deck += Card(3, power, id[curr+3]))
            curr += 4

        return deck


    def __spec_deck(self, deck_id, size):
        id = self.__generate_id(deck_id, size)
        deck = []
        added = {}

        i = 0
        while i < size:
            power = int(random.random()*10 + 2)
            suit = int(random.random()*4)

            if not (suit, power) in added:
                deck += Card(suit, power, id[i]))
                i += 1
                added[(suit, power)] = None

        return deck


    def __generate_id(self, prefix, size=52):
        id = [prefix for _ in range(size)]
        length = 15 - len(prefix)

        for i in range(size):
            for j in range(length):
                id[i] += chr(int(random.random()*26 + 97))

        return id
