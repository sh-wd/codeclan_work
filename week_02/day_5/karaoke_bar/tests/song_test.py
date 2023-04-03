import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Summer Holiday", "Cliff Richard")
        self.songs = []
        
    def test_song_has_a_title(self):
        expected_value = "Summer Holiday"
        actual_value = self.song1.title
        self.assertEqual(expected_value, actual_value)

    def test_song_has_an_artist(self):
        expected_value = "Cliff Richard"
        actual_value = self.song1.artist
        self.assertEqual(expected_value, actual_value)

    def test_can_create_new_song(self):
        Song.create_a_new_song(self)

    def test_new_song_added_to_list(self):
        Song.add_song_to_list(self, "Toxic", "Britney Spears")
        excepted_value = 1
        actual_value = len(self.songs)
        self.assertEqual(excepted_value, actual_value)