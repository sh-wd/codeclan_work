class Floor:
    def __init__(self, floor_number):
        self.people = []
        self.floor_number = floor_number


    def floor_count(self):
        return len(self.people)

