import spotipy
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import urllib3 as url
import os


def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_lyrics(artist, music):
    http = url.PoolManager()
    artist = artist.replace(" ", "").lower()
    artist = artist.replace("'", "")
    artist = artist.replace("(", "")
    artist = artist.replace(")", "")
    artist = artist.replace(",", "")
    artist = artist.replace("!", "")
    artist = artist.replace("-", "")
    artist = artist.replace("+", "")
    artist = artist.replace(".", "")
    artist = artist.replace("ü", "u")
    artist = artist.replace("ö", "o")
    artist = artist.replace("ä", "a")
    artist = artist.replace("ë", "e")
    music = music.replace(" ", "").lower()
    music = music.replace("'", "")
    music = music.replace("(", "")
    music = music.replace(")", "")
    music = music.replace(",", "")
    music = music.replace("!", "")
    music = music.replace("-", "")
    music = music.replace("+", "")
    music = music.replace(".", "")
    music = music.replace(".", "")
    music = music.replace("ü", "")
    music = music.replace("ö", "")
    music = music.replace("ä", "")
    music = music.replace("ë", "")
    music = music.split("liveat")[0]
    music = music.split("feat")[0]
    music = music.split("remastered")[0]

    music_url = f"https://www.azlyrics.com/lyrics/{artist}/{music}.html"
    r = http.request('GET', music_url)

    # print(music_url)

    lyrics = str(r.data)
    lyrics = lyrics.split("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")[1]

    lyrics = lyrics.split("<!-- MxM banner -->")[0]
    lyrics = lyrics.replace("\\r\\n", "\n")
    lyrics = lyrics.replace("\\n", "\n")
    lyrics = lyrics.replace("<br>", "")
    lyrics = lyrics.replace("\\r", "")
    lyrics = lyrics.replace("&quot", "")
    lyrics = lyrics.replace("\\", "")
    lyrics = lyrics.replace("xe2x80x99", "'")
    lyrics = lyrics.replace(";", "")
    lyrics = lyrics.replace("</div>", "")
    lyrics = lyrics.replace("<i>", "")
    lyrics = lyrics.replace("</i>", "")
    lyrics = lyrics.replace("\n\n\n", "")
    lyrics = lyrics.replace("xc3xbc", "ü")
    lyrics = lyrics.replace("ö", "o")
    lyrics = lyrics.replace("xc3xa4", "ä")
    lyrics = lyrics.replace("ë", "e")

    return lyrics


f = open("id.txt").readlines()

token = util.prompt_for_user_token("r23111",
                                   "user-read-playback-state",
                                   client_id=f[0],
                                   client_secret=f[1],
                                   redirect_uri='http://localhost:8080')


spotify = spotipy.Spotify(auth=token)
# spotipy.oauth2.SpotifyOAuth(f[0], f[1], redirect_uri="http://localhost:8080")


track = spotify.current_playback()
last_track = 0

while(True):
    track = spotify.current_playback()
    if(track != None and last_track != None and last_track != 0):
        if(last_track["item"] == track["item"]):
            continue
    if(track == None):
        if(track == last_track):
            continue
    else:
        if(track == None):
            print("Spotify is not playing anything")
        else:
            clear_scr()
            band = track["item"]["artists"][0]["name"]
            music = track["item"]["name"]
            print(f"\n\n\t========================================\n\t\t{music} by {band}\n\t========================================\n")
            try:
                print(get_lyrics(band, music))
            except:
                print("\nNo Lyrics Found")
        last_track = track

