# test spotifyAPI handling module
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

def test_calc_similaly():
    main_artists1 = ["#0001" ,"#0002" ,"#0003"]
    related_artists1 = ["#0004", "#0002", "#0003"]
    main_artists2 = ["#0001", "#0003", "#0004"]
    relatetd_artists2 = ["#0006", "#0008", "#0001"]
    user_artists = artists_set(main_artists1, related_artists1)
    target_user_artists = artists_set(main_artists2, relatetd_artists2)
    assert calculate_similaly(user_artists, target_user_artists)
