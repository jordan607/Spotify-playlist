import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:

    def __init__(self, song_list, date):
        self.user = ""

        self.cred_dict = ""
        self.Client_ID = ""
        self.Client_Secret= ""
        self.scope = "playlist-modify-public"
        self.Rediredt_URI = "http://example.com"
        self.song_uri = []
        self.date = date
        self.year = date.split("-")[0]
        self.user = ""
        self.findcred()
        self.song_list =song_list

    def findcred(self):
        with open("credentials","r") as cred:
            credentials = cred.read()
        self.cred_dict = json.loads(credentials)
        self.Client_ID = self.cred_dict["Client_ID"]
        self.Client_Secret = self.cred_dict["Client_Secret"]

    def spotifyOauth(self):

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.Client_ID,
                                                            client_secret=self.Client_Secret,
                                                            redirect_uri=self.Rediredt_URI,
                                                            scope=self.scope,
                                                            show_dialog=True,
                                                            cache_path="token.txt"
                                                            ))

        self.user = sp.current_user()["id"]

        for song in self.song_list:
            try:
                result = sp.search(q=f"track:{song} year:{self.year}", type="track")
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uri.append(uri)
            except IndexError:
                print(f"Song not found, Skipped: {song}")
            except:
                print(f"Song not found, Skipped: {song}")


        playlist = sp.user_playlist_create(user= self.user, name=f"{self.date} Billboard 100", description=f"Top 100 songs of Billboard for date: {self.date}")
        sp.playlist_add_items(playlist["id"], self.song_uri )