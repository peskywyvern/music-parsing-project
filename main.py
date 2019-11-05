from classes import Artist, Album, Song

if __name__ == '__main__':
    a = Artist('Ed Sheeran', 'GB')
    s = Artist('Edn', 'GB')
    b = Album('Divide', 2015, 'pop', a)
    print(a.albums)
    print(a.songs)
    c = Song('Galway Girl', a, 2016, 150, b, 9)
    print(a.songs)

    print(c.duration)