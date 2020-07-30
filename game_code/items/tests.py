"""
All tests for the items library.
"""
import unittest

from game_code.factory import Factory
from game_code.items import ConsumableItem
from game_code.items.healing_items import LesserHealingPotion, IntermediateHealingPotion, \
    GreaterHealingPotion


class TestItem(unittest.TestCase):
    def test_is_usable_valid(self):
        consumable = ConsumableItem(remaining_uses=10, name="test", value=0, weight=0)
        self.assertEqual(True, consumable.is_usable())

    def test_is_usable_borderline_valid(self):
        consumable = ConsumableItem(remaining_uses=1, name="test", value=0, weight=0)
        self.assertEqual(True, consumable.is_usable())

    def test_is_usable_borderline_invalid(self):
        consumable = ConsumableItem(remaining_uses=0, name="test", value=0, weight=0)
        self.assertEqual(False, consumable.is_usable())

    def test_is_usable_invalid(self):
        consumable = ConsumableItem(remaining_uses=-1, name="test", value=0, weight=0)
        self.assertEqual(False, consumable.is_usable())


class TestHealthPotion(unittest.TestCase):
    def test_use_remaining_uses_reduction(self):
        healing_potion = LesserHealingPotion()
        executor = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        target = Factory().create_creature(creature_class="goblin", first_name="Charles", second_name="Brown")
        healing_potion.use(executor=executor, target=target)
        self.assertEqual(0, healing_potion.remaining_uses())

    def test_use_lesser_healing_potion_healing_quantity(self):
        healing_potion = LesserHealingPotion()
        executor = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        target = Factory().create_creature(creature_class="goblin", first_name="Charles", second_name="Brown")
        action = healing_potion.use(executor=executor, target=target)
        self.assertEqual(10, action.healing_quantity())

    def test_use_intermediate_healing_potion_healing_quantity(self):
        healing_potion = IntermediateHealingPotion()
        executor = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        target = Factory().create_creature(creature_class="goblin", first_name="Charles", second_name="Brown")
        action = healing_potion.use(executor=executor, target=target)
        self.assertEqual(20, action.healing_quantity())

    def test_use_greater_healing_potion_healing_quantity(self):
        healing_potion = GreaterHealingPotion()
        executor = Factory().create_creature(creature_class="goblin", first_name="John", second_name="Doe")
        target = Factory().create_creature(creature_class="goblin", first_name="Charles", second_name="Brown")
        action = healing_potion.use(executor=executor, target=target)
        self.assertEqual(30, action.healing_quantity())
