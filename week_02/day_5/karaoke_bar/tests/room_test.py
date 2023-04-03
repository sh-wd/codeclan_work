import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(50, 10)

    def test_room_has_a_fee(self):
        expected_value = 50
        actual_value = self.room1.fee 
        self.assertEqual(expected_value, actual_value)

    def test_room_has_a_capacity(self):
        expected_value = 10
        actual_value = self.room1.capacity
        self.assertEqual(expected_value, actual_value)