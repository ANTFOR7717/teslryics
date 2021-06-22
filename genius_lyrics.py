import lyricsgenius

genius = lyricsgenius.Genius('yIMwOXNt-DWfbMt1k-KSWVh_U2ND2MQdLjTs0k-KHGykZQFSCH_1APSh2aafsmZW')


def search_song(name, artist=''):
    song = genius.search_song(name, artist)
    return song.title_with_featured


def search_artist(name, artist=''):
    artist = genius.search_song(name, artist)
    return artist.artist


def search_lyrics(name, artist=''):
    lyrics = genius.search_song(name, artist)
    return lyrics.lyrics


def search_albumart(name, artist=''):
    albumart = genius.search_song(name, artist)
    return albumart.song_art_image_url
