import unittest

from game_code.actions import AttackAction
from game_code.creatures import Creature
from game_code.weapons import Weapon


class TestWeaponMethods(unittest.TestCase):
    def test_weapon_rename(self):
        weapon = Weapon()
        self.assertEqual("default weapon", weapon.name())
        weapon.change_name("modified name")
        self.assertEqual("modified name ()", weapon.name())

    def test_use_action_type(self):
        weapon = Weapon()
        action = weapon.use(Creature(), Creature())
        self.assertEqual(AttackAction, type(action))

    def test_use_action_executor(self):
        weapon = Weapon()
        creature1 = Creature()
        creature2 = Creature()
        action = weapon.use(creature1, creature2)
        self.assertEqual(creature1, action.executor())

    def test_use_action_target(self):
        weapon = Weapon()
        creature1 = Creature()
        creature2 = Creature()
        action = weapon.use(creature1, creature2)
        self.assertEqual(creature2, action.target())
