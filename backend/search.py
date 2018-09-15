import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='089776be79914d7f8d3a4a87594f4463', client_secret='079b16e58d3c480c8e55263caed0c284')




def search(song):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(song)
    uri = result['tracks']['items'][0]['id']
    print("Search Successful!")
    print(uri)
    return uri
search("Animal Spirits")
