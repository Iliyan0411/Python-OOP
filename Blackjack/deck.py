from card import Card
from random import random


class Deck:
    def __init__(self, cards):
        self.cards = cards


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
        stirs = int(len(self.cards))
        bottom = len(self.cards)
        
        for _ in range(stirs):
            pos_1 = int(random()*bottom)
            pos_2 = int(random()*bottom)

            if pos_1 != pos_2:
                self.swap(pos_1, pos_2)

###########################################################

class BuildDeck:
    def create_deck(self, decks=1):
        deck = []
        for _ in range(decks):
            deck += self._default_deck() 

        return deck


    def _default_deck(self):
        deck = []

        for i in range(13):
            power = 0
            
            if i + 2 <= 10:
                power = i + 2
            elif i != 12:
                power = 10
            else:
                power = 11

            for j in range(4):
                deck.append(Card(i, j, power))

        return deck
