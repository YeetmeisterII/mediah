import unittest

from code.creatures import Goblin
from code.factory import Factory
from code.weapons import Sword


class TestCreatureCreationMethods(unittest.TestCase):
    def test_create_creature(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(type(creature), Goblin)

    def test_create_custom_creature(self):
        creature = Factory().create_creature("goblin", {"physicality": 7})
        self.assertEqual(creature.physicality_base(), 7)

    def test_default_goblin_creation(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(creature.constitution(), 10)
        self.assertEqual(creature.physicality_base(), 5)
        self.assertEqual(creature.dexterity_base(), 10)
        self.assertEqual(creature.social(), 0)
        self.assertEqual(creature.gold_worth(), 5)
        self.assertEqual(creature.experience_worth(), 10)

    def test_default_orc_creation(self):
        creature = Factory().create_creature("orc")
        self.assertEqual(creature.constitution(), 15)
        self.assertEqual(creature.physicality_base(), 13)
        self.assertEqual(creature.dexterity_base(), 13)
        self.assertEqual(creature.social(), 0)
        self.assertEqual(creature.gold_worth(), 10)
        self.assertEqual(creature.experience_worth(), 15)

    def test_default_earth_elemental_creation(self):
        creature = Factory().create_creature("earth_elemental")
        self.assertEqual(creature.constitution(), 5)
        self.assertEqual(creature.physicality_base(), 16)
        self.assertEqual(creature.dexterity_base(), 16)
        self.assertEqual(creature.social(), 0)
        self.assertEqual(creature.gold_worth(), 0)
        self.assertEqual(creature.experience_worth(), 30)

    def test_default_djinn_creation(self):
        creature = Factory().create_creature("djinn")
        self.assertEqual(creature.constitution(), 10)
        self.assertEqual(creature.physicality_base(), 5)
        self.assertEqual(creature.dexterity_base(), 16)
        self.assertEqual(creature.social(), 17)
        self.assertEqual(creature.gold_worth(), 30)
        self.assertEqual(creature.experience_worth(), 15)

    def test_default_dragon_creation(self):
        creature = Factory().create_creature("dragon")
        self.assertEqual(creature.constitution(), 30)
        self.assertEqual(creature.physicality_base(), 18)
        self.assertEqual(creature.dexterity_base(), 18)
        self.assertEqual(creature.social(), 0)
        self.assertEqual(creature.gold_worth(), 100000000)
        self.assertEqual(creature.experience_worth(), 500)

    def test_default_human_creation(self):
        creature = Factory().create_creature("human")
        self.assertEqual(creature.constitution(), 10)
        self.assertEqual(creature.physicality_base(), 10)
        self.assertEqual(creature.dexterity_base(), 10)
        self.assertEqual(creature.social(), 10)
        self.assertEqual(creature.gold_worth(), 0)
        self.assertEqual(creature.experience_worth(), 0)


class TestWeaponCreationMethods(unittest.TestCase):
    def test_weapon_creation(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual(type(weapon), Sword)

    def test_custom_weapon_stat(self):
        weapon = Factory().create_weapon("sword", {"base_value": 7})
        self.assertEqual(weapon.base_value(), 7)

    def test_default_unarmed_creation(self):
        weapon = Factory().create_weapon("unarmed")
        self.assertEqual(weapon.name(), "Fist")
        self.assertEqual(weapon.base_value(), 0)
        self.assertEqual(weapon.dice_quantity(), 1)
        self.assertEqual(weapon.dice_max(), 1)

    def test_default_sword_creation(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual(weapon.name(), "Sword")
        self.assertEqual(weapon.base_value(), 0)
        self.assertEqual(weapon.dice_quantity(), 1)
        self.assertEqual(weapon.dice_max(), 6)

    def test_default_dagger_creation(self):
        weapon = Factory().create_weapon("dagger")
        self.assertEqual(weapon.name(), "Dagger")
        self.assertEqual(weapon.base_value(), 0)
        self.assertEqual(weapon.dice_quantity(), 1)
        self.assertEqual(weapon.dice_max(), 3)

    def test_default_rock_fist_creation(self):
        weapon = Factory().create_weapon("rock_fist")
        self.assertEqual(weapon.name(), "Rock Fist")
        self.assertEqual(weapon.base_value(), 3)
        self.assertEqual(weapon.dice_quantity(), 1)
        self.assertEqual(weapon.dice_max(), 8)


class TestSkillCreationMethods(unittest.TestCase):
    # TODO: Refactor create_weapon to create_skill when the necessary modifications in the code are completed.
    def test_default_fire_breath_creation(self):
        skill = Factory().create_weapon("fire_breath")
        self.assertEqual(skill.base_value(), 0)
        self.assertEqual(skill.dice_quantity(), 2)
        self.assertEqual(skill.dice_max(), 12)

    def test_default_harsh_language_creation(self):
        skill = Factory().create_weapon("harsh_language")
        self.assertEqual(skill.name(), "Harsh Language")
        self.assertEqual(skill.base_value(), 0)
        self.assertEqual(skill.dice_quantity(), 1)
        self.assertEqual(skill.dice_max(), 4)
