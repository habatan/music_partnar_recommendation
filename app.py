# Flask application(API)
from flask import Flask, request
from modules.models.models import *
from modules.spotify_tools import *
import os
import dotenv
dotenv.load_dotenv("../_info/.env")

# テストの際はspotifyのログイン情報を取らない
# CLIENT_ID = os.environ["CLIENT_ID"]
# CLIENT_SECRET = os.environ["CLIENT_SECRET"]
# ACCESS_TOKEN = spotify.get_access_token(CLIENT_ID, CLIENT_SECRET)
# test_artist_id = "6U3ybJ9UHNKEdsH7ktGBZ7"


def create_app(config="base"):
    # instance_relative_config : 相対的なconfigファイルを指定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="test_secret"
    )

    # configファイル : https://qiita.com/nanakenashi/items/e272ff1aafb3889230bc
    if config == "test":
        print("読み込まれてまっせ")
        app.config.from_object("config.TestingConfig")
    elif config == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif config == "base":
        app.config.from_object("config.BaseConfig")

    @app.route("/v1/get_user_data", methods=["POST"])
    def get_user_data():
        return

    @app.route("/v1/regist_user_data", methods=["POST"])
    def refist_user_data():
        return

    @app.route("/v1/delete_user_data", methods=["POST"])
    def delete_user_data():
        return

    def make_artist_data():
        return

    def find_similar_user():
        return
    
    return app

