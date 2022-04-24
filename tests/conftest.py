# import pytest
# from club_activity_app.app import create_app

# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })

#     # other setup can go here

#     return app

#     # clean up / reset resources here


# @pytest.fixture()
# def client(app):
#     return app.test_client()


# # "/"でログイン処理が行われ, sessionを用いてlogged_in情報を保存している
# # postリクエストを投げる関数
# def login(client, login_id, password):
#     return client.post("/", data=dict(login_id=login_id, password=password), follow_redirets=True)

# # テスト例
# def test_login(client):
#     with client:
#         # login success test
#         rv = login(client, "admin", "password")
#         assert b"Menu" in rv.data
#         assert session["logged_in"]
#         # login erro test
#         rv = login(client, "none", "none")
#         assert b"Not logged in" in rv.data
#         assert "logged_in" not in session 
