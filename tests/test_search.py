"""
test_search.py
Unit test the search.py script.
"""
import json
import os
import unittest
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

JSON_FILENAME = os.path.join(os.path.dirname(__file__), 'resources/fake_search_result.json')
JSON_MIN_FILENAME = os.path.join(os.path.dirname(__file__), 'resources/fake_search_result_min.json')

class TestSearch(unittest.TestCase):

    # TEST: search_for() with valid input
    # Should return: valid JSON
    @patch("scripts.search.call_spotipy_search")
    def test_search_01_search_for_valid_input(self, mock_search_response):
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
    def test_search_02_search_for_empty_input(self):
        sp = Mock()
        q = ""
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual

    # TEST: search_for() with whitespace input
    # Should return: ERR_SEARCH_FOR_NULL
    # (no need to patch here, because call_spotipy_search() should NOT get called)
    def test_search_03_search_for_whitespace_input(self):
        sp = Mock()
        q = "          "
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual
    
    # TEST: search_for() with no input
    # Should return: ERR_SEARCH_FOR_NULL
    # (no need to patch here, because call_spotipy_search() should NOT get called)
    def test_search_04_search_for_no_input(self):
        sp = Mock()
        q = None
        expected = ERR_SEARCH_FOR_NULL
        actual = search_for(sp, q)
        assert expected == actual

    # TEST: validate_and_search() with valid input
    # Should return: JSON w/ properties: track_id, track_name, track_artist, track_album
    @patch("scripts.search.call_spotipy_search")
    def test_search_05_validate_and_search_valid_input(self, mock_search_response):
        with patch("py4web.request") as patched_request: 
                sp = Mock()
                # Create a query payload for our fake request
                patched_request.query = {"q":"As+Tall+As+Lions"}

                # Read JSON files from resources/ to populate mocked & expected search results
                fp0 = open(JSON_FILENAME)
                fp1 = open(JSON_MIN_FILENAME)
                JSON_RESULTS = json.load(fp0)
                JSON_RESULTS_MIN = fp1.read()
                fp0.close()
                fp1.close()
                
                # "Call" validate_and_search() with our fake request & trim the mocked result (handled by validate_and_search)
                mock_search_response.return_value = JSON_RESULTS
                expected = JSON_RESULTS_MIN
                actual = validate_and_search(sp, patched_request)

                assert mock_search_response.called
                assert expected == actual
                
    # TEST: validate_and_search() with null request
    # Should return: ERR_VALIDATE_SEARCH_NULL
    def test_search_06_validate_and_search_null_request(self):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            patched_request = None
            expected = ERR_VALIDATE_SEARCH_NULL
            actual = validate_and_search(sp, patched_request)
            assert expected == actual

    # TEST: validate_and_search() with no query in request
    # Should return: ERR_VALIDATE_SEARCH_NO_QUERY
    def test_search_07_validate_and_search_empty_query(self):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            patched_request.query = None
            expected = ERR_VALIDATE_SEARCH_NO_QUERY
            actual = validate_and_search(sp, patched_request)
            assert expected == actual

    # TEST: validate_and_search() with no query param 'q' in request
    # Should return: ERR_VALIDATE_SEARCH_NO_Q
    def test_search_08_validate_and_search_no_q(self):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            patched_request.query = {"message":"these aren't the droids you're looking for"}
            expected = ERR_VALIDATE_SEARCH_NO_Q
            actual = validate_and_search(sp, patched_request)
            assert expected == actual

    # TEST: validate_and_search() with empty query param 'q' in request
    # Should return: ERR_VALIDATE_SEARCH_BAD_Q
    def test_search_09_validate_and_search_empty_q(self):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            patched_request.query = {"q":""}
            expected = ERR_VALIDATE_SEARCH_BAD_Q
            actual = validate_and_search(sp, patched_request)
            assert expected == actual

    # TEST: validate_and_search() with error in call to search_for()
    # Should return: ERR_VALIDATE_SEARCH_SEARCH_FOR_ERR
    @patch("scripts.search.search_for")
    def test_search_10_validate_and_search_search_for_err(self, mock_search_for):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            patched_request.query = {"q":"something interesting"}
            mock_search_for.return_value = ERR_SEARCH_FOR_NULL
            expected = ERR_VALIDATE_SEARCH_SEARCH_FOR_ERR
            actual = validate_and_search(sp, patched_request)
            assert expected == actual

    # TEST: validate_and_search() with no results
    # Should return: ERR_VALIDATE_SEARCH_NO_RESULTS
    @patch("scripts.search.search_for")
    def test_search_11_validate_and_search_no_results(self, mock_search_for):
        with patch("py4web.request") as patched_request:
            sp = Mock()
            query_words = "a duck walked up to a lemonade stand"
            patched_request.query = {"q":query_words}
            mock_search_for.return_value = None
            expected = ERR_VALIDATE_SEARCH_NO_RESULTS + query_words
            actual = validate_and_search(sp, patched_request)
            assert expected == actual