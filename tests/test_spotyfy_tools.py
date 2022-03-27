# test spotifyAPI handling module
import pytest
import modules.spotify_tools as spotify

def test_spotify():
    # os.environでエラー出てる
    assert spotify.get_related_artists_dict("test") == {}
