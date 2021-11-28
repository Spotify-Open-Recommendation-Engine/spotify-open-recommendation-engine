"""
test_search.py
Unit test the search.py script.
"""

import json
import spotipy
import time
import unittest
from py4web import request, response
from unittest import mock
#from ..common import session
from controllers import sp_search
from scripts.search import search_for

class TestSearch(unittest.TestCase):

    # We mock the things that we need but cannot have
    def setUp():
        mock_session = Mock()
        mock_session["token_info"] = 'fake_info'
        mock_session["token_info"]["expires_at"] = int(time.time()) * 2
        mock_response = Mock()
        mock_response.return_value = '{"message:"hello"}'
        print(mock_session["token_info"]["expires_at"])

    # TEST: search_for() with valid input
    # (search_for() is in search.py)
    # Should return: 
    @mock.patch()
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

    # TEST: sp_search() with valid input
    # (sp_search() is in controllers.py)
    # Should return: JSON w/ properties: track_id, track_name, track_artist, track_album
    def test_sp_search_valid_input():
        return True

    # TEST: sp_search() with bad input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    def test_sp_search_bad_input():
        return True

    # TEST: sp_search() with no input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    def test_sp_search_no_input():
        return True

    # TEST: sp_search(), but w/o proper auth
    # Should return: '(sp_search) error: not authorized' (403)
    def test_sp_search_unauthorized():
        return True
