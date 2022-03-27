# Flask application(API)
from crypt import methods
from flask import Flask, request
import modules.spotify_tools as spotify
import modules.db_manager as db
import os
import dotenv
dotenv.load_dotenv("../_info/.env")

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
ACCESS_TOKEN = spotify.get_access_token(CLIENT_ID, CLIENT_SECRET)
test_artist_id = "6U3ybJ9UHNKEdsH7ktGBZ7"

app = Flask(__name__)

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






