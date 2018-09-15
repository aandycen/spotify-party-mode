import pprint
import sys

from search import *
import spotipy
import spotipy.util as util

scope = 'playlist-modify-public'

if len(sys.argv) > 3:
	username = sys.argv[1]
	playlist_id = sys.argv[2]
	track_ids = sys.argv[3:]
else:
	print("Invalid parameters!")
	sys.exit()

token = util.prompt_for_user_token(username, scope)



if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)	
	print(results)
	print("Tracks added successfully")
else:
	print("Can't get token for ", username)


def addsong(artist, song):
	track_id = search.search(artist, song)
	sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_id)
