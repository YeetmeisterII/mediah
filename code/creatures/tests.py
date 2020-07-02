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

    def test_health_increase(self):
        creature = Creature(constitution=10)
        creature._health = 5
        self.assertEqual(creature.stats().increase_health(2), 2)
        self.assertEqual(creature.stats().health(), 7)

    def test_health_reduce(self):
        creature = Creature(constitution=10)
        self.assertEqual(creature.stats().reduce_health(12), 12)
        self.assertEqual(creature.stats().health(), -2)

    def test_health_max_cap(self):
        creature = Creature(constitution=10)
        creature._health = 5
        self.assertEqual(creature.stats().increase_health(6), 5)
        self.assertEqual(creature.stats().health(), 10)

    def test_constitution_increase(self):
        creature = Creature(constitution=10)
        self.assertEqual(creature.stats().increase_constitution(10), 10)
        self.assertEqual(creature.stats().constitution(), 20)

    def test_constitution_reduce(self):
        creature = Creature(constitution=10)
        self.assertEqual(creature.stats().health(), 10)
        self.assertEqual(creature.stats().reduce_constitution(4), 4)
        self.assertEqual(creature.stats().constitution(), 6)
        self.assertEqual(creature.stats().health(), 6)

    def test_constitution_min_cap(self):
        creature = Creature(constitution=10)
        self.assertEqual(creature.stats().reduce_constitution(11), 10)
        self.assertEqual(creature.stats().constitution(), 0)
        self.assertEqual(creature.stats().health(), 0)

    def test_mana_increase(self):
        creature = Creature(magic_base=10)
        creature._mana = 5
        self.assertEqual(creature.stats().increase_mana(2), 2)
        self.assertEqual(creature.stats().mana(), 7)

    def test_mana_reduce(self):
        creature = Creature(magic_base=10)
        self.assertEqual(creature.stats().reduce_mana(2), 2)
        self.assertEqual(creature.stats().mana(), 8)

    def test_mana_max_cap(self):
        creature = Creature(magic_base=10)
        creature._mana = 5
        self.assertEqual(creature.stats().increase_mana(6), 5)
        self.assertEqual(creature.stats().mana(), 10)

    def test_mana_min_cap(self):
        creature = Creature(magic_base=10)
        self.assertEqual(creature.stats().reduce_mana(11), 10)
        self.assertEqual(creature.stats().mana(), 0)

    def test_magic_base_increase(self):
        creature = Creature(magic_base=10)
        self.assertEqual(creature.stats().increase_magic_base(6), 6)
        self.assertEqual(creature.stats().magic_base(), 16)

    def test_magic_base_reduce(self):
        creature = Creature(magic_base=10)
        self.assertEqual(creature.stats().mana(), 10)
        self.assertEqual(creature.stats().reduce_magic_base(4), 4)
        self.assertEqual(creature.stats().magic_base(), 6)
        self.assertEqual(creature.stats().mana(), 6)

    def test_magic_base_min_cap(self):
        creature = Creature(magic_base=10)
        self.assertEqual(creature.stats().mana(), 10)
        self.assertEqual(creature.stats().reduce_magic_base(11), 10)
        self.assertEqual(creature.stats().magic_base(), 0)
        self.assertEqual(creature.stats().mana(), 0)

    def test_charisma_increase(self):
        creature = Creature(social=10)
        creature._charisma = 5
        self.assertEqual(creature.stats().increase_charisma(2), 2)
        self.assertEqual(creature.stats().charisma(), 7)

    def test_charisma_reduce(self):
        creature = Creature(social=10)
        self.assertEqual(creature.stats().reduce_charisma(2), 2)
        self.assertEqual(creature.stats().charisma(), 8)

    def test_charisma_max_cap(self):
        creature = Creature(social=10)
        creature._charisma = 5
        self.assertEqual(creature.stats().increase_charisma(6), 5)
        self.assertEqual(creature.stats().charisma(), 10)

    def test_charisma_min_cap(self):
        creature = Creature(social=10)
        self.assertEqual(creature.stats().reduce_charisma(11), 10)
        self.assertEqual(creature.stats().charisma(), 0)

    def test_social_increase(self):
        creature = Creature(social=10)
        self.assertEqual(creature.stats().increase_social(6), 6)
        self.assertEqual(creature.stats().social(), 16)

    def test_social_reduce(self):
        creature = Creature(social=10)
        self.assertEqual(creature.stats().charisma(), 10)
        self.assertEqual(creature.reduce_social(4), 4)
        self.assertEqual(creature.stats().social(), 6)
        self.assertEqual(creature.stats().charisma(), 6)

    def test_social_min_cap(self):
        creature = Creature(social=10)
        self.assertEqual(creature.stats().charisma(), 10)
        self.assertEqual(creature.reduce_social(11), 10)
        self.assertEqual(creature.stats().social(), 0)
        self.assertEqual(creature.stats().charisma(), 0)

    def test_physicality_increase(self):
        creature = Creature(physicality=10)
        creature._physicality = 5
        self.assertEqual(creature.stats().increase_physicality(2), 2)
        self.assertEqual(creature.stats().physicality(), 7)

    def test_physicality_reduce(self):
        creature = Creature(physicality=10)
        self.assertEqual(creature.stats().reduce_physicality(2), 2)
        self.assertEqual(creature.stats().physicality(), 8)

    def test_physicality_max_cap(self):
        creature = Creature(physicality=10)
        creature._physicality = 5
        self.assertEqual(creature.stats().increase_physicality(6), 5)
        self.assertEqual(creature.stats().physicality(), 10)

    def test_physicality_min_cap(self):
        creature = Creature(physicality=10)
        self.assertEqual(creature.stats().reduce_physicality(11), 10)
        self.assertEqual(creature.stats().physicality(), 0)

    def test_physicality_base_increase(self):
        creature = Creature(physicality=10)
        self.assertEqual(creature.stats().increase_physicality_base(6), 6)
        self.assertEqual(creature.stats().physicality_base(), 16)

    def test_physicality_base_reduce(self):
        creature = Creature(physicality=10)
        self.assertEqual(creature.stats().physicality(), 10)
        self.assertEqual(creature.stats().reduce_physicality_base(4), 4)
        self.assertEqual(creature.stats().physicality_base(), 6)
        self.assertEqual(creature.stats().physicality(), 6)

    def test_physicality_base_min_cap(self):
        creature = Creature(physicality=10)
        self.assertEqual(creature.stats().physicality(), 10)
        self.assertEqual(creature.stats().reduce_physicality_base(11), 10)
        self.assertEqual(creature.stats().physicality_base(), 0)
        self.assertEqual(creature.stats().physicality(), 0)

    def test_dexterity_increase(self):
        creature = Creature(dexterity=10)
        creature._dexterity = 5
        self.assertEqual(creature.stats().increase_dexterity(2), 2)
        self.assertEqual(creature.stats().dexterity(), 7)

    def test_dexterity_reduce(self):
        creature = Creature(dexterity=10)
        self.assertEqual(creature.stats().reduce_dexterity(2), 2)
        self.assertEqual(creature.stats().dexterity(), 8)

    def test_dexterity_max_cap(self):
        creature = Creature(dexterity=10)
        creature._dexterity = 5
        self.assertEqual(creature.stats().increase_dexterity(6), 5)
        self.assertEqual(creature.stats().dexterity(), 10)

    def test_dexterity_min_cap(self):
        creature = Creature(dexterity=10)
        self.assertEqual(creature.stats().reduce_dexterity(11), 10)
        self.assertEqual(creature.stats().dexterity(), 0)

    def test_dexterity_base_increase(self):
        creature = Creature(dexterity=10)
        self.assertEqual(creature.stats().increase_dexterity_base(6), 6)
        self.assertEqual(creature.stats().dexterity_base(), 16)

    def test_dexterity_base_reduce(self):
        creature = Creature(dexterity=10)
        self.assertEqual(creature.stats().dexterity(), 10)
        self.assertEqual(creature.stats().reduce_dexterity_base(4), 4)
        self.assertEqual(creature.stats().dexterity_base(), 6)
        self.assertEqual(creature.stats().dexterity(), 6)

    def test_dexterity_base_min_cap(self):
        creature = Creature(dexterity=10)
        self.assertEqual(creature.stats().dexterity(), 10)
        self.assertEqual(creature.stats().reduce_dexterity_base(11), 10)
        self.assertEqual(creature.stats().dexterity_base(), 0)
        self.assertEqual(creature.stats().dexterity(), 0)

    def test_experience(self):
        creature = Creature(experience=10)
        self.assertEqual(creature.stats().experience(), 10)
        self.assertEqual(creature.stats().increase_experience(5), 5)
        self.assertEqual(creature.stats().experience(), 15)
