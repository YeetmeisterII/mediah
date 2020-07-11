import unittest

from game_code.actions import NullAction
from game_code.creatures import Creature
from game_code.status import Block, Status


class TestStatusMethods(unittest.TestCase):
    def test_effect_in_status(self):
        status = Status()
        effect = Block()
        status._effects = [effect]
        self.assertTrue(Block in status)

    def test_effect_not_in_status(self):
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

    def test_end_turn_actions(self):
        status = Status()
        creature = Creature()
        effect = Block()
        status._effects = [effect]
        responses = status.end_turn(self_creature=creature)
        self.assertEqual([NullAction], list(map(type, responses)))

    def test_end_turn_timed_out_effect(self):
        status = Status()
        creature = Creature()
        status._effects = [Block()]
        responses = status.end_turn(self_creature=creature)
        self.assertEqual(status._effects, [])

    def test_end_turn_non_timed_out_effect(self):
        status = Status()
        creature = Creature()
        effect = Block(turns=2)
        status._effects = [effect]
        responses = status.end_turn(self_creature=creature)
        self.assertEqual(status._effects, [effect])
