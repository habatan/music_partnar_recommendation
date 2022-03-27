# 類似ユーザ探索API

## API本体機能

### app.py

| method | argument | describe |
| ------- | :------- | :------ |
| make_artist_data | artist_ids : list | userが選択したアーティストからspotify_toolを用いて,それに関連するアーティスを含めた情報を作成 |
| find_similar_user | user_id :str | fav_db内の他のuser情報から音楽性が似ているuserを計算し, 発見する. |
| get_user_data | user_id : str, artist_list : list | fav_dbに置けるuser情報を取得 |
| regist_user_data | user_id : str | fav_dbにuserレコードを作成 |
| delete_user_data | user_id : str | fav_dbからuserレコードを削除 |

***

## モジュール・メソッド一覧

### spotify_tool.py

| method | argument | describe |
| ------- | :------- | -------
| get_access_token | client_id : str, secret_key : str | アクセストークン取得 |
| get_related_artist | artist_id : str | 類似性の高いアーティスト取得 |

### db_manager.py

| method | argument | describe |
| ------- | :------- | :------ |
| check_user_id | user_id : str | fav_dbにuserIDが登録されているか確認 |
| create_recordt | user_id :str | fav_dbにuserのレコードを作成 |
| delete_record | user_id : str | fav_dbからuserのレコードを削除 |
| set_artist_data | user_id : str, artist_list : list | fav_dbにuserと音楽性が似ているアーティスト情報を格納 |
| set_similar_user | user_id : str, users_list : list | fav_dbにuserに似たuser情報を格納 |
| get_user_record | user_id : str | fav_dbからuserのレコードを取得 |

***

## APIエンドポイント

| methods | endpoint | data |
| ------- | :------- | :--- |
| POST | /club_app_api/v1/get_user_data | user_id |
| POST | /club_app_api/v1/regist_user_data | user_id, favarite_aritsts |
| POST | /club_app_api/v1/delete_user_data | user_id |
