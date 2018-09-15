import pprint
import sys

from search import search
from search import *
import spotipy
import spotipy.util as util

scope = 'playlist-modify-public'
username = "rilapapax"
token = util.prompt_for_user_token(username, scope, client_id='72eca0e228434844a1638a6cc48e0ff5', client_secret='45c2a761720d4f1297510ef41f1c2b62', redirect_uri='http://localhost/')
# client_id (victor) 089776be79914d7f8d3a4a87594f4463
# client secret id (victor) 079b16e58d3c480c8e55263caed0c284

def addSong(song, playlist_id):
	songDict = search(song)
	track_id = songDict['uri'].split()
	print(track_id)
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_add_tracks(username, playlist_id, track_id)
	print(results)
	return songDict
