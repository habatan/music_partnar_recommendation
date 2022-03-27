# Spotify tools
import requests
import json

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
            artist_dict[artist_id] = artist_name
    except:
        artists = {}

    return artists
