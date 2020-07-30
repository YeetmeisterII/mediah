"""
All tests of the creatures library.
"""
import unittest

from game_code.creatures import Creature
from game_code.stats import Stats
from game_code.status import Status
from game_code.weapons import Unarmed


class TestCreature(unittest.TestCase):
    def test_is_alive_above_zero(self):
        weapon = Unarmed(base_value=0, dice_quantity=0, dice_max=0, weight=0, value=0)
        creature = Creature(first_name="John", second_name="Doe", stats=Stats(), status=Status(), weapon=weapon)
        creature._stats._health = 1
        self.assertEqual(1, creature.stats().health())
        self.assertEqual(True, creature.is_alive())

    def test_is_not_alive_at_zero(self):
        weapon = Unarmed(base_value=0, dice_quantity=0, dice_max=0, weight=0, value=0)
        creature = Creature(first_name="John", second_name="Doe", stats=Stats(), status=Status(), weapon=weapon)
        creature._stats._health = 0
        self.assertEqual(0, creature.stats().health())
        self.assertEqual(False, creature.is_alive())

    def test_is_not_alive_below_zero(self):
        weapon = Unarmed(base_value=0, dice_quantity=0, dice_max=0, weight=0, value=0)
        creature = Creature(first_name="John", second_name="Doe", stats=Stats(), status=Status(), weapon=weapon)
        creature._stats._health = -1
        self.assertEqual(-1, creature.stats().health())
        self.assertEqual(False, creature.is_alive())
