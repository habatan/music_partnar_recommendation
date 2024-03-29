# バックエンド処理全般

## 本体機能

### main.py
#### リクエスト処理系

| method | parameter | return json | describe |
| ------- | :------- | :------ | :------ |
| regist_user | user_name : str, password : str | user_id : str, regist_status : bool | ユーザ登録 |
| delete_user | user_id : str | delete_status : bool | ユーザ削除 |
| get_user_data | user_id : str | user_name : str, artist_ids : list, login_status : bool | ユーザ情報取得
| login_user（追加リリース） | user_name : str, password : str | user_id : str, login_status : bool | ログイン処理　|
| logout_user（追加リリース） | user_id : str |user_id : str, login_status : bool | ログアウト処理 | 
| regist_user_like_artist | user_id :str, artist_ids : list | like_artists : list, regist_status : bool | likeアーティストの登録 |
| delete_user_like_artist | user_id :str, artist_ids : list | like_artists : list, delete_status : bool| likeアーティストの登録解除 |
| find_similar_user（追加リリース） | user_id :str | user_ids : list | 音楽趣向が類似しているユーザ検索 |


#### 機能

| method | argument | return | describe |
| ------- | :------- | :------ | :------ |
| user_db_login_status | user_id : str | login_status : bool | user_dbログイン状態確認　| 
| user_db_regist | user_id : str, user_name : str, pass_word : list | regist_status : bool |user_dbにuser_idを登録 |
| user_db_delete | user_id : str | delete_status : bool |user_dbからuser_idを削除 |
| user_db_check | user_id : str | delete_status : bool | user_dbにuser_idがあるか確認 |
| fav_artist_regist | user_id : str, favorite_artists : list | regist_status : bool, favorite_artists : list | favorite_artist_dbにアーティストを登録 |
| fav_artist_delete | user_id : str, favorite_artists : list | delete_status : bool, favorite_artists : list | favorite_artist_dbからアーティストの登録解除 |
| fav_artist_check | user_id : str | favorite_artists : list | user_idの登録済みアーティスト取得 |

***

## モジュール・メソッド一覧

### spotify_tool.py

| method | argument | describe |
| ------- | :------- | -------
| get_access_token | client_id : str, secret_key : str | アクセストークン取得 |
| get_related_artists | access_token : str, artist_id : str | 類似性の高いアーティスト取得 |

### models/models.py

#### UserList

| method | argument | describe |
| ------- | :------- | :------ |
| add_user | user_id :str, display_name : str, mail_address : str, pass_word : str | databaseにuserのレコード追加 |
| delete_user | display_name : str | databaseからuserのレコードを削除 |
| get_user_all | user_id : str | databaseからすべてのuserレコードを取得 |

#### FavArtistList

| method | argument | describe |
| ------- | :------- | :------ |
| add | user_id : str, fav_artist : str, main_flag : str | userのfav_artist_idをdatabaseに追加 |
| delete_user_fav_artist | user_id : str, user_token : str | databaseからuserのfav_artist_idを削除 |
| get_all_main_fav_artist | user_id : str | userが選択したfav_artist_idを取得 |
| get_all_sub_fav_aritist | user_id : str, users_list : list | userが選択したfav_artist_idに関連するartist_idを取得 |
| get_user_fav_all | user_id : str | datebaseにおけるuserのすべてのデータを取得 |

#### SimUserList（追加リリース）

| method | argument | describe |
| ------- | :------- | :------ |
| add_sim_user | target_user_id : str, sim_user :str | target_userに近いuser_idを追加 |
| delete_users_data | target_user_id :str | target_userのレコードを削除 |
| get_sim_user_all | user_id : str | databaseからtarget_userの全sim_userレコードを取得 |

***

## APIエンドポイント

| methods | endpoint | parameter | return json |
| ------- | :------- | ---- | ---- |
| POST | /club_app_api/v1/regist_user | user_name, password | user_id, regist_status |
| GET | /club_app_api/v1/get_user_data/ | user_id | user_name, similar_users, favorite_artists, login_status |
| POST（追加リリース） | /club_app_api/v1/login_user | user_name, password | user_id, login_status |
| POST（追加リリース） | /club_app_api/v1/logout_user | user_id | logout_status |
| POST | /club_app_api/v1/{user_id}/regist_user_favartist | user_id, favorite_artists | favorite_artists, regist_status |
| POST | /club_app_api/v1/{user_id}/delete_user | user_id | delete_status |
