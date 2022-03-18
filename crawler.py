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

def get_lyrics(song_url):
    r = requests.get(song_url)
    soup = BeautifulSoup(r.content, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics


def crawl():
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists:
        print(name, "   :   ",link)
        songs = get_songs(link)
        for song, song_link in songs:
            with open("lyric","a") as f:
                lyrics = get_lyrics(song_link) 
                f.write("\n\n*********\n\n")
                f.write(song)
                f.write("\n\n*********\n\n")
                f.write(lyrics)
            print("Done")
        print("DONE")

if __name__ =="__main__":
    crawl()
