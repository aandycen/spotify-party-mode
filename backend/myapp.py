from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS
from flask import request
import requests
from playlistadd import addSong
from playlistcreate import create_playlist
from search import search
from words import returnRandomNoun

import pprint
import sys
import spotipy
import spotipy.util as util

app = Flask(__name__) # create a new website
CORS(app, resources={r"/*": {"origins": "*"}})


scope = 'playlist-modify-public'
username = "rilapapax"
playlist_name = "Your Room ID is: "

token = util.prompt_for_user_token(username, scope, client_id='72eca0e228434844a1638a6cc48e0ff5', client_secret='45c2a761720d4f1297510ef41f1c2b62', redirect_uri='http://localhost/')
playlists = {}


@app.route('/') # home page
def home():
    # return render_template('home.html')
    return "Home Page"

@app.route('/create', methods = ['GET']) # create room
def create():
    print("Attempting to create room...")
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    noun = str(returnRandomNoun())
    name = playlist_name + noun # Spotify-Party-Mode + *RANDOM NOUN*
    results = sp.user_playlist_create(username, name, public=True)
    playlist_id = results['id']
    #playlist_id = create_playlist(username, name, public=True)
    playlists[noun] = playlist_id
    playlistDict = {
        "playlistID" : playlist_id,
        "playlistName" : noun
    }
    print("New Room Created! ID: " + playlist_id + " Room Name: " + name)
    return jsonify(playlistDict)
    #playlist_ID = playlist_id
    #return playlist_id

@app.route('/join', methods = ['POST'])
def join():
    # the 'room' or playlist_id a user wants to join must exist
    #print(playlistID)
    post = request.get_json()
    name = post.get('name')
    name = name.lower()
    canJoin = "False"
    if name in playlists.keys():
        canJoin = "True"
        print("Successfully Entered Room: " + name + " (" + playlists[name] + ")")
    else:
        print("Room Name Does Not Exist!")
    boolDict = {
        "canJoin" : canJoin
    }
    return jsonify(boolDict)

@app.route('/add', methods = ['POST'])
def add():
    post = request.get_json()
    song = post.get('song')
    name = post.get('name') # room name
    name = name.lower()
    id = playlists[name]
    songDict = addSong(song, id) # return dict of song and artist, and track_id
    artist = songDict['artist']
    print(artist + "'s' " + song + " added to playlist: " + name + " (" + id + ")")
    return jsonify(songDict)

if '__name__' == '__main__':
    app.run(app)
