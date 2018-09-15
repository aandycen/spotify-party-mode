import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='089776be79914d7f8d3a4a87594f4463', client_secret='079b16e58d3c480c8e55263caed0c284')




if len(sys.argv) > 2:
    artist_str = sys.argv[1]
    song_str = sys.argv[2]
else:
    search_str = "Vulfpeck"
    song_str = "Dean Town"


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
result = sp.search(artist_str)
for x in range(0, len(result['tracks']['items'])):
    if(result['tracks']['items'][x]['name'] == song_str):
        print("Song found!")
        pprint.pprint(result['tracks']['items'][x]['id'])
#pprint.pprint(result['tracks']['items'][3])


def search(artist, song):
    result = sp.search(artist)
    for x in range(0, len(result['tracks']['items'])):
        if(result['tracks']['items'][x]['name'] == song):
            print("Song found!")
            pprint.pprint(result['tracks']['items'][x]['id'])
            uri = result['tracks']['items'][x]['id']
    return uri


