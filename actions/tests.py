import unittest

from mediah.actions import AttackAction, HealAction
from mediah.creatures import Creature


class TestAttackMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.executor = Creature()
        cls.target = Creature()
        cls.attack = AttackAction(executor=cls.executor, target=cls.target, damage=5, hit_index=6)

    def test_executor(self):
        self.assertEqual(self.attack.executor(), self.executor)

    def test_target(self):
        self.assertEqual(self.attack.target(), self.target)

    def test_damage(self):
        self.assertEqual(self.attack.damage(), 5)

    def test_hit_index(self):
        self.assertEqual(self.attack.hit_index(), 6)


class TestHealMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.executor = Creature()
        cls.target = Creature()
        cls.heal = HealAction(executor=cls.executor, target=cls.target, heal_quantity=11)

    def test_executor(self):
        self.assertEqual(self.heal.executor(), self.executor)

    def test_target(self):
        self.assertEqual(self.heal.target(), self.target)

    def test_health_quantity(self):
        self.assertEqual(self.heal.heal_quantity(), 11)
