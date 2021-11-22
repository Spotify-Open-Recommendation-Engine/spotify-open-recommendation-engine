"""
get_song_features.py
Get the features of a song 
Takes a paramter of 'tid'- track id of a song 
return a JSON of a songs audio features, popularity, and genres
""" 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .spotifyoauth import get_token
from ..common import session
import json

def get_song_features(tid):
    #get token 
    session['token_info'], authorized = get_token()
    if authorized:
        sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))

        #get features
        features = sp.audio_features(tid)

        #dictionary to hold seed info of audio features
        song_features={}
        song_features["target_danceability"] = features[0]['danceability']
        song_features["target_energy"] = features[0]['energy']
        song_features["target_key"] = features[0]['key']
        song_features["target_loudness"] = features[0]['loudness']
        song_features["target_mode"] = features[0]['mode']
        song_features["target_speechiness"] = features[0]['speechiness']
        song_features["target_instrumentalness"] = features[0]['instrumentalness']
        song_features["target_valence"] = features[0]['tempo']

        #get track info
        track_name = sp.track(tid)

        #set seed popularity 
        popularity = track_name['popularity']
        song_features["target_popularity"] = popularity

        #get genre by getting artist (no track genre available)
        artist_uri = track_name['album']['artists'][0]['id']
        artist = sp.artist(artist_uri)
        genres = artist['genres'] 

        #these are the valid genres seeds you are allowed to use returned from spotify endpoint 
        lg = sp.recommendation_genre_seeds()
        legal_genres = lg['genres']

        #take the interscetion of the artist genres and the valid genres 
        genres_set = set(genres)
        intersection = genres_set.intersection(legal_genres)
        sgenres = list(intersection)
        song_features["genres"] = sgenres
        
        #Make features dictionary into a JSON object
        song_features_json = json.dumps(song_features)
       
        return song_features_json

    else:
        return "(search_for) error: not authorized"
