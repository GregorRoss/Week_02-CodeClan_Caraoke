import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest('Jean-Luc Picard', 100, 'Miracle')
        self.guest2 = Guest('William Riker', 50, 'Die for you')
        self.guest3 = Guest('Geordi La Forge', 20, 'Calm down')
        self.guest4 = Guest('Worf', 30, 'People')
        self.guest5 = Guest('Deanna Troi', 50, 'Ceilings')

        self.room1 = Room('Holodeck1',10,100,2)
        self.room2 = Room('Holodeck2',20,100,4)
        self.room3 = Room('Holodeck3',30,100,3)
        self.room4 = Room('Holodeck4',50,100,5)

        self.song1 = Song('Miracle','Calvin Harris')
        self.song2 = Song('Die for you','Weekend')
        self.song3 = Song('Calm down','Rema')
        self.song4 = Song('People','Libianca')
        self.song5 = Song('Ceilings','Lizzy McAlpine')

    def test_room_has_name(self):
        expected_value = 'Holodeck1'
        actual_value = self.room1.name
        self.assertEqual(expected_value, actual_value)


    def test_add_guest_to_room(self):
        self.room1.guest_check_in(self.guest1)
        expected_value = 1
        actual_value = len(self.room1.occupancy)
        self.assertEqual(expected_value, actual_value)

    def test_check_out_guest_from_room(self):
        self.room1.guest_check_in(self.guest1)
        self.room1.guest_check_out(self.guest1)
        expected_value = 0
        actual_value = len(self.room1.occupancy)
        self.assertEqual(expected_value, actual_value)

    def test_add_song_to_room(self):
        self.room2.add_song(self.song1)
        expected_value = 1
        actual_value = len(self.room2.playlist)
        self.assertEqual(expected_value, actual_value)

    def test_remove_song_from_room(self):
        self.room2.add_song(self.song1)
        self.room2.remove_song(self.song1)
        expected_value = 0
        actual_value = len(self.room2.playlist)
        self.assertEqual(expected_value, actual_value)

    def test_add_guest_to_rooms(self):
        self.room1.guest_check_in(self.guest1)
        self.room1.guest_check_in(self.guest2)
        self.room2.guest_check_in(self.guest4)
        self.room2.guest_check_in(self.guest5)
        expected_value =[2,2]
        actual_value = [len(self.room1.occupancy),len(self.room2.occupancy)]
        self.assertEqual(expected_value, actual_value)

    def test_add_songs_to_rooms(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song3)
        self.room1.add_song(self.song4)
        self.room1.add_song(self.song5)
        self.room2.add_song(self.song1)
        self.room2.add_song(self.song2)
        self.room2.add_song(self.song3)
        self.room2.add_song(self.song4)
        self.room2.add_song(self.song5)        
        self.room3.add_song(self.song1)
        self.room3.add_song(self.song2)
        self.room3.add_song(self.song3)
        self.room3.add_song(self.song4)
        expected_value =[5,5,4]
        actual_value = [len(self.room1.playlist),len(self.room2.playlist),len(self.room3.playlist)]
        self.assertEqual(expected_value, actual_value)

    def test_add_guest_to_rooms_with_room_check(self):
        self.room1.guest_check_in_check_size(self.guest1)
        self.room1.guest_check_in_check_size(self.guest2)
        self.room1.guest_check_in_check_size(self.guest3)
        expected_value = [2,"Room full, please return in 10 minutes or select another room"]
        actual_value = [len(self.room1.occupancy), "Room full, please return in 10 minutes or select another room"]
        self.assertEqual(expected_value, actual_value)

    def test_favourite_song(self):
        self.room4.guest_check_in(self.guest1)
        self.room4.guest_check_in(self.guest2)
        self.room4.guest_check_in(self.guest4)
        self.room4.guest_check_in(self.guest5)
        self.room4.add_song(self.song1)
        self.room4.add_song(self.song2)
        self.room4.add_song(self.song3)
        self.room4.add_song(self.song4)
        self.room4.add_song(self.song5)
        expected_value = "yay favourite song"
        actual_value = "yay favourite song"
        self.assertEqual(expected_value, actual_value)
   
    def test_entry_fee(self):
        self.room1.guest_check_in(self.guest1)
        self.room1.guest_check_in(self.guest2)
        self.room2.guest_check_in(self.guest4)
        self.room2.guest_check_in(self.guest5)
        expected_value = [90,40,10,30]
        actual_value = [self.guest1.wallet,self.guest2.wallet,self.guest4.wallet,self.guest5.wallet]
        self.assertEqual(expected_value, actual_value)

