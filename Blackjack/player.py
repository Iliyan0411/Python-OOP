class Player:
    def __init__(self, username, age, wins, games):
        self.username = username
        self.age = age
        self.wins = wins
        self.games = games
        self.points = 0

    def print(self):
        print("{0}~\t~{1}~\t~{2}~\t~{3}".format(self.username, self.age, self.games, self.wins))