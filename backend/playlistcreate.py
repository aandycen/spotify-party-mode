import pprint
import sys

import spotipy
import spotipy.util as util

username="victorsch52"
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id='089776be79914d7f8d3a4a87594f4463', client_secret='079b16e58d3c480c8e55263caed0c284', redirect_uri='http://localhost/')

def create_playlist(username, playlist_name):
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_create(username, playlist_name, public=True)
	playlist_id = results['id']
	return playlist_id

create_playlist("victorsch52", "New Playlist")
