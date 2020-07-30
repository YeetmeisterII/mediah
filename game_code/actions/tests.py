"""
All tests for the actions library.
"""

import unittest
from copy import deepcopy

from game_code.actions import AttackAction
from game_code.creatures import Goblin
from game_code.stats import Stats
from game_code.status import Status, Block
from game_code.weapons import Sword


class TestAttackAction(unittest.TestCase):
    def setUp(self) -> None:
        """
        Creates two goblin instances for each test. They both have all stats at 0 and a sword.
        """
        sword = Sword(base_value=0, dice_quantity=0, dice_max=0, weight=0, value=0)
        kwargs = {"second_name": "Goblin", "stats": Stats(), "status": Status(), "weapon": sword}
        self.attacker = Goblin(first_name="Attacker", **deepcopy(kwargs))
        self.defender = Goblin(first_name="Defender", **deepcopy(kwargs))

    def test_critical_hit(self):
        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=20, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("Critical Hit!" in response_result[1])

    def test_critical_hit_with_defender_blocking(self):
        self.defender.status().add_effect(Block(turns=1))

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=20, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("Critical Hit!" in response_result[1])

    def test_hit(self):
        self.defender.stats()._dexterity = 10

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=11, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("attack lands" in response_result[1])

    def test_hit_with_defender_blocking(self):
        self.defender.status().add_effect(Block(turns=1))
        self.defender.stats()._dexterity = 5

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=11, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("attack lands" in response_result[1])

    def test_miss(self):
        self.defender.stats()._dexterity = 10

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=10, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("attack misses" in response_result[1])

    def test_miss_with_defender_blocking(self):
        self.defender.status().add_effect(Block(turns=1))
        self.defender.stats()._dexterity = 5

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=10, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("attack misses" in response_result[1])

    def test_critical_miss(self):
        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=1, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("Critical miss" in response_result[1])

    def test_critical_miss_with_defender_blocking(self):
        self.defender.status().add_effect(Block(turns=1))

        attack = AttackAction(
            executor=self.attacker, target=self.defender, tool_used=self.attacker.weapon(), hit_index=1, damage=0
        )
        response = attack()
        response_result = response()
        self.assertTrue("Critical miss" in response_result[1])
