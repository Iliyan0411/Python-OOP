from player import Player
from deck import Deck
from card import Card


class Blackjack:
    def __init__(self, player: Player, deck: Deck):
        self.player = player
        self.deck = deck
        self.draw_count = 0


    def __make_choice(self):
        while True:
            try:
                choice = int(input("$ "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except ValueError:
                print("# Invalid choice.")
                continue
            except TypeError:
                print("# Invalid input")
                continue
            else:
                return choice


    def action(self):
        while True:
            print("# [1] Draw card")
            print("# [2] Stop draw")
            choice = self.__make_choice()

            if choice == 1:
                card = Card(self.deck.draw())
                
                self.draw_count += 1
                if self.draw_count > 30:
                    self.deck.stir()
                    self.draw_count = 0
                
                if card.suit == 12 and card.value + self.player.points > 21:
                    self.player.points += 1
                else:
                    self.player.points += card.value
                        
                if self.player.points > 21:
                    return False
            else:
                break

        dealer_points = 0
        while dealer_points < 17:
            card = Card(self.deck.draw())
            
            self.draw_count += 1
            if self.draw_count > 30:
                    self.deck.stir()
                    self.draw_count = 0

            if card.suit == 12 and card.value + dealer_points > 21:
                    dealer_points += 1
            else:
                dealer_points += card.value
                        
            if dealer_points > 21:
                return True

        return self.player.points >= dealer_points, dealer_points
