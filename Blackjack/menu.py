from player import Player
from deck import BuildDeck, Deck
from game import Blackjack
from accounts import Account
from sys import exit
from time import sleep
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
            2: self._info,
            3: self._sign_out,
            4: self._delete_account,
            5: self._quit
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
                choice = self._menu_choice(1, 5)

                system('cls||clear')
                action = self.game_options[choice]
                action()

                if choice == 3 or choice == 4:
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
        print("\nThank you for playing Blackjack!")
        
        if self.quit_without_save == False:
            Account().save(self.player)
        
        sleep(0.5)
        exit(0)


    def _play(self):
        while True:
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

        if self.BJ.play():
            print("\nYou win.")
        else:
            print("\nYou lose.")


    def _info(self):
        self.player.print()


    def _sign_out(self):
        Account().save(self.player)


    def _delete_account(self):
        self.quit_without_save = True
        Account().delete(self.player.username)

    


Menu().run()