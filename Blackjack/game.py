from player import Player
from deck import Deck, BuildDeck
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
        print("# [1] Draw card")
        print("# [2] Stop draw")

        while True:
            choice = self.__make_choice()

            if choice == 1:
                card = self.deck.draw()
                
                self.draw_count += 1
                if self.draw_count > 30:
                    self.deck.stir()
                    self.draw_count = 0
                
                if card.suit == 12 and card.value + self.player.points > 21:
                    self.player.points += 1
                else:
                    self.player.points += card.value

                print(self.player.points)

                if self.player.points > 21:
                    return False
            else:
                break

        dealer_points = 0
        while dealer_points < 17:
            card = self.deck.draw()
            
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

        print(dealer_points)
        return self.player.points >= dealer_points



###############################################
# deck_creator = BuildDeck()
# my_deck = deck_creator.create_deck(True)
# deck = Deck(my_deck)
# deck.stir()


# BJ = Blackjack(Player("Iliyan", 20, 2, 5), deck)
# result = BJ.action()

# if result:
#     print("You win!")
# else:
#     print("You lose!")