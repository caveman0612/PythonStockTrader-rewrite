

class Companies():
    def __init__(self, name, ticker, TargetPrice):
        self.name = name
        self.ticker = ticker
        self.TargetPrice = TargetPrice

    def __str__(self):
        return f"Sell {self.name} when the price gets to {self.TargetPrice}"




