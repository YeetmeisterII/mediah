import unittest

from code.creatures import Creature
from code.weapons import Sword


class TestCreatureMethods(unittest.TestCase):
    def test_is_alive_above_zero(self):
        creature = Creature()
        creature._stats._health = 1
        self.assertEqual(1, creature.stats().health())
        self.assertEqual(True, creature.is_alive())

    def test_is_not_alive_at_zero(self):
        creature = Creature()
        creature._stats._health = 0
        self.assertEqual(0, creature.stats().health())
        self.assertEqual(False, creature.is_alive())

    def test_is_not_alive_below_zero(self):
        creature = Creature()
        creature._stats._health = -1
        self.assertEqual(-1, creature.stats().health())
        self.assertEqual(False, creature.is_alive())

    def test_full_name_without_second_name(self):
        creature = Creature(first_name="YeetmeisterII")
        self.assertEqual("YeetmeisterII", creature.full_name())

    def test_full_name_with_second_name(self):
        creature = Creature(first_name="YeetmeisterII", second_name="IGOR")
        self.assertEqual("YeetmeisterII IGOR", creature.full_name())

    def test_store_weapon_without_weapon(self):
        creature = Creature()
        creature._store_weapon()
        self.assertEqual([], creature._inventory)

    def test_store_weapon_with_weapon(self):
        creature = Creature()
        weapon = Sword()
        creature._weapon = weapon
        creature._store_weapon()
        self.assertEqual([weapon], creature._inventory)
