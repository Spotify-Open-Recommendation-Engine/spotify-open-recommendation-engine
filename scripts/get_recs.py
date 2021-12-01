"""
get_recs.py
Input: 
    - sgenres: seed genre
    - limit: num of songs
    - target_attributes: a dictionary of target audio features
Output: returns a list of recommended tracks
"""
import spotipy
from .spotifyoauth import get_token
from ..common import session


def get_recs(sgenres, limit, target_attributes):
    # Get token from session
    session['token_info'], authorized = get_token()

    if authorized:
        sp = spotipy.Spotify(auth=session.get('token_info').get(
            'access_token'), requests_timeout=30)

        # Get recommended tracks by calling Spotify API
        recs = sp.recommendations(
            seed_genres=sgenres, limit=limit, country='US', **target_attributes)

        return recs

    else:
        return "error: not authorized"
