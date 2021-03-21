import requests
from bs4 import BeautifulSoup

class SongList:

    def __init__(self):
        self.URL = "https://www.billboard.com/charts/hot-100/"
        self.songs_list = []
        self.date = ""
        self.year = ""


    def songlist(self,date):
        self.date = date
        self.year=  self.date.split("-")[0]

        response = requests.get(self.URL + self.date)
        songs_data = response.text
        soup = BeautifulSoup(songs_data, "html.parser")
        song_name = soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")
        self.songs_list = [song.getText() for song in song_name]
        return self.songs_list