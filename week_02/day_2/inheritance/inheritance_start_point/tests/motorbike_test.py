import unittest

from classes.motorbike import Motorbike
from classes.engine import Engine

class TestMotorbike(unittest.TestCase):

    def setUp(self):
        engine = Engine()
        self.motorbike = Motorbike(engine)

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrmmm", self.motorbike.engine.start_engine())
