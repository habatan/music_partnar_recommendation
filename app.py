# Flask application
from flask import Flask
import os
import dotenv
dotenv.load_dotenv("../_info/.env")

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
artist_id = "6U3ybJ9UHNKEdsH7ktGBZ7"
