import unittest

from code.actions import NullAction, HealingAction
from code.creatures import Creature
from code.items import Consumable
from code.items.healing_items import HealingPotion


class TestItemMethods(unittest.TestCase):
    pass


class TestConsumableMethods(unittest.TestCase):
    def test_is_usable(self):
        consumable = Consumable(remaining_uses=1)
        self.assertEqual(consumable.is_usable(), True)

    def test_not_usable(self):
        consumable = Consumable(remaining_uses=0)
        self.assertEqual(consumable.is_usable(), False)

    def test_use_action_type(self):
        consumable = Consumable()
        action = consumable.use(Creature(), Creature())
        self.assertEqual(type(action), NullAction)


class TestHealthPotionMethods(unittest.TestCase):
    def test_is_usable(self):
        healing_potion = HealingPotion(remaining_uses=1, healing_quantity=0)
        self.assertEqual(healing_potion.is_usable(), True)

    def test_not_usable(self):
        healing_potion = HealingPotion(remaining_uses=0, healing_quantity=0)
        self.assertEqual(healing_potion.is_usable(), False)

    def test_use_action_type(self):
        healing_potion = HealingPotion(healing_quantity=0)
        action = healing_potion.use(Creature(), Creature())
        self.assertEqual(type(action), HealingAction)

    def test_use_action_healing_quantity(self):
        healing_potion = HealingPotion(healing_quantity=7)
        action = healing_potion.use(Creature(), Creature())
        self.assertEqual(action.healing_quantity(), 7)

    def test_use_action_executor(self):
        healing_potion = HealingPotion(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_potion.use(executor=creature1, target=creature2)
        self.assertEqual(action.executor(), creature1)

    def test_use_action_target(self):
        healing_potion = HealingPotion(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_potion.use(executor=creature1, target=creature2)
        self.assertEqual(action.target(), creature2)
