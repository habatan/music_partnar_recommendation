# Flask application(API)
from flask import Flask, request, jsonify
from modules.models.models import *
from modules.spotify_tools import *
import dotenv
dotenv.load_dotenv("../_info/.env")

# テストの際はspotifyのログイン情報を取らない
# CLIENT_ID = os.environ["CLIENT_ID"]
# CLIENT_SECRET = os.environ["CLIENT_SECRET"]
# ACCESS_TOKEN = spotify.get_access_token(CLIENT_ID, CLIENT_SECRET)
# test_artist_id = "6U3ybJ9UHNKEdsH7ktGBZ7"

def create_app(config="development"):
    # instance_relative_config : 相対的なconfigファイルを指定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="test_secret"
    )

    # configファイル : https://qiita.com/nanakenashi/items/e272ff1aafb3889230bc
    if config == "test":
        app.config.from_object("config.TestingConfig")
    elif config == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif config == "base":
        app.config.from_object("config.BaseConfig")
    
    # SQLAlchemy
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    user_list = UserList()

    @app.route("/v1/get_user_data", methods=["POST"])
    def get_user_data():
        return
    
    @app.route("/v1/regist_user_data", methods=["POST"])
    def regist_user_data():
        """
        Summary:
            新規ユーザの登録.
        Args:
            display_name: ユーザ名
            pass_word: パスワード
        """
        # リクエスト受け取り
        # JSONを受け取る
        print(request.get_json)
        json = request.get_json()
        display_name = json["display_name"]
        pass_word = json["pass_word"]
        print(json)
        
        # 既存である場合　登録済みエラー
        is_known = User.query.filter_by(user_name=display_name).first()
        if is_known != None:
            return jsonify({"user_id": None})
        
        pass_word = pass_word
        user_id = "#good"

        # 登録
        user_list.add_user(
            user_token=user_id,
            display_name=display_name,
            pass_word=pass_word
        )

        return jsonify({"user_id": user_id})

    @app.route("/v1/delete_user_data", methods=["POST"])
    def delete_user_data():
        return

    def make_artist_data():
        return

    def find_similar_user():
        return
    
    return app

