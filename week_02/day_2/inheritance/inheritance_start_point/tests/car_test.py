import unittest

from classes.car import Car
from classes.engine import Engine

class TestCar(unittest.TestCase):

    def setUp(self):
        engine = Engine()
        self.car = Car(engine)

    def test_car_can_start_engine(self):
        self.assertEqual("Vrrmmm", self.car.engine.start_engine())
