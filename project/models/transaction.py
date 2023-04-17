class Transaction:
    def __init__(self, cost, merchant, tag, user, id = None):
        self.cost = cost
        self.merchant = merchant
        self.tag = tag
        self.user = user
        self.id = id