class Person:
    def __init__(self, name, no_of_kills):
        self.name = name
        self.no_of_kills = no_of_kills

    def add_kill(self):
        self.no_of_kills += 1