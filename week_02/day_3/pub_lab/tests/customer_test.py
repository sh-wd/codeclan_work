import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Maggie May", 50.00, 21, 8)
    

    def test_customer_has_name(self):
        self.assertEqual("Maggie May", self.customer.name)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_customer_has_cash(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_customer_drunkenness(self):
        self.assertEqual(8, self.customer.drunkenness)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(5.50)
        self.assertEqual(44.50, self.customer.wallet)

    def test_customer_drunkeness_increase(self):
        self.customer.increase_drunk_level(1)
        self.assertEqual(9, self.customer.drunkenness)

    def test_decrease_drunkenness(self):
        self.customer.decrease_drunk_level(2)
        self.assertEqual(6, self.customer.drunkenness)


        # customer = Customer("Maggie May", 50.00)

        # self.assertEqual(44.50, customer.wallet)
