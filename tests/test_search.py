"""
test_search.py
Unit test the search.py script.
"""

import json
import spotipy
import unittest
from py4web import request, response
from unittest import mock
from ..common import session
from ..controllers import sp_search
from ..scripts.search import search_for

class TestSearch(unittest.TestCase):

    # TEST: search_for() with valid input
    # Should return ...
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

    # TEST: sp_search() with valid input
    # Should return ...
    def test_sp_search_valid_input():
        return True

    # TEST: sp_search() with bad input
    # Should return ...
    def test_sp_search_bad_input():
        return True

    # TEST: sp_search() with no input
    # Should return ...
    def test_sp_search_no_input():
        return True
