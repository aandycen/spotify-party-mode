import pprint
import sys

import spotipy
import spotipy.util as util

username="rilapapax"
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id='72eca0e228434844a1638a6cc48e0ff5', client_secret='45c2a761720d4f1297510ef41f1c2b62', redirect_uri='http://localhost/')

def create_playlist(username, playlist_name):
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_create(username, playlist_name, public=True)
	playlist_id = results['id']
	return playlist_id
