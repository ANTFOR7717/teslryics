from flask import Flask, render_template, request
import genius_lyrics

# import re

# quoted = re.compile('"[^"]*"')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/lyrics/", methods=['POST'])
def fetch_lyrics():
    # Moving forward code
    lyrics, artist, song, albumart = "", "", "", ""
    if request.method == 'POST':
        result = request.form
        lyrics = genius_lyrics.search_lyrics(result['name'])
        artist = genius_lyrics.search_artist(result['name'])
        song = genius_lyrics.search_song(result['name'])
        # song = re.findall(r'"([^"]*)"', str(genius_lyrics.search_song(result['name'])))
        albumart = genius_lyrics.search_albumart(result['name'])
    return render_template('lyrics.html', lyrics=lyrics, artist=artist, song=song, albumart=albumart)


if __name__ == '__main__':
    app.run()
