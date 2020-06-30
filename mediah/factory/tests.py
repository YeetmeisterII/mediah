import unittest

from mediah.creatures import Goblin
from mediah.factory import Factory
from mediah.weapons import Sword


# TODO: Add a test case to check the defaults of all creatures and weapons.
class TestCreatureCreationMethods(unittest.TestCase):
    def test_creature_creation(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(type(creature), Goblin)

    def test_default_creature_creation(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(creature.constitution(), 10)
        self.assertEqual(creature.physicality_base(), 5)
        self.assertEqual(creature.dexterity_base(), 10)
        self.assertEqual(creature.social(), 0)
        self.assertEqual(creature.gold_worth(), 5)
        self.assertEqual(creature.experience_worth(), 10)

    def test_custom_creature_stat(self):
        creature = Factory().create_creature("goblin", {"physicality": 7})
        self.assertEqual(creature.physicality_base(), 7)

    def test_weapon_creation(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual(type(weapon), Sword)

    def test_custom_weapon_stat(self):
        weapon = Factory().create_weapon("sword", {"base_value": 7})
        self.assertEqual(weapon.base_value(), 7)
