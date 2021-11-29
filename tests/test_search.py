"""
test_search.py
Unit test the search.py script.
"""
import unittest
from boddle import boddle
from py4web import request, response
from unittest.mock import Mock, patch
from scripts.search import search_for, validate_and_search

ERR_SEARCH_FOR_NULL = "(search_for) error: search_string null or empty"
ERR_VALIDATE_SEARCH_NULL = "(validate_and_search) error: request is null"
ERR_VALIDATE_SEARCH_NO_QUERY = "(validate_and_search) error: no query parameters found"
ERR_VALIDATE_SEARCH_NO_Q = "(validate_and_search) error: query parameter 'q' not found in request"
ERR_VALIDATE_SEARCH_BAD_Q = "(validate_and_search) error: query parameter 'q' null or empty"
ERR_VALIDATE_SEARCH_SEARCH_FOR_ERR = "(validate_and_search) error in search_for: search query (q) null or empty"
ERR_VALIDATE_SEARCH_NO_RESULTS = "(validate_and_search) error: no results found for search query: "
VALID_JSON_RESPONSE = '{"message":"very cool json payload"}'

class TestSearch(unittest.TestCase):

    # TEST: search_for() with valid input
    # Should return: valid JSON
    @patch("scripts.search.call_spotipy_search")
    def test_0_search_for_valid_input(self, mock_search_response):
        sp = Mock()
        q = "Sleep+Token"
        # Our fake params for search_for() are valid - mock a valid JSON response from call_spotipy_search()
        mock_search_response.return_value = VALID_JSON_RESPONSE
        expected = VALID_JSON_RESPONSE
        # search_for() calls call_spotipy_search(), which is mocked out - return the mock JSON response from above
        actual = search_for(sp, q)
        assert mock_search_response.called
        assert expected == actual

    # TEST: search_for() with empty input
    # Should return: ERR_SEARCH_FOR_NULL
    # (no need to patch here, because call_spotipy_search() should NOT get called)
    def test_1_search_for_empty_input(self):
        sp = Mock()
        q = ""
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual

    # TEST: search_for() with whitespace input
    # Should return: ERR_SEARCH_FOR_NULL
    # (no need to patch here, because call_spotipy_search() should NOT get called)
    def test_2_search_for_whitespace_input(self):
        sp = Mock()
        q = "          "
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual
    
    # TEST: search_for() with no input
    # Should return: ERR_SEARCH_FOR_NULL
    # (no need to patch here, because call_spotipy_search() should NOT get called)
    def test_3_search_for_no_input(self):
        sp = Mock()
        q = None
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual

    # TEST: validate_and_search() with valid input
    # Should return: JSON w/ properties: track_id, track_name, track_artist, track_album
    # Uses boddle to 
    # @patch("scripts.search.call_spotipy_search")
    # def test_4_validate_and_search_valid_input(self, mock_search_response):
    #     with boddle(query={"q":"As+Tall+As+Lions"}) as r:
    #         sp = Mock()
    #         #r = boddle(query={'q':'As+Tall+As+Lions'})
    #         # r.query_string = "q=Sleep+Token"
    #         mock_search_response.return_value = VALID_JSON_RESPONSE

    #         print("DEBUG:")
    #         print(r)
    #         #print(r.query)

    #         expected = VALID_JSON_RESPONSE
    #         actual = validate_and_search(sp, r)

    #         print(actual)

    #         assert mock_search_response.called
    #         assert expected == actual

    # TEST: validate_and_search() with bad input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    #def test_validate_and_search_bad_input():
    #     return True

    # TEST: validate_and_search() with no input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    #def test_validate_and_search_no_input():
    #     return True

