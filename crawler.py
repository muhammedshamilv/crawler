import requests
from bs4 import BeautifulSoup


def get_artists(url):
    artist=[]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links= tracklists.find_all("a")
    for i in links:
        artist.append((i.text,i['href']))
    return artist


def get_songs(artist_url):
    songs=[]
    r = requests.get(artist_url)
    soup = BeautifulSoup(r.content, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links=tracklists.find_all("a")
    for i in links:
        songs.append((i.text,i['href']))
    return songs


def crawl():
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists:
        print(name, "   :   ",link)
        songs = get_songs(link)
        print(songs)

if __name__ =="__main__":
    crawl()
