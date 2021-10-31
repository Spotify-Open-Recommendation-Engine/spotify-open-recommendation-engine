""" 
get_song_features.py
return a dictionary of target audio features + popularity, and the seed genre
params: tid - track_id
""" 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .spotifyoauth import get_token
from ..common import session

def get_song_features(tid):
    #get token 
    session['token_info'], authorized = get_token()
    if authorized:
        sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))

        #get features
        features = sp.audio_features(tid)
        
        #dictionary to hold seed info of audio features
        playlist_seed={}
        playlist_seed["target_danceability"] = features[0]['danceability']
        playlist_seed["target_energy"] = features[0]['energy']
        playlist_seed["target_key"] = features[0]['key']
        playlist_seed["target_loudness"] = features[0]['loudness']
        playlist_seed["target_mode"] = features[0]['mode']
        playlist_seed["target_speechiness"] = features[0]['speechiness']
        playlist_seed["target_instrumentalness"] = features[0]['instrumentalness']
        playlist_seed["target_valence"] = features[0]['tempo']

        #get track info
        track_name = sp.track(tid)

        #set seed popularity 
        popularity = track_name['popularity']
        playlist_seed["target_popularity"] = popularity

        #get genre by getting artist (no track genre available)
        artist_uri = track_name['album']['artists'][0]['id']
        artist = sp.artist(artist_uri)
        genres = artist['genres'] 

        #these are the valid genres seeds you are allowed to use 
        lg = sp.recommendation_genre_seeds()
        legal_genres = lg['genres']

        #take the interscetion of the artist genres and the valid genres 
        genres_set = set(genres)
        intersection = genres_set.intersection(legal_genres)
        sgenres = list(intersection)

        return playlist_seed, sgenres
    return 

