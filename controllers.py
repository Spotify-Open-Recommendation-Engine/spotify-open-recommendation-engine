"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from py4web import action, request, response, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from .scripts.spotifyoauth import do_oauth, do_callback, get_token
from .scripts.get_recs import get_recs

import spotipy


@unauthenticated("index", "index.html")
@action.uses(session)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}

    session['token_info'], authorized = get_token()
    if authorized:
        sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
        results = sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
        # print(token_info)
    
    return dict(message=message, actions=actions)

@unauthenticated("recommendations", "recommendations.html")
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    return dict(message=message, actions=actions)

@unauthenticated("search", "search.html")
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    return dict(message=message, actions=actions)

@action("login")
@action.uses(session)
def login():
    return do_oauth()

@action("api_callback")
@action.uses(session)
def api_callback():
    return do_callback()

@action("playlist")
@action.uses(session) 
def playlist(songs):
    return create_playlist(songs)

@action("song_features")
@action.uses(session)
def song_features(tid):
    return get_song_features(tid)

@action("recs")
@action.uses(session)
def recs():
    limit = 10 # default limit value
    if validate_parameter(request.query, 'limit'):
        limit = int(request.query.get('limit'))
    if not validate_parameter(request.query, 'sgenres'):
        response.status = 400
        return "(recs) error: sgenres expected"
    sgenres = request.query.get('sgenres').split(',')
    attribute_params = ["tempo", "key", "popularity", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence"]
    target_attributes = {}
    for attribute_param in attribute_params:
        if validate_parameter(request.query, attribute_param):
            param_range = request.query.get(attribute_param).split(',')
            if len(param_range) != 2:
                response.status = 400
                return "(recs) error: invalid format for " + attribute_param + " expected 'min,max'"
            target_attributes.update({"min_" + attribute_param: float(param_range[0]), "max_" + attribute_param: float(param_range[1])})
            
            
    return get_recs(sgenres, limit, target_attributes)

def validate_parameter(query, param):
    return param in request.query and len(request.query.get(param)) != 0 and request.query.get(param).isspace() is False