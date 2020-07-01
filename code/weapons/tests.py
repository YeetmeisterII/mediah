import unittest

from code.actions import AttackAction
from code.creatures import Creature
from code.weapons import Weapon


class TestWeaponMethods(unittest.TestCase):
    def test_weapon_rename(self):
        weapon = Weapon()
        self.assertEqual(weapon.name(), "default weapon")
        weapon.change_name("modified name")
        self.assertEqual(weapon.name(), "modified name ()")

    def test_use_action_type(self):
        weapon = Weapon()
        action = weapon.use(Creature(), Creature())
        self.assertEqual(type(action), AttackAction)

    def test_use_action_executor(self):
        weapon = Weapon()
        creature1 = Creature()
        creature2 = Creature()
        action = weapon.use(creature1, creature2)
        self.assertEqual(action.executor(), creature1)

    def test_use_action_target(self):
        weapon = Weapon()
        creature1 = Creature()
        creature2 = Creature()
        action = weapon.use(creature1, creature2)
        self.assertEqual(action.target(), creature2)
