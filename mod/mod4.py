import json
import requests

artist = input("enter the artist name")
song_title= input("enter the song name")


url= 'https://api.lyrics.ovh/v1/' + artist + '/' + song_title

response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data["lyrics"]

print(lyrics)