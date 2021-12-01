"""
test_recs.py
Unit test the get_recs.py script.
"""
import json
import os
import unittest
from py4web import request, response
from unittest.mock import Mock, patch
from scripts.get_recs import get_recs
