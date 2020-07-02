import unittest

from code.creatures import Creature
from code.response import Response, AttackResponse


class TestResponseMethods(unittest.TestCase):
    def test_result(self):
        executor = Creature()
        target = Creature()
        response = Response(executor=executor, target=target, medium="reason", outcome="outcome", cause="cause")
        self.assertEqual(response.result(), None)


class TestAttackResponseMethods(unittest.TestCase):
    def test_result_damage(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=10, cause="hit")
        expected_message = ["First_name1 attacks First_name2.", "First_name1 lands attack on First_name2.",
                            "First_name2 takes 10 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_no_second_name(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="hit")
        expected_message = ["First_name1 attacks First_name2.", "First_name1 lands attack on First_name2.",
                            "First_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_with_second_name(self):
        executor = Creature(first_name="First_name1", second_name="Second_name1")
        target = Creature(first_name="First_name2", second_name="Second_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="hit")
        expected_message = ["First_name1 Second_name1 attacks First_name2 Second_name2.",
                            "First_name1 Second_name1 lands attack on First_name2 Second_name2.",
                            "First_name2 Second_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_critical_hit(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="critical_hit")
        expected_message = ["First_name1 attacks First_name2.", "Critical Hit! Attack bypasses defence.",
                            "First_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_hit(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="hit")
        expected_message = ["First_name1 attacks First_name2.", "First_name1 lands attack on First_name2.",
                            "First_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_miss(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="miss")
        expected_message = ["First_name1 attacks First_name2.", "First_name1 misses attack on First_name2.",
                            "First_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)

    def test_result_critical_miss(self):
        executor = Creature(first_name="First_name1")
        target = Creature(first_name="First_name2")
        response = AttackResponse(executor=executor, target=target, outcome=0, cause="critical_miss")
        expected_message = ["First_name1 attacks First_name2.",
                            "Critical miss. Attack on First_name2 fails expeditiously.", "First_name2 takes 0 damage."]
        self.assertEqual(response.result(), expected_message)
