from user_tree import UserTree
from player import Player
import pickle


class Registration:
    def create_registration(self):
        username, age, password = self.__user_details()
        new_user = Player(username, age, password)
        
        users_file = open("users.bin", "rb")
        us_tree: UserTree()
        us_tree = pickle.load(users_file)
        users_file.close()

        us_tree.add(new_user)

        users_file = open("users.bin", "wb")
        pickle.dump(us_tree, users_file)
        users_file.close()

        return new_user


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
                    raise ValueError("You are too young/old.")
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
                print("Please, enter password with length between 8 and 15 symbols.")
                continue
            except ValueError:
                print("Please, enter password, which contains least 2 big and 2 small letters.")
                continue
            else:
                break

        return username, age, password
