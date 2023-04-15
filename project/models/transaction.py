class Transaction:
    def __init__(self, cost, merchant, tag, id = None):
        self.cost = cost
        self.merchant = merchant
        self.tag = tag
        self.id = id