# test spotifyAPI handling module
from webbrowser import get
import pytest
from modules.spotify_tools import *

def test_get_access_token():
    assert get_access_token("test_id", "test_secret") == None
    assert get_access_token(1111, 1111) == None

def test_spotify():
    assert get_related_artists("test","test") == {}
    assert get_related_artists(1111,"test") == {}
    # ↓エラーの対策よくわからん
    # with pytest.raises(TypeError) as e:
    #     _ = get_access_token()
    # assert str(e.value) == "get_access_token() missing 2 required positional arguments: 'CLIENT_ID' and 'CLIENT_SECRET'"
