from user_tree import UserTree
from player import Player
import pickle


class Verification:
    def _username_input(self):
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
                return username

    
    def _password_input(self):
        while True:
            try:
                password = input("Enter password: ")
                if len(password) < 8 or len(password) > 15:
                    raise OverflowError("Wrong length of password.")
            except OverflowError:
                print("Please, enter password with length between 8 and 15 symbols.")
                continue
            except Exception:
                print("Something went wrong.")
                continue
            else:
                return password



class Registration(Verification):
    def create_registration(self):
        username = super()._username_input()
        age = self._age_input()
        password = None

        while True:
            password = super()._password_input()

            if not self._secured_password(password):
                continue
            else:
                break

        new_user = Player(username, age, password)
        
        users_file = open("users.bin", "rb")
        us_tree = pickle.load(users_file)
        users_file.close()

        us_tree.add(new_user)

        users_file = open("users.bin", "wb")
        pickle.dump(us_tree, users_file)
        users_file.close()

        return new_user


    def _secured_password(self, password):
        bigch, smallch = 0, 0
        for c in password:
            if ord(c) >= 65 and ord(c) <= 90:
                bigch += 1
            if ord(c) >= 97 and ord(c) <= 122:
                smallch += 1
        
        return bigch >= 2 and smallch >= 2
        

    def _age_input(self):
        while True:
            try:
                age = int(input("Age: "))
                if age < 18 or age > 90:
                    raise ValueError("You are too young/old.")
            except ValueError:
                print("Please, enter valid age.")
                continue
            except Exception:
                print("Something went wrong.")
                continue
            else:
                return age


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WrongUsername(Exception):
    pass
class WrongPassword(Exception):
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SignIn(Verification):
    def make_sign_in(self):

        users_file = open("users.bin", "rb")
        us_tree = pickle.load(users_file)
        users_file.close()

        while True:
            try:
                username = super()._username_input()
                password = super()._password_input()

                corr_usr, corr_pwd = us_tree.exist(username, password)
                if corr_usr == False:
                    raise WrongUsername("Wrong username.")
                if corr_pwd == False:
                    raise WrongPassword("Wrong password.")
            except WrongUsername:
                print("Please, enter correct username.")
                continue
            except WrongPassword:
                print("Please, enter correct password.")
                continue
            else:
                break

        
        user = us_tree.locate(username)
        return user
