import re
import requests
from bs4 import BeautifulSoup

AZ_LYRICS = "https://www.azlyrics.com/lyrics/{}/{}.html"

# Remove newline and line feed characters from the lyrics
def _clean_lyrics(lyrics):

    # Filter out lines that are just the newline
    lyric_list = list(filter(lambda x: x != "\n", lyrics))

    # Strip both newline and carriage return chars from a lyric line
    lyric_list = list(map(lambda x: x.strip("\r").strip("\n"), lyric_list))[1:]

    return lyric_list

# Remove leading The from the artist name
# Remove all non alphanumeric characters from artist, song names
def _clean_names(artist_name, song_name):
    artist_name = re.sub(r"^The", "", artist_name)
    artist_name = re.sub(r"[^a-zA-Z0-9_]", "", artist_name.lower().replace(" ", ""))
    song_name = re.sub(r"[^a-zA-Z0-9_]", "", song_name.lower().replace(" ", ""))

    return artist_name, song_name


def _create_url(artist_name, song_name):
    artist_name, song_name = _clean_names(artist_name, song_name)
    return AZ_LYRICS.format(artist_name, song_name)


def _get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    elif r.status_code == 404:
        return "Lyrics not found"


def get_lyrics(artist, song):
    artist_name, song_name = _clean_names(artist, song)
    # print(artist_name, song_name)
    url = _create_url(artist_name, song_name)
    page = _get_page(url)
    if page == "Lyrics not found":
        return [page]
    soup = BeautifulSoup(page, "html.parser")
    mydivs = soup.find("div", {"class": "ringtone"})
    lyrics = mydivs.find_next_sibling("div")
    lyric_list = []
    for line in lyrics:
        try:
            if "<br/>" not in line.string:
                lyric_list.append(line.string)
        except TypeError:
            pass

    lyric_list = _clean_lyrics(lyric_list)
    return lyric_list

# Print out the lyrics in blocks of 4 lines
def pretty_print_lyrics(lyric_list):
    for i in range(0, len(lyric_list)):
        print(lyric_list[i])
        if (i + 1) % 4 == 0 and i > 0:
            print("\n")
            # pass
    print("\n")
