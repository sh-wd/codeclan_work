class Customer:
    def __init__(self, name, wallet, age, drunk_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunk_level

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def increase_drunk_level(self, drink):
        self.drunkenness += drink

    def decrease_drunk_level(self, rejuvination_level):
        self.drunkenness -= rejuvination_level

    # def buy_drink(self, customer, drink):
    #     drink_to_sell = self.find_drink_by_name(drink)
    #     customer.decrease_wallet(drink_to_sell.price)
    #     self.increase_till(drink_to_sell.price)