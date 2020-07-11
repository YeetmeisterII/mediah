import unittest

from game_code.creatures import Goblin
from game_code.factory import Factory
from game_code.weapons import Sword


class TestCreatureCreationMethods(unittest.TestCase):
    def test_create_creature(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(type(creature), Goblin)

    def test_create_custom_creature(self):
        creature = Factory().create_creature("goblin", {"physicality": 7})
        self.assertEqual(7, creature.stats().physicality_base())

    def test_default_goblin_creation(self):
        creature = Factory().create_creature("goblin")
        self.assertEqual(10, creature.stats().constitution())
        self.assertEqual(5, creature.stats().physicality_base())
        self.assertEqual(10, creature.stats().dexterity_base())
        self.assertEqual(0, creature.stats().social())
        self.assertEqual(5, creature.gold_worth())
        self.assertEqual(10, creature.experience_worth())

    def test_default_orc_creation(self):
        creature = Factory().create_creature("orc")
        self.assertEqual(15, creature.stats().constitution())
        self.assertEqual(13, creature.stats().physicality_base())
        self.assertEqual(13, creature.stats().dexterity_base())
        self.assertEqual(0, creature.stats().social())
        self.assertEqual(10, creature.gold_worth())
        self.assertEqual(15, creature.experience_worth())

    def test_default_earth_elemental_creation(self):
        creature = Factory().create_creature("earth_elemental")
        self.assertEqual(5, creature.stats().constitution())
        self.assertEqual(16, creature.stats().physicality_base())
        self.assertEqual(16, creature.stats().dexterity_base())
        self.assertEqual(0, creature.stats().social())
        self.assertEqual(0, creature.gold_worth())
        self.assertEqual(30, creature.experience_worth())

    def test_default_djinn_creation(self):
        creature = Factory().create_creature("djinn")
        self.assertEqual(10, creature.stats().constitution())
        self.assertEqual(5, creature.stats().physicality_base())
        self.assertEqual(16, creature.stats().dexterity_base())
        self.assertEqual(17, creature.stats().social())
        self.assertEqual(30, creature.gold_worth())
        self.assertEqual(15, creature.experience_worth())

    def test_default_dragon_creation(self):
        creature = Factory().create_creature("dragon")
        self.assertEqual(30, creature.stats().constitution())
        self.assertEqual(18, creature.stats().physicality_base())
        self.assertEqual(18, creature.stats().dexterity_base())
        self.assertEqual(0, creature.stats().social())
        self.assertEqual(100000000, creature.gold_worth())
        self.assertEqual(500, creature.experience_worth())

    def test_default_human_creation(self):
        creature = Factory().create_creature("human")
        self.assertEqual(10, creature.stats().constitution())
        self.assertEqual(10, creature.stats().physicality_base())
        self.assertEqual(10, creature.stats().dexterity_base())
        self.assertEqual(10, creature.stats().social())
        self.assertEqual(0, creature.gold_worth())
        self.assertEqual(0, creature.experience_worth())


class TestWeaponCreationMethods(unittest.TestCase):
    def test_weapon_creation(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual(Sword, type(weapon))

    def test_custom_weapon_stat(self):
        weapon = Factory().create_weapon("sword", {"base_value": 7})
        self.assertEqual(7, weapon.base_value())

    def test_default_unarmed_creation(self):
        weapon = Factory().create_weapon("unarmed")
        self.assertEqual("Fist", weapon.name())
        self.assertEqual(0, weapon.base_value())
        self.assertEqual(1, weapon.dice_quantity())
        self.assertEqual(1, weapon.dice_max())

    def test_default_sword_creation(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual("Sword", weapon.name())
        self.assertEqual(0, weapon.base_value())
        self.assertEqual(1, weapon.dice_quantity())
        self.assertEqual(6, weapon.dice_max())

    def test_default_dagger_creation(self):
        weapon = Factory().create_weapon("dagger")
        self.assertEqual("Dagger", weapon.name())
        self.assertEqual(0, weapon.base_value())
        self.assertEqual(1, weapon.dice_quantity())
        self.assertEqual(3, weapon.dice_max())

    def test_default_rock_fist_creation(self):
        weapon = Factory().create_weapon("rock_fist")
        self.assertEqual("Rock Fist", weapon.name())
        self.assertEqual(3, weapon.base_value())
        self.assertEqual(1, weapon.dice_quantity())
        self.assertEqual(8, weapon.dice_max())


class TestSkillCreationMethods(unittest.TestCase):
    # TODO: Refactor create_weapon to create_skill when the necessary modifications in the game_code are completed.
    def test_default_fire_breath_creation(self):
        skill = Factory().create_weapon("fire_breath")
        self.assertEqual(0, skill.base_value())
        self.assertEqual(2, skill.dice_quantity())
        self.assertEqual(12, skill.dice_max())

    def test_default_harsh_language_creation(self):
        skill = Factory().create_weapon("harsh_language")
        self.assertEqual("Harsh Language", skill.name())
        self.assertEqual(0, skill.base_value())
        self.assertEqual(1, skill.dice_quantity())
        self.assertEqual(4, skill.dice_max())
