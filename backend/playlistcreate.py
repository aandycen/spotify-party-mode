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
token = util.prompt_for_user_token(username, scope, client_id='089776be79914d7f8d3a4a87594f4463', client_secret='079b16e58d3c480c8e55263caed0c284', redirect_uri='http://localhost/')

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
