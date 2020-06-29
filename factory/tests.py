import unittest

from mediah.creatures import Goblin
from mediah.factory import CreatureFactory, WeaponFactory
from mediah.weapons import Sword, Unarmed, Dagger


class TestCreatureCreationMethods(unittest.TestCase):
    def test_creature_creation(self):
        creature = CreatureFactory().create_creature("goblin")
        self.assertEqual(type(creature), Goblin)

    def test_custom_creature_stat(self):
        creature = CreatureFactory().create_creature("goblin", {"physicality": 7})
        self.assertEqual(creature.physicality_base(), 7)

    def test_default_weapon_assigned(self):
        creature = CreatureFactory().create_default_creature("goblin")
        self.assertEqual(type(creature.weapon()), Dagger)

    def test_default_weapon_not_assigned(self):
        creature = CreatureFactory().create_default_creature_without_weapon("goblin")
        self.assertEqual(type(creature.weapon()), Unarmed)


class TestWeaponCreationMethods(unittest.TestCase):
    def test_weapon_creation(self):
        weapon = WeaponFactory().create_weapon("sword")
        self.assertEqual(type(weapon), Sword)

    def test_custom_weapon_stat(self):
        weapon = WeaponFactory().create_weapon("sword", {"base_value": 7})
        self.assertEqual(weapon.base_value(), 7)
