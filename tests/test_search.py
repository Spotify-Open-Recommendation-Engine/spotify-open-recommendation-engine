"""
test_search.py
Unit test the search.py script.
"""

import json
import time
import unittest
from py4web import request, response
from unittest.mock import Mock, patch
from scripts.search import search_for, validate_and_search

class TestSearch(unittest.TestCase):

    # We mock the things that we need but cannot have
    def setUp():
        result = "not modified yet"
        search_for("blah")

    def do_mock_get_token():
        result = "fake_token_info", True

    @patch('spotifyoauth.get_token()', side_effect=do_mock_get_token())
    def mock_get_token():
        print(result)

    # TEST: search_for() with valid input
    # (search_for() is in search.py)
    # Should return: 
    @patch()
    def test_search_for_valid_input():
        return True

    # TEST: search_for() with bad input
    # Should return ...
    def test_search_for_bad_input():
        return True

    # TEST: search_for() with no input
    # Should return ...
    def test_search_for_no_input():
        return True

    # TEST: search_for(), but w/o proper auth
    # Should return: '(search_for) error: not authorized'
    def test_search_for_unauthorized():
        return True

    # TEST: validate_and_search() with valid input
    # (sp_search() is in controllers.py)
    # Should return: JSON w/ properties: track_id, track_name, track_artist, track_album
    def test_validate_and_search_valid_input():
        return True

    # TEST: validate_and_search() with bad input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    def test_validate_and_search_bad_input():
        return True

    # TEST: validate_and_search() with no input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    def test_validate_and_search_no_input():
        return True

    # TEST: validate_and_search(), but w/o proper auth
    # Should return: '(sp_search) error: not authorized' (403)
    def test_validate_and_search_unauthorized():
        return True
