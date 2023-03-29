import unittest
from src.floor import Floor
from src.person import Person

class TestFloor(unittest.TestCase):
    def setUp(self):
        self.floor = Floor(1)
        self.bad_guy1 = Person("German Guy")
        self.bad_guy2 = Person("German Guy")
        

    def test_floor_starts_empty(self):
        population = self.floor.floor_count()
        self.assertEqual(0, population)


    @unittest.skip("Delete this line to run the test")
    def test_bad_guys_can_be_added_to_floor(self):
        self.floor.add_person(self.bad_guy1)
        self.assertEqual(1, len(self.floor.people))


    @unittest.skip("Delete this line to run the test")
    def test_bad_guys_can_be_removed_from_floor(self):
        self.floor.add_person(self.bad_guy1)
        self.floor.add_person(self.bad_guy2)
        self.floor.remove_person(self.bad_guy2)
        self.assertEqual(1, len(self.floor.people))


