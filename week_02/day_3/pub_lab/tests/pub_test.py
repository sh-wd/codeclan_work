import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Beer", 5, 2)
        self.drink2 = Drink("Guinness", 5, 3)

        self.stock = {
            self.drink1: 3,
            self.drink2: 5
        }
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.stock = self.stock
        self.customer = Customer("Maggie May", 50.00, 21, 8)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_can_find_drink_by_name(self):
        beer = Drink("beer", 5.50, 4.5)
        self.pub.add_drink_to_stock(beer)
        drink = self.pub.find_drink_by_name("beer")
        self.assertEqual("beer", drink.name)

    def test_pub_has_drinks(self):
        beer = Drink("beer", 5.50, 4.5) 
        self.pub.add_drink_to_stock(beer)
        self.assertEqual(1, len(self.pub.drinks))

    def test_till_has_increased(self):
        self.pub.increase_till(5.50)
        self.assertEqual(105.50, self.pub.till)

    def test_cut_off_level(self):
        self.assertEqual("Too drunk", self.pub.is_customer_drunk(self.customer))
        

