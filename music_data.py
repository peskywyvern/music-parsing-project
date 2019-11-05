import requests
from bs4 import BeautifulSoup


def get_artist_page(artist_name: str):
    return requests.get(f'https://www.last.fm/ru/music/{artist_name}').text


def get_albums_page(artist_name: str, page_number: int):
    return requests.get(
        f'https://www.last.fm/music/{artist_name}/+albums?page={page_number}'
    ).text


def get_album_page(link: str):
    return requests.get(link).text


def fetch_album(album_page: str):
    soup = BeautifulSoup(album_page, 'html.parser')
    album_name = soup.find('h1').text
    album_release = soup.find('dd', {'class': 'catalogue-metadata-description'}).text
    year = int(album_release.split(' ')[-1])
    artist_name = soup.find_all('span', {'itemprop': 'name'}).text
    songs = []
    for tr in soup.find_all('tr', {'class': 'chartlist-row'}):
        songs.append({
            'name': tr.find('td', {'class': 'chartlist-name'}).text,
            'artist': artist_name,
            'duration': tr.find('td', {'class': 'chartlist-duration'}).text,
            'year': year,
            'album': album_name
        })
    return true


def fetch_albums_links(albums_page: str):
    soup = BeautifulSoup(albums_page, 'html.parser')
    section = soup.find('section', {'id': 'artist-albums-section'})
    for a in section.findAll('a', {'class': 'link-block-target'}):
        yield f"https://www.last.fm{a['href']}"


def parse_artist_info(artist_page: str):
    soup = BeautifulSoup(artist_page, 'html.parser')
    artist_name = soup.find('h1').text
    print(artist_name)
    try:
        location = soup.findAll(
            'dd',
            {'class': 'catalogue-metadata-description'}
        )[1].text
    except IndexError:
        location = 'undefined'

    return artist_name, location



