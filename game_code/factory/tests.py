"""
All tests for the factory library.
"""
import unittest

from game_code.creatures import Goblin
from game_code.factory import Factory
from game_code.weapons import Sword


class TestCreatureCreation(unittest.TestCase):
    def test_create_creature(self):
        creature = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        self.assertEqual(Goblin, type(creature))

    def test_create_creature_with_stat_values(self):
        stat_values = {
            "constitution": 1, "physicality": 2, "dexterity": 3, "social": 4, "experience": 5, "magic_base": 6,
            "gold_worth": 7, "experience_worth": 8, "magic_enabled": True
        }
        creature = Factory().create_creature(
            creature_class="goblin", first_name="John", second_name="Doe", stat_values=stat_values
        )
        stats = creature.stats()
        expected_values = (1, 2, 3, 4, 5, 6, 7, 8, True)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_goblin_creation(self):
        creature = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (10, 5, 10, 0, 0, 0, 5, 10, False)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_orc_creation(self):
        creature = Factory().create_creature(creature_class="orc", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (15, 13, 13, 0, 0, 0, 10, 15, False)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_earth_elemental_creation(self):
        creature = Factory().create_creature(creature_class="earth_elemental", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (5, 16, 16, 0, 0, 0, 0, 30, True)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_djinn_creation(self):
        creature = Factory().create_creature(creature_class="djinn", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (10, 5, 16, 17, 0, 0, 30, 15, True)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_dragon_creation(self):
        creature = Factory().create_creature(creature_class="dragon", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (30, 18, 18, 0, 0, 0, 100000000, 500, False)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_default_human_creation(self):
        creature = Factory().create_creature(creature_class="human", first_name="John", second_name="Doe")
        stats = creature.stats()
        expected_values = (10, 10, 10, 10, 0, 0, 0, 0, False)
        actual_values = (
            stats.constitution(), stats.physicality_base(), stats.dexterity_base(), stats.social(), stats.experience(),
            stats.magic_base(), stats.gold_worth(), stats.experience_worth(), stats.magic_enabled()
        )
        self.assertTupleEqual(expected_values, actual_values)


class TestWeaponCreation(unittest.TestCase):
    def test_create_weapon(self):
        weapon = Factory().create_weapon("sword")
        self.assertEqual(Sword, type(weapon))

    def test_create_weapon_with_stat_values(self):
        stat_values = {"base_value": 1, "dice_quantity": 2, "dice_max": 3, "value": 4, "weight": 5}
        weapon = Factory().create_weapon(weapon_class="sword", stat_values=stat_values)
        expected_values = (1, 2, 3, 4, 5, "Sword")
        actual_values = (
            weapon.base_value(), weapon.dice_quantity(), weapon.dice_max(), weapon.value(), weapon.weight(),
            weapon.name()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_create_weapon_without_name(self):
        weapon = Factory().create_weapon(weapon_class="sword")
        self.assertEqual("Sword", weapon.name())

    def test_create_weapon_with_name(self):
        weapon = Factory().create_weapon(weapon_class="sword", name="John Doe")
        self.assertEqual("John Doe (Sword)", weapon.name())

    def test_create_weapon_default_unarmed(self):
        weapon = Factory().create_weapon("unarmed")
        expected_values = (0, 1, 1, 0, 0, "Fist")
        actual_values = (
            weapon.base_value(), weapon.dice_quantity(), weapon.dice_max(), weapon.value(), weapon.weight(),
            weapon.name()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_create_weapon_default_sword(self):
        weapon = Factory().create_weapon("sword")
        expected_values = (0, 1, 6, 5, 4, "Sword")
        actual_values = (
            weapon.base_value(), weapon.dice_quantity(), weapon.dice_max(), weapon.value(), weapon.weight(),
            weapon.name()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_create_weapon_default_dagger(self):
        weapon = Factory().create_weapon("dagger")
        expected_values = (0, 1, 3, 2, 1, "Dagger")
        actual_values = (
            weapon.base_value(), weapon.dice_quantity(), weapon.dice_max(), weapon.value(), weapon.weight(),
            weapon.name()
        )
        self.assertTupleEqual(expected_values, actual_values)

    def test_create_weapon_default_rock_fist(self):
        weapon = Factory().create_weapon("rock_fist")
        expected_values = (3, 1, 8, 0, 0, "Rock Fist")
        actual_values = (
            weapon.base_value(), weapon.dice_quantity(), weapon.dice_max(), weapon.value(), weapon.weight(),
            weapon.name()
        )
        self.assertTupleEqual(expected_values, actual_values)


class TestSkillCreation(unittest.TestCase):
    # TODO: Refactor create_weapon to create_skill when the necessary modifications in the game_code are completed.
    def test_create_weapon_default_fire_breath(self):
        skill = Factory().create_weapon("fire_breath")
        expected_values = (0, 2, 12, "Fire Breath")
        actual_values = (skill.base_value(), skill.dice_quantity(), skill.dice_max(), skill.name())
        self.assertTupleEqual(expected_values, actual_values)

    def test_create_weapon_default_harsh_language(self):
        skill = Factory().create_weapon("harsh_language")
        expected_values = (0, 1, 4, "Harsh Language")
        actual_values = (skill.base_value(), skill.dice_quantity(), skill.dice_max(), skill.name())
        self.assertTupleEqual(expected_values, actual_values)
