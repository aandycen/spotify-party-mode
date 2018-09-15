import pprint
import sys

from search import search
from search import *
import spotipy
import spotipy.util as util

scope = 'playlist-modify-public'
username = "victorsch52"
token = util.prompt_for_user_token(username, scope)

def addsong(username, song, playlist_id):
	track_id = search(song).split()
	print(track_id)
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_add_tracks(username, playlist_id, track_id)
	print(results)



