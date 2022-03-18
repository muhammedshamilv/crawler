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

def crawl():
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists:
        print(name, "   :   ",link)

if __name__ =="__main__":
    crawl()