import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 2:
	username = sys.argv[1]
	playlist_name = sys.argv[2]
else:
	print("Invalid parameters")
	sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_create(username, playlist_name, public=True)
	print(results['id'])
	pprint.pprint("Playlist created successfully!")
else:
	print("Can't get token for", username)


def create_playlist(username, playlist_name):
	sp.spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_create(username, playlist_name, public=True)
	playlist_id = results['id']
	return playlist_id
