"""
All tests for the response library.
"""
import unittest

from game_code.response import Response


class TestResponse(unittest.TestCase):
    def test_possessive_noun_conversion_not_ending_in_s(self):
        possessive = Response()._to_possessive_noun("John Doe")
        self.assertEqual("John Doe's", possessive)

    def test_possessive_noun_conversion_ending_in_s(self):
        possessive = Response()._to_possessive_noun("John Does")
        self.assertEqual("John Does'", possessive)

    def test_possessive_noun_conversion_blank_string(self):
        with self.assertRaises(ValueError) as cm:
            Response()._to_possessive_noun("")
