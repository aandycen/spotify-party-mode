import spotipy
import sys
import spotipy.util as util
import pprint

scope = 'user-library-read'

username = sys.argv[1]


token = util.prompt_for_user_token(username,scope)

if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
	print("Can't get token for ", username)



