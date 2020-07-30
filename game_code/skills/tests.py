"""
All tests for the skills library.
"""
import unittest

from game_code.factory import Factory
from game_code.skills import HarshLanguage


class TestHarshLanguage(unittest.TestCase):
    def test_use_action_base_damage_using_social(self):
        harsh_language_skill = HarshLanguage(base_value=0, dice_quantity=0, dice_max=0)
        creature1 = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe", stat_values={"social": 5}
        )
        creature2 = Factory().create_creature(creature_class="goblin", first_name="Charles", second_name="Brown")
        action = harsh_language_skill.use(creature1, creature2)
        self.assertEqual(5, action.damage())
