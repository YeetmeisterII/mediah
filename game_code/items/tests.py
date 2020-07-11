import unittest

from game_code.actions import NullAction, HealingAction
from game_code.creatures import Creature
from game_code.items import Consumable
from game_code.items.healing_items import HealingPotion


class TestItemMethods(unittest.TestCase):
    pass


class TestConsumableMethods(unittest.TestCase):
    def test_is_usable(self):
        consumable = Consumable(remaining_uses=1)
        self.assertEqual(True, consumable.is_usable())

    def test_not_usable(self):
        consumable = Consumable(remaining_uses=0)
        self.assertEqual(False, consumable.is_usable())

    def test_use_action_type(self):
        consumable = Consumable()
        action = consumable.use(Creature(), Creature())
        self.assertEqual(NullAction, type(action))


class TestHealthPotionMethods(unittest.TestCase):
    def test_is_usable(self):
        healing_potion = HealingPotion(remaining_uses=1, healing_quantity=0)
        self.assertEqual(True, healing_potion.is_usable())

    def test_not_usable(self):
        healing_potion = HealingPotion(remaining_uses=0, healing_quantity=0)
        self.assertEqual(False, healing_potion.is_usable())

    def test_use_action_type(self):
        healing_potion = HealingPotion(healing_quantity=0)
        action = healing_potion.use(Creature(), Creature())
        self.assertEqual(HealingAction, type(action))

    def test_use_action_healing_quantity(self):
        healing_potion = HealingPotion(healing_quantity=7)
        action = healing_potion.use(Creature(), Creature())
        self.assertEqual(7, action.healing_quantity())

    def test_use_action_executor(self):
        healing_potion = HealingPotion(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_potion.use(executor=creature1, target=creature2)
        self.assertEqual(creature1, action.executor())

    def test_use_action_target(self):
        healing_potion = HealingPotion(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_potion.use(executor=creature1, target=creature2)
        self.assertEqual(creature2, action.target())
