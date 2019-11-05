import json
import requests
from bs4 import BeautifulSoup


class AlbumsParser:
    def __init__(self, artist_name):
        self.artist = artist_name

    def to_json(self):
        with open(f'{self.artist}.json', 'w') as file:
            file.write(json.dumps(self.fetch_albums(), indent=2))

    def fetch_albums(self):
        albums = []
        page = self.get_albums_page()
        for link in self.fetch_albums_links(page):
            albums.append(self.fetch_album(self.get_album_page(link)))
        return albums

    def get_albums_page(self, page_number=1):
        return requests.get(
            f'https://www.last.fm/music/{self.artist}/+albums?page={page_number}'
        ).text

    @staticmethod
    def duration_to_seconds(duration: str) -> int:
        try:
            seconds = int(duration[:duration.find(':')]) * 60 + \
                      int(duration[duration.find(':') + 1:])
            return seconds
        except ValueError:
            return duration

    @staticmethod
    def get_album_page(link: str):
        return requests.get(link).text

    @staticmethod
    def fetch_albums_links(albums_page: str):
        soup = BeautifulSoup(albums_page, 'html.parser')
        section = soup.find('section', {'id': 'artist-albums-section'})
        for a in section.findAll('a', {'class': 'link-block-target'}):
            yield f"https://www.last.fm{a['href']}"

    @staticmethod
    def fetch_album(album_page: str):
        soup = BeautifulSoup(album_page, 'html.parser')
        album = soup.find('h1').text
        year = soup.findAll('dd', {
                'class': 'catalogue-metadata-description'})[1].text.split()[-1]
        artist = soup.find('span', {'itemprop': 'name'}).text
        songs = []
        for tr in soup.find_all('tr', {'class': 'chartlist-row'}):
            duration = tr.find(
                    'td', {'class': 'chartlist-duration'}
            ).text.replace('\n', '').strip()
            duration_seconds = AlbumsParser.duration_to_seconds(duration)
            songs.append({
                'name': tr.find(
                    'td', {'class': 'chartlist-name'}
                ).text.replace('\n', '').strip(),
                'artist': artist,
                'duration': duration_seconds,
                'year': year,
                'album': album
            })
        return {
            'name': album,
            'year': year,
            'genre': None,
            'artist': artist,
            'songs': songs
        }


a = AlbumsParser('alt-J')
a.to_json()
