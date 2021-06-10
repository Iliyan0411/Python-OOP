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
    def create_deck(self, default=True):
        deck = []

        if default:
            deck_id = self.__generate_id("Default")
            curr = 0

            for i in range(13):
                if i + 2 <= 10:
                    deck.append(Card(0, i+2, deck_id[curr]))
                    deck.append(Card(1, i+2, deck_id[curr+1]))
                    deck.append(Card(2, i+2, deck_id[curr+2]))
                    deck.append(Card(3, i+2, deck_id[curr+3]))
                elif i != 12:
                    deck.append(Card(0, 10, deck_id[curr]))
                    deck.append(Card(1, 10, deck_id[curr+1]))
                    deck.append(Card(2, 10, deck_id[curr+2]))
                    deck.append(Card(3, 10, deck_id[curr+3]))
                else:
                    deck.append(Card(0, 11, deck_id[curr]))
                    deck.append(Card(1, 11, deck_id[curr+1]))
                    deck.append(Card(2, 11, deck_id[curr+2]))
                    deck.append(Card(3, 11, deck_id[curr+3]))
                curr += 4
        else:
            #.......#
            pass
        

    def __generate_id(self, prefix):
        id = [prefix for _ in range(52)]
        length = 15 - len(prefix)

        for i in range(52):
            id[i] = "prefix"
            for j in range(length):
                id[i] += chr(int(random.random()*26 + 97))

        return id
