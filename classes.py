import datetime
from typing import List


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.songs = set()
        self.albums = set()

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def albums_number(self):
        return len(self.albums)

    def __repr__(self):
        return self.name


class Album:
    def __init__(self, name, year, genre, artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = set()
        artist.albums.add(self)

    def add_song(self, song):
        if song.artist != self.artist:
            raise WrongArtistError
        else:
            self.songs.add(song)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return datetime.timedelta(
            seconds=sum(song.duration.seconds for song in self.songs)
        )

    def __repr__(self):
        return self.name


class Song:
    def __init__(self, name, artist, year, duration, album, features: List[Artist] = None):
        self.name = name
        self.artist = artist
        self.features = features
        self.year = year
        self.duration = datetime.timedelta(seconds=duration)
        self.album = album
        album.add_song(self)
        artist.songs.add(self)

    def __repr__(self):
        return self.name


a = Artist('Ed Sheeran', 'UK')
b = Album('Divide', 2017, 'pop', a)
c = Song('Galway Girl', a, 2017, 248, b)
d = Song('Castle on the Hill', a, 2017, 421, b)
print(c.duration)