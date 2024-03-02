# Flask application(API)
from flask import Flask, request, jsonify
import secrets
from models import *

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
    
    user_list = UserList()
    user_like_artists_list = FavArtistList()
    sim_user_list = SimUserList()

    @app.route("/v1/regist_user_data", methods=["POST"])
    def regist_user_data():
        """
        Summary:
            新規ユーザの登録.
        Args:
            display_name: ユーザ名
            pass_word: パスワード
        """
        # JSONを受け取る
        json = request.get_json()
        display_name = json["display_name"]
        pass_word = json["pass_word"]
        regist_status = True
        # print(json)
        
        # 既存である場合　登録済みエラー
        is_known = User.query.filter_by(user_name=display_name).first()
        if is_known != None:
            regist_status = False
            return jsonify({"user_id": None, "regist_status":regist_status})
        
        # ユーザIDの作成
        user_id = secrets.token_hex()
        
        # DB挿入
        user_list.add_user(
            user_token=user_id,
            display_name=display_name,
            pass_word=pass_word
        )

        return jsonify({"user_id": user_id, "regist_status":regist_status})

    @app.route("/v1/get_user_data", methods=["POST"])
    def get_user_data():
        """
        Summary:
            ユーザ情報の取得.
        Args:
            display_name: ユーザ名
            pass_word: パスワード
        """
        return
    
    @app.route("/v1/delete_user_data", methods=["POST"])
    def delete_user_data():
        return

    def make_artist_data():
        return

    def find_similar_user():
        return

    return app



