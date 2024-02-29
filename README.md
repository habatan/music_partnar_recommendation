# バックエンド処理全般

## 本体機能

### app.py
#### リクエスト処理系

| method | parameter | return json | describe |
| ------- | :------- | :------ | :------ |
| regist_user | user_name : str, password : str | user_id : str | ユーザ登録 |
| delete_user | user_id : str | done : bool | ユーザ削除 |
| check_user | user_id : str | login : bool | ログイン状態確認　| 
| get_user_info | user_id : str | user_name : str, artist_ids : list | ユーザ情報取得
| login_user（追加リリース） | user_name : str, password : str | user_id : str, login : bool | ログイン処理　|
| logout_user（追加リリース） | user_id : str |user_id : str, login : bool | ログアウト処理 | 
| regist_user_like_artist | user_id :str, artist_ids : list | artist_ids : list | likeアーティストの登録 |
| find_similar_user（追加リリース） | user_id :str | user_ids : list | 音楽趣向が類似しているユーザ検索 |


#### 機能

| method | argument | return | describe |
| ------- | :------- | :------ | :------ |
| get_user | user_name : str, password : str | user_id : str, artist_ids : list | user_idを返す |
| retrieval_artists | artist_ids : list |  | 類似アーティスを含めた情報を返す |
| user_db_regist | user_id : str, user_name : str, pass_word : list |  |user_dbにuser_idを登録 |
| user_db_check | user_id : str |  | user_dbからuser_idがあるか確認 |

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

| methods | endpoint | data | return |
| ------- | :------- | ---- | ---- |
| GET | /club_app_api/v1/get_user_data/{user_id} | | similar_users, display_name, favorite_artists |
| POST（追加リリース） | /club_app_api/v1/login_user | mail_add, password | user_token |
| POST | /club_app_api/v1/regist_user_data | user_id, display_name, mail_add, password | bool(True, False) |
| POST | /club_app_api/v1/{user_id}/regist_user_favartist | user_token, favorite_artists | bool(True, False) |
| POST | /club_app_api/v1/{user_id}/delete_user_data | user_token | bool(True, Flase)
