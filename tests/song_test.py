import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('Flowers', 'Miley Cyrus')

    def test_song_has_name(self):
        self.assertEqual('Flowers', self.song.name)