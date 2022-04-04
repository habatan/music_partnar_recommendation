# 類似ユーザ探索API

## 概要

club_activity_appのAPI機能

### API本体機能

#### app.py

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

### モジュール・メソッド一覧

#### spotify_tools.py

| method | argument | describe |
| ------- | :------- | -------
| get_access_token | client_id : str, secret_key : str | アクセストークン取得 |
| get_related_artists | access_token : str, artist_id : str | 類似性の高いアーティスト取得 |

#### db_manager.py

| method | argument | describe |
| ------- | :------- | :------ |
| check_user_id | user_id : str | fav_dbにuserIDが登録されているか確認 |
| create_recordt | user_id :str | fav_dbにuserのレコードを作成 |
| delete_record | user_id : str | fav_dbからuserのレコードを削除 |
| set_artist_data | user_id : str, artist_list : list | fav_dbにuserと音楽性が似ているアーティスト情報を格納 |
| set_similar_user | user_id : str, users_list : list | fav_dbにuserに似たuser情報を格納 |
| get_user_record | user_id : str | fav_dbからuserのレコードを取得 |

#### user_db.py

| method | argument | describe |
| ------- | :------ | :------ |
| register_user | user_id : str, display_name : str | line_idをuser_dbに登録 |
| delete_user | user_id : str | line_idをuser_dbから削除 |
| get_user_id | userid : str | user_idが存在するか確認 |
| get_user_display_name | user_id :str | 表示名を取得 |

***

### APIエンドポイント

| methods | endpoint | data | return |
| ------- | :------- | ---- | ---- |
| POST | /club_app_api/v1/get_user_data | user_id | similar_users, display_name |
| POST | /club_app_api/v1/regist_user_data | user_id, favarite_aritsts, display_name | bool(True, False) |
| POST | /club_app_api/v1/delete_user_data | user_id | bool(True, Flase)
