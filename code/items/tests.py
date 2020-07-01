import unittest

from mediah.actions import NullAction, HealingAction
from mediah.creatures import Creature
from mediah.items import Consumable
from mediah.items.healing_items import HealingPotion


class TestItemMethods(unittest.TestCase):
    pass


class TestConsumableMethods(unittest.TestCase):
    def test_is_usable(self):
        consumable = Consumable(remaining_uses=1)
        self.assertEqual(consumable.is_usable(), True)

    def test_not_usable(self):
        consumable = Consumable(remaining_uses=0)
        self.assertEqual(consumable.is_usable(), False)

    def test_use_action(self):
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

    def test_use_action(self):
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
