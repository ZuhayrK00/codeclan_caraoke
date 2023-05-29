import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Zuhayr", 50.00, "Terminal 5")

        self.room_1 = Room("Hip Hop", 3, 100.00)

        self.song_1 = Song("Burn", "Juice WRLD")
        self.song_2 = Song("Samantha", "Dave")
        self.song_3 = Song("Terminal 5", "Central Cee")

# MVP 

    def test_guest_has_name(self):
        self.assertEqual("Zuhayr", self.guest_1.name)

    def test_can_update_guest_name(self):
        self.guest_1.name = "Bob"
        self.assertEqual("Bob", self.guest_1.name)
    
# Extensions 

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest_1.cash)
        
    def test_can_reduce_guest_cash(self):
        self.guest_1.cash -= 15.00
        self.assertEqual(35, self.guest_1.cash)


        