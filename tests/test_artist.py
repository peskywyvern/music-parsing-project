import unittest
from classes import Artist, Song, Album


class TestArtist(unittest.TestCase):
    def test_song_number_is_calculated_right(self):
        a = Artist('Ed Sheeran', 'UK')
        b = Album('Divide', 2017, 'pop', a)
        c = Song('Galway Girl', a, 2017, 248, b)
        d = Song('Castle on the Hill', a, 2017, 421, b)
        self.assertEqual(a.songs_number, 2)

    def test_albums_number_is_calculated_right(self):
        a = Artist('Panic At The Disco', 'USA')
        b = Album('Pray for the Wicked', 2018, 'rock/alternative', a)
        c = Album('Death of a Bachelor', 2016, 'rock/alternative', a)
        self.assertEqual(a.albums_number, 2)

    def test_repr_check(self):
        a = Artist('Nickelback', 'Canada')
        self.assertEqual(repr(a), a.name)