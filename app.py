from flask import Flask, render_template
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

TRACKS_FILE = os.path.join(basedir, 'static', 'tracks.json')

def get_tracks():
    if not os.path.exists(TRACKS_FILE):
        return []
    with open(TRACKS_FILE, encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artistas')
def artistas():
    return render_template('artistas.html')

@app.route('/musicas')
def musicas():
    tracks = get_tracks()
    return render_template('musicas.html', tracks=tracks)

@app.route('/ultima')
def ultima():
    return render_template('ultima.html')

if __name__ == '__main__':
    app.run(debug=True)
