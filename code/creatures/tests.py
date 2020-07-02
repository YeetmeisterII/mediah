import unittest

from code.creatures import Creature


class TestCreatureMethods(unittest.TestCase):
    def test_is_alive(self):
        creature1 = Creature(constitution=1)
        creature2 = Creature(constitution=0)
        self.assertEqual(creature1.stats().health(), 1)
        self.assertEqual(creature2.stats().health(), 0)
        self.assertTrue(creature1.is_alive())
        self.assertFalse(creature2.is_alive())
