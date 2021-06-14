from game import Blackjack
from deck import BuildDeck
from player import Player
from sys import exit
from time import sleep


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
        sleep(2)
        exit(0)


    def info(self):
        self.BJ.player.print()

    
    def play(self):
        self.BJ.action()


    def __secured_password(self, password):
        bigch, smallch = 0, 0
        for c in password:
            if ord(c) >= 65 and ord(c) <= 90:
                bigch += 1
            if ord(c) >= 97 and ord(c) <= 122:
                smallch += 1
        
        return bigch >= 2 and smallch >= 2


    def __user_details(self):
        username, age, password = None, None, None

        while True:
            try:
                username = input("Username: ")
                if len(username) > 15:
                    raise ValueError("Too long username.")
            except ValueError:
                print("Please, enter shorter username.")
                continue
            except Exception:
                print("Something went wrong.")
                continue
            else:
                break
        
        while True:
            try:
                age = int(input("Age: "))
                if age < 18 or age > 90:
                    raise ValueError("You are too young or too old.")
            except ValueError:
                print("Please, enter valid age.")
                continue
            except Exception:
                print("Something went wrong.")
                continue
            else:
                break

        while True:
            try:
                password = input("Enter password: ")
                if len(password) < 8 or len(password) > 15:
                    raise OverflowError("Wrong length of password.")
                if not self.__secured_password(password):
                    raise ValueError("Your password is not secured.")
            except OverflowError:
                print("Please, enter password with correct length.")
                continue
            except ValueError:
                print("Please, enter password, which contains Big and small characters.")
                continue
            else:
                break

        return username, age, password


    def __create_userfile(self, username, password):
        try:
            users = open("users.txt", "a")
        except Exception:
            print("Problem with <users.txt>.")
            exit(-1)

        users.write("{0} {1}".format(username, password))

        users.close()


    def register(self):
        username, age, password = self.__user_details()
        self.__create_userfile(username, password)

        