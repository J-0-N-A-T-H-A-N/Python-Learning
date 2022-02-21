import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

chart_date = "1975-07-23"
URL = f"https://www.billboard.com/charts/hot-100/{chart_date}"

html_content = requests.get(URL).text

soup = BeautifulSoup(html_content, "html.parser")

songs = soup.find_all(name="h3", class_="a-no-trucate")
artists = soup.find_all(name="span", class_="a-no-trucate")

tracks = {track.getText().strip(): artist.getText().strip() for track, artist in zip(songs, artists)}

SPOTIFY_CLIENT_ID = "93514d751ee44414a453b2b95083142c"
SPOTIFY_CLIENT_SECRET = "6d6a3e5eabf04b87a74b5a83ca403ca6"

scope = "playlist-modify-private, playlist-read-private, user-read-playback-state, user-modify-playback-state"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        scope=scope,
        cache_path=None,
        redirect_uri="http://localhost:8080/callback"
    )
)


spotify_user = sp.current_user()
print(f"{spotify_user['display_name']} ({spotify_user['id']})")

playlists = sp.current_user_playlists()
user_playlists = [pl["name"] for pl in playlists["items"]]

new_playlist_name = f"{chart_date} Billboard 100"
if new_playlist_name not in user_playlists:
    print("Not there, creating")
    new_playlist = sp.user_playlist_create(user=spotify_user["id"], name=new_playlist_name, public=False,
                                           collaborative=False, description="Python Script")
    playlist_id = new_playlist["id"]

    track_uri_list = []
    for track, artist in tracks.items():
        song_search = sp.search(q=f"track: {track} artist: {artist})", type="track", limit=1)
        try:
            track_uri_list.append(song_search["tracks"]["items"][0]["uri"])
        except:
            print(f"Couldn't find a match for '{track}' by '{artist}'")

    sp.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)    # Items must be a list!

else:
    print(f"Hey! That playlist, '{new_playlist_name}', exists!")

spotify_devices = sp.devices()
pprint.pprint(spotify_devices)
sp.volume(volume_percent=50, device_id="2b1829699fe111497e0b81545adecbe49c9a56d5")
spotify_devices = sp.devices()
pprint.pprint(spotify_devices)
