from user_tree import UserTree
from player import Player
from os import path
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
            except Exception:
                print("Something went wrong.")
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
            except Exception:
                print("Something went wrong.")
            else:
                return password



class Registration(Verification):
    def make_registration(self):
        username = super()._username_input()
        age = self._age_input()
        password = None

        while True:
            password = super()._password_input()

            if self._secured_password(password):
                break

        new_user = Player(username, age, password)
        
        user_tree = None
        if path.getsize("users.bin") == 0:
            user_tree = UserTree()
        else:
            users_file = open("users.bin", "rb")
            user_tree = pickle.load(users_file)
            users_file.close()

        user_tree.add(new_user)

        users_file = open("users.bin", "wb")
        pickle.dump(user_tree, users_file)
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
            except Exception:
                print("Something went wrong.")
            else:
                return age


class SignIn(Verification):
    def make_sign_in(self):
        users_file = open("users.bin", "rb")
        us_tree = pickle.load(users_file)
        users_file.close()

        while True:
            try:
                username = super()._username_input()
                password = super()._password_input()

                located = us_tree.exist(username, password)
                if located == False:
                    raise ValueError
            except ValueError:
                print("Please, enter correct username and password.")
            except Exception:
                print("Something went wrong.")
            else:
                return us_tree.locate(username)


class Account(Registration, SignIn):
    def delete(self, username):
        users_file = open("users.bin", "rb")
        users_tree = pickle.load(users_file)
        users_file.close()

        users_tree.remove(username)

        users_file = open("users.bin", "wb")
        pickle.dump(users_tree, users_file)
        users_file.close()


    def save(self, user):
        users_file = open("users.bin", "rb")
        users_tree = pickle.load(users_file)
        users_file.close()

        users_tree.save(user)

        users_file = open("users.bin", "wb")
        pickle.dump(users_tree, users_file)
        users_file.close()
    