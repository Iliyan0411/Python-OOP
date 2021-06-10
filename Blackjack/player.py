class Player:
    def __init__(self, name, age, wins, games):
        self.name = name
        self.age = age
        self.wins = wins
        self.games = games
        self.win_coef = wins / games
        self.points = 0    