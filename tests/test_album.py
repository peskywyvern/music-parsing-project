import unittest
from classes import Artist, Song, Album, WrongArtistError


class TestAlbum(unittest.TestCase):
    def test_creating_album_adds_it_to_artists_albums_list(self):
        a = Artist('Lana Del Ray', 'USA')
        b = Album('Born to Die', 2012, 'alternative/indie', a)
        self.assertIn(b, a.albums)

    def test_adding_song_raises_error_when_artists_doesnt_match(self):
        a = Artist('Lana Del Ray', 'USA')
        a1 = Artist('Adele', 'UK')
        b = Album('Born to Die', 2012, 'alternative/indie', a)
        b1 = Album('21', 2011, 'pop/soul', a1)
        c = Song('Blue Jeans', a, 2012, 240, b)
        with self.assertRaises(WrongArtistError):
            b1.add_song(c)

    def test_duration_is_calculated_right(self):
        a = Artist('Lana Del Ray', 'USA')
        b = Album('Born to Die', 2012, 'alternative/indie', a)
        c = Song('Blue Jeans', a, 2012, 240, b)
        d = Song('Born to Die', a, 2012, 320, b)
        self.assertEqual(b.duration, c.duration + d.duration)

    def song_number_is_calculated_right(self):
        a = Artist('Lana Del Ray', 'USA')
        b = Album('Born to Die', 2012, 'alternative/indie', a)
        c = Song('Blue Jeans', a, 2012, 240, b)
        d = Song('Born to Die', a, 2012, 320, b)
        self.assertEqual(b.songs_number, 2)

