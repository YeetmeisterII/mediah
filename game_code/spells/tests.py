"""
All tests for the spells library.
"""
import unittest

from game_code.factory import Factory
from game_code.spells import Spell


class TestSpell(unittest.TestCase):
    def test_is_usable_magic_enabled_and_valid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": True, "magic_base": 10}
        )
        self.assertEqual(True, spell.is_usable(creature))

    def test_is_usable_magic_enabled_and_borderline_valid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": True, "magic_base": 1}
        )
        self.assertEqual(True, spell.is_usable(creature))

    def test_is_usable_magic_enabled_and_borderline_invalid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": True, "magic_base": 0}
        )
        self.assertEqual(False, spell.is_usable(creature))

    def test_is_usable_magic_enabled_and_invalid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": True, "magic_base": -10}
        )
        self.assertEqual(False, spell.is_usable(creature))

    def test_is_usable_magic_not_enabled_and_valid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": False, "magic_base": 10}
        )
        self.assertEqual(False, spell.is_usable(creature))

    def test_is_usable_magic_not_enabled_and_borderline_valid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": False, "magic_base": 1}
        )
        self.assertEqual(False, spell.is_usable(creature))

    def test_is_usable_magic_not_enabled_and_borderline_invalid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": False, "magic_base": 0}
        )
        self.assertEqual(False, spell.is_usable(creature))

    def test_is_usable_magic_not_enabled_and_invalid_mana(self):
        spell = Spell(cost=1)
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe",
            stat_values={"magic_enabled": False, "magic_base": -10}
        )
        self.assertEqual(False, spell.is_usable(creature))
