from game import Blackjack
from deck import BuildDeck
import sys
import time


class Menu:
    def __init__(self):
        self.BJ = Blackjack(None, None)

        self.login_options = {
            1: self.register,
            2: self.sign_in,
            3: self.quit
        }
        self.game_options = {
            1: self.play,
            2: self.info,
            3: self.sign_out,
            4: self.delete_account,
            5: self.quit
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
        time.sleep(2)
        sys.exit(0)


    def info(self):
        self.BJ.player.print()

    
    def play(self):
        self.BJ.action()


    