"""
search.py
Search Spotify for a given search_string. Returns search results.

input: search_string
output: search results from Spotify
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .spotifyoauth import get_token
from ..common import session

def search_for(search_string):

	# Get token from session
	session['token_info'], authorized = get_token()

	if authorized:
		sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))

	
		# Return (10) tracks found via search_string
		return sp.search(q=search_string, type='track')

	return "(search_for) error: not authorized"

