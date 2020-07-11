import unittest

from game_code.actions import AttackAction, HealingAction
from game_code.creatures import Creature


class TestAttackActionMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.executor = Creature()
        cls.target = Creature()
        cls.attack = AttackAction(executor=cls.executor, target=cls.target, damage=5, hit_index=6)

    def test_executor(self):
        self.assertEqual(self.executor, self.attack.executor())

    def test_target(self):
        self.assertEqual(self.target, self.attack.target())

    def test_damage(self):
        self.assertEqual(5, self.attack.damage())

    def test_hit_index(self):
        self.assertEqual(6, self.attack.hit_index())


class TestHealingActionMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.executor = Creature()
        cls.target = Creature()
        cls.heal = HealingAction(executor=cls.executor, target=cls.target, healing_quantity=11)

    def test_executor(self):
        self.assertEqual(self.executor, self.heal.executor())

    def test_target(self):
        self.assertEqual(self.target, self.heal.target())

    def test_health_quantity(self):
        self.assertEqual(11, self.heal.healing_quantity())
