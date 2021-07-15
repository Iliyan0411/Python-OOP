from player import Player
from deck import BuildDeck, Deck
from game import Blackjack
from accounts import Account
from sys import exit
from os import system


class Menu:
    def __init__(self):
        self.BJ = Blackjack(None)
        self.player = Player(None, None, None)
        self.quit_without_save = False

        self.login_options = {
            1: self._registration,
            2: self._sign_in,
            3: self._quit
        }
        self.game_options = {
            1: self._play,
            2: self._payment,
            3: self._info,
            4: self._sign_out,
            5: self._delete_account,
            6: self._quit
        }


    def run(self):
        print("\n\t\t\t| Welcome to Console-Blackjack-21. |\n")

        while True:
            self._start_menu()
            choice = self._menu_choice(1, 3)

            system('cls||clear')
            action = self.login_options[choice]
            action()

            while True:
                self._game_menu()
                choice = self._menu_choice(1, 6)

                system('cls||clear')
                action = self.game_options[choice]
                action()

                if choice == 4 or choice == 5:
                    break


    def _start_menu(self):
        print("""
        1. Register
        2. Sign in
        3. Quit
        """)


    def _game_menu(self):
        print("""
        1. Play
        2. Make payment
        3. Account information
        4. Sign out
        5. Delete account
        6. Quit
        """)


    def _menu_choice(self, min, max):
        while True:
            try:
                choice = int(input("$ "))

                if choice < min or choice > max:
                    raise ValueError
            except ValueError:
                print("Your choice must be between {0} and {1}.".format(min, max))
            except Exception:
                print("Something went wrong.")
            else:
                return choice


    def _registration(self):
        self.quit_without_save = False
        self.player = Account().make_registration()


    def _sign_in(self):
        self.quit_without_save = False
        self.player = Account().make_sign_in()


    def _quit(self):
        print("\nThank you for playing Blackjack!\n")
        
        if self.quit_without_save == False:
            Account().save(self.player)
        
        exit(0)


    def _play(self):
        while self.player.money_balance < self.BJ.bet:
            self._payment()

        if self.BJ.deck == None:
            while True:
                try:
                    self.BJ.bet = int(input("Make your bet per distribution: "))
                    if self.BJ.bet <= 0 or self.BJ.bet > self.player.money_balance:
                        raise ValueError
                except ValueError:
                    print("Enter valid bet.")
                    continue
                except TypeError:
                    print("Your bet must be integer.")
                    continue
                except Exception:
                    print("Something went wrong.")
                    continue

                try:
                    deck_num = int(input("Select number of decks[1-6]: "))
                    if deck_num < 1 or deck_num > 6:
                        raise ValueError
                except ValueError:
                    print("Numbers of decks must be between 1 and 6.")
                except Exception:
                    print("Something went wrong.")
                else:
                    self.BJ.deck = Deck(BuildDeck().create_deck(deck_num))
                    self.BJ.deck.stir()
                    break

        self.player.games += 1
        if self.BJ.play():
            self.player.wins += 1
            self.player.money_balance += self.BJ.bet
            print("\nYou win.")
        else:
            self.player.money_balance -= self.BJ.bet
            if self.player.money_balance < 0:
                self.player.money_balance = 0
            print("\nYou lose.")


    def _payment(self):
        self.player.payment()


    def _info(self):
        self.player.print()


    def _sign_out(self):
        Account().save(self.player)
        self.BJ.restart()


    def _delete_account(self):
        self.quit_without_save = True
        Account().delete(self.player.username)
        self.BJ.restart()

    

Menu().run()