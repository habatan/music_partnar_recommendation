# test spotifyAPI handling module
import pytest
from modules.spotify_tools import *

def test_spotify():
    # os.environでエラー出てる
    assert get_related_artists("test") == {}
