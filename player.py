class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.full = self.name + "(" + self.symbol + ")"
