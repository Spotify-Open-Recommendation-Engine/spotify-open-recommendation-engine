"""
test_search.py
Unit test the search.py script.
"""

import json
import unittest
from py4web import request, response
from unittest.mock import Mock, MagicMock, patch
from scripts.search import search_for, validate_and_search

class TestSearch(unittest.TestCase):

    # We mock the things that we need but cannot have
 
    # TEST: search_for() with valid input
    # (search_for() is in search.py)
    # Should return: 
    @patch("scripts.search.call_spotipy_search")
    def test_search_for_valid_input(self, mock_search_response):
        sp = Mock()
        q = "Sleep+Token"
        mock_search_response.return_value = '{"message":"very cool json payload"}'

        expected = '{"message":"very cool json payload"}'
        actual = search_for(sp, q)
        assert mock_search_response.called
        assert expected == actual

    # TEST: search_for() with bad input
    # Should return ...
    # def test_search_for_bad_input():
    #     return True

    # TEST: search_for() with no input
    # Should return ...
    # def test_search_for_no_input():
    #     return True

    # TEST: search_for(), but w/o proper auth
    # Should return: '(search_for) error: not authorized'
    # def test_search_for_unauthorized():
    #     return True

    # TEST: validate_and_search() with valid input
    # (sp_search() is in controllers.py)
    # Should return: JSON w/ properties: track_id, track_name, track_artist, track_album
    # def test_validate_and_search_valid_input():
    #     return True

    # TEST: validate_and_search() with bad input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    # def test_validate_and_search_bad_input():
    #     return True

    # TEST: validate_and_search() with no input
    # Should return: '(sp_search) error: search query (q) null or empty' (400)
    # def test_validate_and_search_no_input():
    #     return True

    # TEST: validate_and_search(), but w/o proper auth
    # Should return: '(sp_search) error: not authorized' (403)
    # def test_validate_and_search_unauthorized():
    #     return True
