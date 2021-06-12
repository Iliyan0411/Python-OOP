class Player:
    def __init__(self, name, age, wins, games):
        self.name = name
        self.age = age
        self.wins = wins
        self.games = games
        self.win_coef = wins / games
        self.points = 0

    def print(self):
        print("{0}~\t~{1}~\t~{2}~\t~{3}".format(self.name, self.age, self.games, self.wins))
        print("Win coefficient: {0}".format(self.win_coef))