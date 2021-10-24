"""
spotifyoauth.py
Functions to facilitate user login via Spotify.
"""
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from py4web import request, redirect
from ..common import session

client_id = "redacted"
client_secret = "redacted"
redirect_uri = "http://localhost:8000/spotify-open-recommendation-engine/api_callback"
scope = "user-library-read"

# User logs in and authorizes access
def do_oauth():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    auth_url = sp_oauth.get_authorize_url()
    redirect(auth_url)
    return dict()

# Request refresh/access tokens and save to session
def do_callback():
    session.clear()
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    code = request.query.get('code')
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    redirect("index")
    return dict()

# Checks to see if token is valid and gets a new token if not
def get_token():
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get("token_info", False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session["token_info"]["expires_at"] - now < 60

    # Refresh token if expired
    if is_token_expired:
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))
    token_valid = True
    return token_info, token_valid
