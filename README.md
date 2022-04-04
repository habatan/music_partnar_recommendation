# バックエンド処理全般

## 本体機能

### app.py

| method | argument | describe |
| ------- | :------- | :------ |
| make_artist_data | artist_ids : list | userが選択したアーティストからspotify_toolを用いて,それに関連するアーティスを含めた情報を作成 |
| find_similar_user | user_id :str | fav_db内の他のuser情報から音楽性が似ているuserを計算し, 発見する. |
| get_user_data | user_id : str, artist_list : list | fav_dbに置けるuser情報を取得 |
| regist_user_data | user_id : str | fav_dbにuserレコードを作成 |
| delete_user_data | user_id : str | fav_dbからuserレコードを削除 |
| user_db_regist | user_id : str | user_dbにuser_idを登録 |
| user_db_check | user_id : str | user_dbからuser_idがあるか確認 |

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
| delete_user_fav_artist | user_id : str | databaseからuserのfav_artist_idを削除 |
| get_all_main_fav_artist | user_id : str | userが選択したfav_artist_idを取得 |
| get_all_sub_fav_aritist | user_id : str, users_list : list | userが選択したfav_artist_idに関連するartist_idを取得 |
| get_user_fav_all | user_id : str | datebaseにおけるuserのすべてのデータを取得 |

#### SimUserList

| method | argument | describe |
| ------- | :------- | :------ |
| add_sim_user | target_user_id : str, sim_user :str | target_userに近いuser_idを追加 |
| delete_users_data | target_user_id :str | target_userのレコードを削除 |
| get_sim_user_all | user_id : str | databaseからtarget_userの全sim_userレコードを取得 |

#### user_db.py

| method | argument | describe |
| ------- | :------ | :------ |
| register_user | user_id : str, display_name : str | line_idをuser_dbに登録 |
| delete_user | user_id : str | line_idをuser_dbから削除 |
| get_user_id | userid : str | user_idが存在するか確認 |
| get_user_display_name | user_id :str | 表示名を取得 |

***

## APIエンドポイント

| methods | endpoint | data | return |
| ------- | :------- | ---- | ---- |
| POST | /club_app_api/v1/get_user_data | user_id | similar_users, display_name |
| POST | /club_app_api/v1/regist_user_data | user_id, favarite_aritsts, display_name | bool(True, False) |
| POST | /club_app_api/v1/delete_user_data | user_id | bool(True, Flase)
