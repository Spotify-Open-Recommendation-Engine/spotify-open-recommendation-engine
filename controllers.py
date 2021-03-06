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
from .scripts.create_playlist import create_playlist
from .scripts.search import validate_and_search
from .scripts.get_song_features import get_song_features
import spotipy


@unauthenticated("index", "index.html")
@action.uses(session)
def index():
    session['token_info'],authorized = get_token()
    return dict(authorized=authorized)

@unauthenticated("recommendations", "recommendations.html")
@unauthenticated("search", "search.html")
@action.uses(session)
def require_login():
    session['token_info'],authorized = get_token()
    if not authorized:
        return redirect(URL('login'))
    return dict(authorized=authorized)


@action("login")
@action.uses(session)
def login():
    return do_oauth()

@action("logout")
@action.uses(session)
def logout():
    session.clear()
    return redirect(URL('index'))

@action("api_callback")
@action.uses(session)
def api_callback():
    return do_callback()

@action("create_playlist")
@action.uses(session)
def create_playlist_req():
    if not validate_parameter(request.query, 'songs'):
        response.status = 400
        return "(create_playlist) error: songs expected"
    songs = request.query.get('songs').split(',')
    if not validate_parameter(request.query, 'name'):
        response.status = 400
        return "(create_playlist) error: name expected"
    name = request.query.get('name')
    return create_playlist(name, songs)

@action("song_features")
@action.uses(session)
def song_features():
    if not validate_parameter(request.query, 'tid'):
        response.status = 400
        return "(song_features) error: track id (tid) expected"
    tid = request.query.get('tid')
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
            if attribute_param == "tempo" or attribute_param == "key" or attribute_param == "popularity":
                target_attributes.update({"min_" + attribute_param: int(param_range[0]), "max_" + attribute_param: int(param_range[1])})
            else:
                target_attributes.update({"min_" + attribute_param: float(param_range[0]), "max_" + attribute_param: float(param_range[1])})
            
    return get_recs(sgenres, limit, target_attributes)

def validate_parameter(query, param):
    return param in query and len(query.get(param)) != 0 and query.get(param).isspace() is False

@action("sp_search")
@action.uses(session)
def search():
    # Get token from session
    session['token_info'], authorized = get_token()

    # If the user is authorized, process the request
    if authorized:
	    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
	    return validate_and_search(sp, request)

    # Otherwise, return appropriate error
    response.status(403)
    return "error: not authorized"
