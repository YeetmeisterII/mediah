import unittest

from code.creatures import Creature


class TestCreatureMethods(unittest.TestCase):
    def test_is_alive_above_zero(self):
        creature = Creature()
        creature._stats._health = 1
        self.assertEqual(1, creature.stats().health())
        self.assertEqual(True, creature.is_alive())

    def test_is_not_alive(self):
        creature = Creature(constitution=0)
        self.assertEqual(creature.stats().health(), 0)
        self.assertEqual(False, creature.is_alive())

    def test_full_name_without_second_name(self):
        creature = Creature(first_name="YeetmeisterII")
        self.assertEqual("YeetmeisterII", creature.full_name())

    def test_full_name_with_second_name(self):
        creature = Creature(first_name="YeetmeisterII", second_name="IGOR")
        self.assertEqual("YeetmeisterII IGOR", creature.full_name())
