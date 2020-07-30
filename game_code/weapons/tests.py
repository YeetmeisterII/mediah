"""
All tests for the weapons library.
"""
import unittest

from game_code.weapons import Sword


class TestWeapon(unittest.TestCase):
    def test_weapon_has_name_changed_false(self):
        sword = Sword(base_value=0, dice_max=0, dice_quantity=0, value=0, weight=0)
        self.assertEqual("Sword", sword.name())
        self.assertEqual(False, sword.has_name_changed())

    def test_weapon_renamed_at_instantiation(self):
        sword = Sword(name="test name", base_value=0, dice_max=0, dice_quantity=0, value=0, weight=0)
        self.assertEqual("test name (Sword)", sword.name())
        self.assertEqual(True, sword.has_name_changed())

    def test_weapon_renamed_after_instantiation(self):
        sword = Sword(base_value=0, dice_max=0, dice_quantity=0, value=0, weight=0)
        self.assertEqual("Sword", sword.name())
        sword.change_name("test name")
        self.assertEqual("test name (Sword)", sword.name())
        self.assertEqual(True, sword.has_name_changed())
