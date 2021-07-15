
class Player:
    def __init__(self, username, age, password):
        self.username = username
        self.age = age
        self.wins = 0
        self.password = password
        self.games = 0
        self.money_balance = 0


    def payment(self):
        while True:
            try:
                payment = int(input("Payment: "))
                if payment <= 0:
                    raise ValueError
            except ValueError:
                print("Enter valid payment bigger than zero.")
            except TypeError:
                print("Your payment must be integer.")
            except Exception:
                print("Something went wrong.")
            else:
                self.money_balance += payment
                break


    def print(self):
        print("\nUsername: {}".format(self.username))
        print("Age: {}".format(self.age))
        print("Money balance: {}".format(self.money_balance))
        print("Games: {}".format(self.games))
        print("Wins: {}".format(self.wins))
        