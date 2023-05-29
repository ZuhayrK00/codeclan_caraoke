import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest
# from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Hip Hop", 3, 100.00)
        self.room_2 = Room("Pop", 4, 100.00)
        self.room_3 = Room("Grime", 4, 100.00)
        
        self.song_1 = Song("Burn", "Juice WRLD")
        self.song_2 = Song("Samantha", "Dave")
        self.song_3 = Song("Terminal 5", "Central Cee")
        self.song_4 = Song("Lose Yourself", "Eminem")
        self.song_5 = Song("No more interview", "Big Sean")
        self.song_6 = Song("Secrets", "Boogie wit a hoodie")

        self.playlist_1 = [self.song_1, self.song_2, self.song_3]
        self.playlist_2 = [self.song_4, self.song_5, self.song_6]

        self.guest_1 = Guest("Zuhayr", 50.00, "Terminal 5")
        self.guest_2 = Guest("Jim", 45.00, "Chapters")
        self.guest_3 = Guest("Joe", 75.00, "Pillowtalk")
        self.guest_4 = Guest("Jack", 20.00, "Lose Yourself")
        self.guest_5 = Guest("Jill", 60.00, "Burn")

        # self.drink_1 = Drink("Juice", 3.50)
        # self.drink_2 = Drink("Mocktail", 19.00)
        # self.drink_3 = Drink("Cocktail", 6.00)
        # self.drink_4 = Drink("Coke", 2.00)
        # self.drink_5 = Drink("Water", 0.00)

# MVP

    def test_room_has_name(self):
        self.assertEqual("Hip Hop", self.room_1.name)

    def test_can_update_room_name(self):
        self.room_2.name = "Soul"
        self.assertEqual("Soul", self.room_2.name)

    def test_room_has_playlist(self):
        self.assertEqual([], self.room_1.playlist)

    def test_room_has_guests(self):
        self.assertEqual([], self.room_1.guests)

    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1)
        expected = [self.song_1]
        self.assertEqual(expected, self.room_1.playlist)
        self.assertEqual(1, len(self.room_1.playlist))
    
    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        expected = [self.guest_1, self.guest_2]
        self.assertEqual(expected, self.room_1.guests)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_1)
        expected = [self.guest_2]
        self.assertEqual(expected, self.room_1.guests)
        self.assertEqual(1, len(self.room_1.guests))
    
# Extension

    def test_check_space_in_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.assertEqual(3, len(self.room_1.guests))

    def test_room_has_till(self):
        self.assertEqual(100, self.room_2.till)

    def test_can_increase_till(self):
        self.room_2.till += 15.00
        self.assertEqual(115, self.room_2.till)

    def test_can_take_entry_fee(self):
        self.room_1.take_entry_fee(self.guest_1)
        self.assertEqual(40, self.guest_1.cash)
        self.assertEqual(110, self.room_1.till)
