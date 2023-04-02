import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('Beverly', 20, 'Flowers')

    
    def test_guest_has_favourite_song(self):
        self.assertEqual('Flowers', self.guest.favourite)