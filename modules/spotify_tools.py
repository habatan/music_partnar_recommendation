# Spotify tools
import requests
import json
import math
import numpy as np
import gensim

def get_access_token(CLIENT_ID:str,CLIENT_SECRET:str)->str:
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    '''Get user authorization and set access token.'''
    # Request authorization from user
    payload = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }
    # `auth=(CLIENT_ID, SECRET)` basically wraps an 'Authorization'
    # header with value:
    # b'Basic ' + b64encode((CLIENT_ID + ':' + SECRET).encode())
    
    res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=payload)
    res_data = res.json()
    access_token = res_data.get('access_token')
    
    return access_token


def get_related_artists(access_token, artist_id:str)->json:
    """
    アーティストidを入力にして類似のアーティストを辞書で返します
    input : spotify access token, output : {aritist_id(1) : artist_value(1),･･･,artist_id(N) : artist_value(N)}
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = {'Authorization':f'Bearer {access_token}','Content-Type': 'application/json','Accept': 'application/json'}
    # requestの例外処理
    try:
        response = requests.get(url, headers=headers)
        artist_info = response.json()['artists']
        artists = {}
        for data in artist_info:
            artist_id = data['id']
            artist_name = data['name']
            artists[artist_id] = artist_name
    except:
        artists = {}
        
    return artists

# stracture
# def artists_set(main_artists, related_artists):
#     main = set(main_artists)
#     related = set(related_artists)
#     return {
#         "main":main,"related":related
#         }

# artists_set構造を用いた関数
# def calculate_similaly(user_fav_artists_set, target_user_artists_set):
#     # 重み的な何か
#     C1 = 0.05
#     C2 = 0.05
#     main_fav_diff = abs(len(user_fav_artists_set["main"]) - len(target_user_artists_set["main"]))
#     related_fav_diff = abs(len(user_fav_artists_set["related"]) - len(target_user_artists_set["related"]))
#     point = 0
#     point += len(user_fav_artists_set["main"] & target_user_artists_set["main"]) - C1*(main_fav_diff)
#     point += len(user_fav_artists_set["related"] & target_user_artists_set["related"]) - C2 * (related_fav_diff)
#     return point

def calc_BM25(all_user_num, user_fav_main_artists, user_fav_sub_artists, artist_to_user,  aval, k1 = 1.2, b = 0.75):
    """
    BM25スコアを計算する
    all_user_num; 総user数
    user_fav_main_artists: userが選択したartists
    user_fav_sub_artists: userが選択したartistの関連artists
    artist_to_user : artistを選択しているuserのdictを返す
    aval: ユーザ一人当たり平均選択アーティスト数
    k1: パラメータ（初期値1.2）
    b: パラメータ（初期値0.75）
    """
    # [課題] ユーザが選択したユーザと関連ユーザが混ざっている
    assert type(user_fav_main_artists) == list and type(user_fav_sub_artists) == list, "user_fav_artistのデータ形式をlistにしてください"
    user_selected = user_fav_sub_artists + user_fav_main_artists
    dl = len(user_selected)
    score = 0.0
    # user選択アーティストに含むアーティストだけ考えてスコアを計算
    for artist_id in user_fav_main_artists:
        # artistにおけるuserの選択回数()
        freq = 1
        # userの選択にartistが含まれているか確認(ここいらないかも)
        if len([artist for artist in user_selected if artist == artist_id]) == 0:
            continue
        # あるartistを選択しているuserの数(ここ改善の余地あり)
        selected_user = len(artist_to_user[artist_id])
        assert selected_user != 0, f"artist_idを見直してください {artist_id}"
        # あるuserがartistを選択している回数(ここは1回)
        num_selected = [artist for artist in user_selected if artist == artist_id]
        tf_user = len(num_selected)
        # 全ユーザからあるアーティストを選んでいるユーザの差(対数)
        idf_artist = math.log2(all_user_num / selected_user)
        right =  (tf_user * (k1 + 1)) / (tf_user + k1 * (1 - b + b * dl / aval))
        okapi = idf_artist * right * freq
        score += okapi
    return score
    
    
    