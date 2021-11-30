"""
search.py
Search Spotify for a given search_string. Returns search results.
"""
import json
from py4web import response

ERR_SEARCH_FOR_NULL = "(search_for) error: search_string null or empty"
ERR_VALIDATE_SEARCH_NULL = "(validate_and_search) error: request is null"
ERR_VALIDATE_SEARCH_NO_QUERY = "(validate_and_search) error: no query parameters found"
ERR_VALIDATE_SEARCH_NO_Q = "(validate_and_search) error: query parameter 'q' not found in request"
ERR_VALIDATE_SEARCH_BAD_Q = "(validate_and_search) error: query parameter 'q' null or empty"
ERR_VALIDATE_SEARCH_SEARCH_FOR_ERR = "(validate_and_search) error in search_for: search query (q) null or empty"
ERR_VALIDATE_SEARCH_NO_RESULTS = "(validate_and_search) error: no results found for search query: "

# Call the Spotify API with the validated query
# (this function is separated out for unit testing purposes)
def call_spotipy_search(sp, query):
	return sp.search(q=query, type='track')

# Validate the search string and call call_spotipy_search()
def search_for(sp, search_string):

	# If search_string is null or empty, return an error
	if search_string is None or len(search_string) == 0 or search_string.isspace():
		return ERR_SEARCH_FOR_NULL
		
	else:
		# Return 10 tracks found via search_string
		return call_spotipy_search(sp, search_string)

# Validate the request and call search_for()
def validate_and_search(sp, request):

	# If request is None, return appropriate error
	if request is None:
		response.status = 400
		return ERR_VALIDATE_SEARCH_NULL

	# If no query parameters are present, return appropriate error
	if request.query is None:
		response.status = 400
		return ERR_VALIDATE_SEARCH_NO_QUERY

	# If query parameter q is not present, return appropriate error
	if 'q' not in request.query:
		response.status = 400
		return ERR_VALIDATE_SEARCH_NO_Q

	# If query parameter q is null, empty, or only whitespace, return appropriate error
	if len(request.query.get('q')) == 0 or request.query.get('q').isspace() is True:
		response.status = 400
		return ERR_VALIDATE_SEARCH_BAD_Q

	# Preliminary error-checking ok - extract the value of query parameter q
	search_query = request.query.get('q')

	# Call search_for with the query parameter
	results = search_for(sp, search_query)

	# If the search query was null or empty (and errored out in search_for)
	if results == ERR_SEARCH_FOR_NULL:

		# Return error 400: bad request
		response.status = 400
		return ERR_VALIDATE_SEARCH_SEARCH_FOR_ERR

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
			return ERR_VALIDATE_SEARCH_NO_RESULTS + search_query