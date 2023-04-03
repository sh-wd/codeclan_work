import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Summer Holiday", "Cliff Richard")
        self.guest1 = Guest("Steve", 50, self.song1)

    def test_guest_has_name(self):
        expected_value = "Steve"
        actual_value = self.guest1.name
        self.assertEqual(expected_value, actual_value)

    def test_guest_has_fav_song(self):
        expected_value = self.song1
        actual_value = self.guest1.fav_song
        self.assertEqual(expected_value, actual_value)
