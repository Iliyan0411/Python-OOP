
class Player:
    def __init__(self, username, age, password):
        self.username = username
        self.age = age
        self.wins = 0
        self.password = password
        self.games = 0
        self.points = 0


    def print(self):
        print("\nUsername: {}".format(self.username))
        print("Age: {}".format(self.age))
        print("Games: {}".format(self.games))
        print("Wins: {}".format(self.wins))
        