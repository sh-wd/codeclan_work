class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []

    def reduce_cash(self, amount_to_reduce):
        self.cash -= amount_to_reduce

    def pet_count(self):
        return len(self.pets)
    
    def add_pet(self, pet):
        self.pets.append(pet)

    def get_total_value_of_pets(self):
        running_total = 0

        for pet in self.pets:
            running_total += pet.price
        return running_total