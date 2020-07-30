"""
All tests for the status library.
"""
import unittest

from game_code.status import Block, Status


class TestStatus(unittest.TestCase):
    def test_contains(self):
        status = Status()
        effect = Block()
        status._effects = [effect]
        self.assertTrue(Block in status)

    def test_does_not_contain(self):
        status = Status()
        status._effects = []
        self.assertFalse(Block in status)

    def test_is_blocking(self):
        status = Status()
        effect = Block()
        status._effects = [effect]
        self.assertTrue(status.is_blocking())

    def test_is_not_blocking(self):
        status = Status()
        status._effects = []
        self.assertFalse(status.is_blocking())
