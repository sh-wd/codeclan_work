class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}

    def add_drink_to_stock(self, drink):
        self.drinks.update({drink})

    def increase_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
            
  
    def is_customer_drunk(self, customer):
        if customer.drunkenness >= 6:
            return "Too drunk"
        
 