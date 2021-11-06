"""
get_recs.py
Input: 
    - sgenres: seed genre
    - limit: num of songs
    - country: country code
    - target_attributes: a dictionary of target audio features
Output: returns a list of recommended tracks, a list of song names, a list of track IDs
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .spotifyoauth import get_token
from ..common import session


def get_recs(sgenres, limit, target_attributes):
    # get token from session
    session['token_info'],authorized = get_token()
    print(get_token())
    if authorized:
        sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'), requests_timeout=30, retries=3)
        # get recommended tracks 
        recs = sp.recommendations(seed_genres=sgenres, limit=limit, country='US', **target_attributes)

        # get song names and track IDs of the recommended tracks
        song_names = []
        track_ids = []
        for idx, track in enumerate(recs['tracks']):
            song_names.append(track['name'])
            track_ids.append(track['id'])
            
        return recs, song_names, track_ids
