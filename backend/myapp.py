from flask import Flask, render_template
from flask import jsonify
from playlistadd import addsong
from playlistcreate import create_playlist
from search import search

app = Flask(__name__) # create a new website


@app.route('/') # home page
def home():
    # return render_template('home.html')
    return "Home Page"

@app.route('/create') # create room
def create(username, playlist_name, methods = ['POST']):
    create_playlist(username, playlist_name)

def add(artist, song, methods = ['POST']):
    addSong(artist, song)

def searchSong(artist, song):
    search(artist, song)

if '__name__' == '__main__':
    app.run(app)
