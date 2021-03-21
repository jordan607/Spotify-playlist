from Spotify import Spotify
from SongList import SongList


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
get_song_list = SongList().songlist(date)
spot_inst = Spotify(get_song_list, date).spotifyOauth()







