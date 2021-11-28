"""
search.py
Search Spotify for a given search_string. Returns search results.

input: search_string
output: search results from Spotify
"""
import json
from py4web import response

def call_spotipy_search(sp, query):
	return sp.search(q=query, type='track')

# Call the Spotify API with the validated search_string
def search_for(sp, search_string):

	# If search_string is null or empty, return an error
	if search_string is None or len(search_string) == 0:
		return "(search_for) error: search_string null or empty"
		
	else:
		# Return 10 tracks found via search_string
		return call_spotipy_search(sp, search_string)

# Validate the request and call search_for()
def validate_and_search(sp, request):

	# Make sure some query parameter is present
	if request.query is not None:

		# Make sure query parameter q is present (and not null, empty, or only whitespace)
		if 'q' in request.query and len(request.query.get('q')) != 0 and request.query.get('q').isspace() is False:
				
			# Extract the value of query parameter q
			search_query = request.query.get('q')

			# Call search_for with the query parameter
			results = search_for(sp, search_query)

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