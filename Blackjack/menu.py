from player import Player
from deck import BuildDeck, Deck
from game import Blackjack
from accounts import Account
from sys import exit
from time import sleep


class Menu:
    def __init__(self):
        self.BJ = Blackjack(None, None)

        self.login_options = {
            1: self._registration,
            2: self._sign_in,
            3: self._quit
        }
        self.game_options = {
            1: self._play,
            2: self._info,
            4: self._delete_account,
            5: self._quit
        }


    def run(self):
        print("Welcome to Console-Blackjack-21.\n")

        while True:
            self._start_menu()
            choice = self._menu_choice(1, 3)

            action = self.login_options[choice]
            action()

            while True:
                self._game_menu()
                choice = self._menu_choice(1, 5)

                if choice == 3:
                    Account.save()
                    break

                action = self.game_options[choice]
                action()


    def _start_menu(self):
        print("""
        1. Register
        2. Sign in
        3. Quit
        """)


    def _game_menu(self):
        print("""
        1. Play
        2. Account information
        3. Sign out
        4. Delete account
        5. Quit
        """)


    def _menu_choice(self, min, max):
        while True:
            try:
                choice = int(input("$ "))

                if choice < min or choice > max:
                    raise ValueError
                if not isinstance(int, choice):
                    raise TypeError
            except ValueError:
                print("Your choice must be between {0} and {1}.".format(min, max))
            except TypeError:
                print("Your choice must be an integer.")
            except Exception:
                print("Something went wrong.")
            else:
                return choice


    def _quit(self):
        print("Thank you for playing Blackjack!")
        Account.save()
        sleep(1)
        exit(0)


    def _info(self):
        self.BJ.player.print()

    
    def _play(self):
        while True:
            try:
                deck_num = int(input("Select number of decks[1-6]: "))
                if deck_num < 1 or deck_num > 6:
                    raise ValueError("Invalid number of decks.")
            except ValueError:
                print("Numbers of decks must be between 1 and 6.")
            except Exception:
                print("Something went wrong.")
            else:
                self.BJ.deck = BuildDeck().create_deck(deck_num)
                break

        self.BJ.action()


    def _registration(self):
        self.BJ.player = Account().make_registration()


    def _delete_account(self):
        Account().delete(self.BJ.player.username)

    
    def _sign_in(self):
        self.BJ.player = Account().make_sign_in()
