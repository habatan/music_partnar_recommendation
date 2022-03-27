# Flask application(API)
from flask import Flask, request
import modules.spotify_tools as spotify
import modules.db_manager as db
import os
import dotenv
dotenv.load_dotenv("../_info/.env")

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
artist_id = "6U3ybJ9UHNKEdsH7ktGBZ7"

app = Flask(__name__)

@app.route("/v1/get_user_data")
def get_user_data():
    user_id = request.form["user_id"]
    data = db.get_user_record(user_id)
    






