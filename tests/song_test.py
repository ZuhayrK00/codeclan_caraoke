import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Burn", "Juice WRLD")

# MVP
    
    def test_song_has_title(self):
        self.assertEqual("Burn", self.song_1.title)

    def test_can_update_song_title(self):
        self.song_1.title = "Lucid Dreams"
        self.assertEqual("Lucid Dreams", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Juice WRLD", self.song_1.artist)

    def test_can_update_song_artist(self):
        self.song_1.artist = "Elvis"
        self.assertEqual("Elvis", self.song_1.artist)