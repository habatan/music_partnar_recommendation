from http import client
import dotenv
from oauthlib.oauth2 import WebApplicationClient
import requests
import os
dotenv.load_dotenv("../_info/.env")

headers = {'Authorization':'Bearer BQAXLC10e9cvUYL1tXWthCbf8fL2ZDrwJR1jX_ttaapK3yEwx-ImiCXIFmpe-usA9nKQNk-oSxOOPpSq0b_-8ocBTw1cVPzpeSNkuKX5rEYyXgTR3DqDaF1reL6TwZhaaGAL1OvH-c3E2mxOsswiqMf3PFRx9Rk','Content-Type': 'application/json','Accept': 'application/json'}
response = requests.get('https://api.spotify.com/v1/artists/6U3ybJ9UHNKEdsH7ktGBZ7/related-artists', headers=headers)
print(response.status_code) 



