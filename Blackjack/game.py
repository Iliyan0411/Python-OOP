from deck import Deck
from time import sleep


class Blackjack:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.draw_count = 0


    def _make_choice(self):
        while True:
            try:
                choice = int(input("$ "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except ValueError:
                print("# Invalid choice.")
            except TypeError:
                print("# Invalid input")
            else:
                return choice


    def play(self):
        player_points, dealer_points = 0, 0

        print("# [1] Draw card")
        print("# [2] Stop draw")

        while True:
            choice = self._make_choice()

            if choice == 1:
                card = self.deck.draw()
                
                self.draw_count += 1
                if self.draw_count > len(self.deck.cards) - 20:
                    self.deck.stir()
                    self.draw_count = 0
                
                if card.kind == 12 and card.value + player_points > 21:
                    player_points += 1
                else:
                    player_points += card.value

                card.print()
                print("  -->  {0}".format(player_points))

                if player_points > 21:
                    player_points = 0
                    return False
                if player_points == 21:
                    player_points = 0
                    return True
            else:
                break

        while dealer_points < player_points:
            card = self.deck.draw()
            sleep(0.5)
            
            self.draw_count += 1
            if self.draw_count > len(self.deck.cards) - 20:
                self.deck.stir()
                self.draw_count = 0

            if card.kind == 12 and card.value + dealer_points > 21:
                dealer_points += 1
            else:
                dealer_points += card.value

            card.print()
            print("  -->  {0}".format(dealer_points))

            if dealer_points > 21:
                return True
            if dealer_points > player_points:
                return False


        return player_points > dealer_points
