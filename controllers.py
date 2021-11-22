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
from .scripts.search import search_for
from .scripts.get_song_features import get_song_features
import json
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

@action("create_playlist")
@action.uses(session)
def create_playlist_req():
    if not validate_parameter(request.query, 'songs'):
        response.status = 400
        return "(create_playlist) error: songs expected"
    songs = request.query.get('songs').split(',')
    return create_playlist(songs)

@action("song_features")
@action.uses(session)
def song_features(tid):
    if request.query is not None:
        if not validate_parameter(request.query, 'tid'):
            response.status = 400
            return "(song_features) error: track id (tid) expected"
        tid = request.query.get('tid')
    	return get_song_features(tid)
    else:			
        response.status = 400 
        return "(song_features) error: missing parameters"

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

	# Make sure some query parameter is present
	if request.query is not None:

		# Make sure query parameter q is present (and not null, empty, or only whitespace)
		if 'q' in request.query and len(request.query.get('q')) != 0 and request.query.get('q').isspace() is False:
				
			# Extract the value of query parameter q
			search_query = request.query.get('q')

			# Call search_for with the query parameter
			results = search_for(search_query)

			# If the user is not authorized (session/token expired, not logged in, etc)
			if results == "(search_for) error: not authorized":

				# Return error 403: forbidden
				response.status = 403 
				return "(sp_search) error: not authorized"

			# If the search query was null or empty (and errored out in search_for)
			elif results == "(search_for) error: search_string null or empty":

				# Return error 400: bad request
				response.status = 400
				return "(sp_search) error in search_for: search query (q) null or empty"

			else:
				# Otherwise, if search_for returned some response:
				if results is not None:
					res = []
				
					# Loop through the response (JSON) and extract track id, name, artist, album
					for idx, result in enumerate(results['tracks']['items']):
						track_id = result['id']
						track_name = result['name']
						track_artist = result['artists'][0]['name']
						track_album = result['album']['name']
						
						# Append to an unalphabetized list (to preserve results' rank/order)
						res.append({
							"track_id":track_id, 
							"track_name":track_name, 
							"track_artist":track_artist, 
							"track_album":track_album
						})
					
					# Turn the extracted info into a JSON object and return it
					res_json = json.dumps(res)
					return res_json
				
				# If no results were found (unlikely), say so
				else:
					response.status = 404
					return "(sp_search) error: no results found for search query: ", search_query
					
		# If query parameter was not present, was empty, or was only whitespace, return an error
		else:
			response.status = 400
			return "(sp_search) error: search query (q) null or empty"
	
	# If we haven't returned anything by now, return an appropriate error
	else:			
		response.status = 400 
		return "(sp_search) error: no query parameters found"
