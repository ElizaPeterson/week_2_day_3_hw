class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
        
    def buy_a_drink(self, price):
        self.wallet -= price

    def check_drunkenness(self, drunkenness):
        return self.drunkenness

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
