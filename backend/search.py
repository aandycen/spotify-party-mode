import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='72eca0e228434844a1638a6cc48e0ff5', client_secret='45c2a761720d4f1297510ef41f1c2b62')

def search(song):
    songDict = {}
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(song)
    #print(result['tracks']['items'][0])
    uri = result['tracks']['items'][0]['id']
    songDict['uri'] = uri
    name = result['tracks']['items'][0]['name']
    songDict['name'] = name
    artist = result['tracks']['items'][0]['album']['artists'][0]['name']
    songDict['artist'] = artist
    print("Search Successful!")
    print(uri)
    return songDict

#search("Animal Spirits")
