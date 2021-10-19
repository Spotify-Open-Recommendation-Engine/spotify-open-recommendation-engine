"""
spotifyoauth.py
Functions to facilitate user login via Spotify.
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def do_oauth():

    # Define the scope of authorization to request
    scope = "user-library-read"

    # Grab these two fields from the Spotify Developer Dashboard
    client_id = "nope"
    client_secret = "nope"

    # The redirect URL must match the value set on the Spotify Developer Dashboard
    redirect_uri = "http://localhost:8080"    

    # Call Spotipy's OAuth function; bounce to the browser (redirect_uri) to login with Spotify and prompt the authorization request (scope)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # Bonus: get & print the user's saved/liked tracks (just to prove that we could login & retrieve their data)
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
