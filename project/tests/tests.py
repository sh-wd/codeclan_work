import unittest

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
from models.user import User

class Test(unittest.TestCase):

    def setUp(self):
        self.user = User("Kermit the Frog")
        self.transaction = Transaction(13.99, "Miss Piggy iPlayer", "Entertainment")
        self.tag = Tag("Personal Care")
        self.merchant = Merchant("Rizzo Gyms")
    
    def test_user_has_name(self):
        self.assertEqual("Kermit the Frog", self.user.name)

    def test_transaction_has_cost(self):
        self.assertEqual(13.99, self.transaction.cost)

    def test_transaction_has_merchant(self):
        self.assertEqual("Miss Piggy iPlayer", self.transaction.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual("Entertainment", self.transaction.tag)

    def test_tag_has_name(self):
        self.assertEqual("Personal Care", self.tag.name)

    def test_merchant_has_name(self):
        self.assertEqual("Rizzo Gyms", self.merchant.name)