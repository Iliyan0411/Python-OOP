from player import Player
from deck import BuildDeck, Deck
from game import Blackjack
from accounts import Registration, SignIn, DeleteAccount
from sys import exit
from time import sleep


class Menu:
    def __init__(self):
        self.BJ = Blackjack(None, None)

        self.login_options = {
            1: self.registration,
            2: self.sign_in,
            3: self.quit
        }
        self.game_options = {
            1: self.play,
            2: self.info,
            3: self.delete_account,
            4: self.quit
        }


    def start_menu(self):
        print("""
        1. Register
        2. Sign in
        3. Quit
        """)


    def game_menu(self):
        print("""
        1. Play
        2. Account information
        3. Sign out
        4. Delete account
        5. Quit
        """)


    def quit(self):
        print("Thank you for playing Blackjack!")
        sleep(1)
        exit(0)


    def info(self):
        self.BJ.player.print()

    
    def play(self):
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


    def registration(self):
        self.BJ.player = Registration().create_registration()


    def delete_account(self):
        DeleteAccount().delete_acc(self.BJ.player.username)

    
    def sign_in(self):
        self.BJ.player = SignIn().make_sign_in()
