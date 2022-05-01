# test spotifyAPI handling module
import pytest
from modules.spotify_tools import get_access_token, get_related_artists, calc_BM25


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

# def test_calc_similaly():
#     main_artists1 = ['2yPOqQXgXAw3TVjCNReIrD' ,'7tyrh2CwSnilzMD8olQxcx' ,'7kDTCZA56nH6fCdEY0rBgh']
#     related_artists1 = ['6cMnpAZ9QN0wn4dVd0Tinb','2YtvgEYiTH6jh7n2UmUdXX' , '2yPOqQXgXAw3TVjCNReIrD']
#     main_artists2 = ["0O0hxUrO2PKxZknken3R24", '6cMnpAZ9QN0wn4dVd0Tinb', '2yPOqQXgXAw3TVjCNReIrD']
#     relatetd_artists2 = ['0hCWVMGGQnRVfDgmhwLIxq', '2yPOqQXgXAw3TVjCNReIrD', '7tyrh2CwSnilzMD8olQxcx']
#     user_artists = artists_set(main_artists1, related_artists1)
#     target_user_artists = artists_set(main_artists2, relatetd_artists2)
#     assert calculate_similaly(user_artists, target_user_artists)

def test_calc_BM25():
    # 変数設定
    all_user_num = 25
    aval = 10
    main_artists1 = ['2yPOqQXgXAw3TVjCNReIrD' ,'7tyrh2CwSnilzMD8olQxcx' ,'7kDTCZA56nH6fCdEY0rBgh']
    related_artists1 = ['6cMnpAZ9QN0wn4dVd0Tinb','2YtvgEYiTH6jh7n2UmUdXX' , '2yPOqQXgXAw3TVjCNReIrD']
    artist_to_user = {
        '2yPOqQXgXAw3TVjCNReIrD':["user01","user02"], '7tyrh2CwSnilzMD8olQxcx':["user01", "user02", "user03"], '7kDTCZA56nH6fCdEY0rBgh':["user01", "user02", "user03", "user05"], '6cMnpAZ9QN0wn4dVd0Tinb':["user04", "user06", "user07", "user01", "user05"],
        '2YtvgEYiTH6jh7n2UmUdXX':["user04"], 
    }
    point = calc_BM25(all_user_num=all_user_num, user_fav_main_artists=main_artists1, user_fav_sub_artists=related_artists1, artist_to_user=artist_to_user, aval=aval)
    assert point != None, "値が出力されていません"




