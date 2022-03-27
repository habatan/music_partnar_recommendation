# test spotifyAPI handling module
from msilib.schema import Error
import pytest
from modules.spotify_tools import *

def test_get_access_token():
    assert get_access_token("test_id", "test_secret")
    assert get_access_token(1111, 1111)

def test_spotify():
    assert get_related_artists("test","test") == {}
    assert get_related_artists(1111,"test") == {}
