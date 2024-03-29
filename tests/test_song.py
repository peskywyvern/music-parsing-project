import unittest
from classes import Artist, Song, Album


class TestSong(unittest.TestCase):
    def test_creating_song_adds_it_to_artists_songs_list(self):
        a = Artist('Ed Sheeran', 'UK')
        b = Album('Divide', 2017, 'pop', a)
        c = Song('Shape of You', a, 2017, 234, b)
        self.assertIn(c, a.songs)

    def test_creating_song_adds_it_to_albums_songs_list(self):
        a = Artist('Ed Sheeran', 'UK')
        b = Album('Divide', 2017, 'pop', a)
        c = Song('New Man', a, 2017, 189, b)
        self.assertIn(c, b.songs)

    def test_repr_check(self):
        a = Artist('Ed Sheeran', 'UK')
        b = Album('Divide', 2017, 'pop', a)
        c = Song('Supermarket Flowers', a, 2017, 221, b)
        self.assertEqual(repr(c), c.name)