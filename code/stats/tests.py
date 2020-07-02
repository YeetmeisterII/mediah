import unittest

from code.stats import Stats


class TestStatsMethods(unittest.TestCase):
    def test_health_increase(self):
        stats = Stats(constitution=10)
        stats._health = 5
        self.assertEqual(stats.increase_health(2), 2)
        self.assertEqual(stats.health(), 7)

    def test_health_reduce(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.reduce_health(12), 12)
        self.assertEqual(stats.health(), -2)

    def test_health_max_cap(self):
        stats = Stats(constitution=10)
        stats._health = 5
        self.assertEqual(stats.increase_health(6), 5)
        self.assertEqual(stats.health(), 10)

    def test_constitution_increase(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.increase_constitution(10), 10)
        self.assertEqual(stats.constitution(), 20)

    def test_constitution_reduce(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.health(), 10)
        self.assertEqual(stats.reduce_constitution(4), 4)
        self.assertEqual(stats.constitution(), 6)
        self.assertEqual(stats.health(), 6)

    def test_constitution_min_cap(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.reduce_constitution(11), 10)
        self.assertEqual(stats.constitution(), 0)
        self.assertEqual(stats.health(), 0)

    def test_mana_increase(self):
        stats = Stats(magic_base=10)
        stats._mana = 5
        self.assertEqual(stats.increase_mana(2), 2)
        self.assertEqual(stats.mana(), 7)

    def test_mana_reduce(self):
        stats = Stats(magic_base=10)
        self.assertEqual(stats.reduce_mana(2), 2)
        self.assertEqual(stats.mana(), 8)

    def test_mana_max_cap(self):
        stats = Stats(magic_base=10)
        stats._mana = 5
        self.assertEqual(stats.increase_mana(6), 5)
        self.assertEqual(stats.mana(), 10)

    def test_mana_min_cap(self):
        stats = Stats(magic_base=10)
        self.assertEqual(stats.reduce_mana(11), 10)
        self.assertEqual(stats.mana(), 0)

    def test_magic_base_increase(self):
        stats = Stats(magic_base=10)
        self.assertEqual(stats.increase_magic_base(6), 6)
        self.assertEqual(stats.magic_base(), 16)

    def test_magic_base_reduce(self):
        stats = Stats(magic_base=10)
        self.assertEqual(stats.mana(), 10)
        self.assertEqual(stats.reduce_magic_base(4), 4)
        self.assertEqual(stats.magic_base(), 6)
        self.assertEqual(stats.mana(), 6)

    def test_magic_base_min_cap(self):
        stats = Stats(magic_base=10)
        self.assertEqual(stats.mana(), 10)
        self.assertEqual(stats.reduce_magic_base(11), 10)
        self.assertEqual(stats.magic_base(), 0)
        self.assertEqual(stats.mana(), 0)

    def test_charisma_increase(self):
        stats = Stats(social=10)
        stats._charisma = 5
        self.assertEqual(stats.increase_charisma(2), 2)
        self.assertEqual(stats.charisma(), 7)

    def test_charisma_reduce(self):
        stats = Stats(social=10)
        self.assertEqual(stats.reduce_charisma(2), 2)
        self.assertEqual(stats.charisma(), 8)

    def test_charisma_max_cap(self):
        stats = Stats(social=10)
        stats._charisma = 5
        self.assertEqual(stats.increase_charisma(6), 5)
        self.assertEqual(stats.charisma(), 10)

    def test_charisma_min_cap(self):
        stats = Stats(social=10)
        self.assertEqual(stats.reduce_charisma(11), 10)
        self.assertEqual(stats.charisma(), 0)

    def test_social_increase(self):
        stats = Stats(social=10)
        self.assertEqual(stats.increase_social(6), 6)
        self.assertEqual(stats.social(), 16)

    def test_social_reduce(self):
        stats = Stats(social=10)
        self.assertEqual(stats.charisma(), 10)
        self.assertEqual(stats.reduce_social(4), 4)
        self.assertEqual(stats.social(), 6)
        self.assertEqual(stats.charisma(), 6)

    def test_social_min_cap(self):
        stats = Stats(social=10)
        self.assertEqual(stats.charisma(), 10)
        self.assertEqual(stats.reduce_social(11), 10)
        self.assertEqual(stats.social(), 0)
        self.assertEqual(stats.charisma(), 0)

    def test_physicality_increase(self):
        stats = Stats(physicality=10)
        stats._physicality = 5
        self.assertEqual(stats.increase_physicality(2), 2)
        self.assertEqual(stats.physicality(), 7)

    def test_physicality_reduce(self):
        stats = Stats(physicality=10)
        self.assertEqual(stats.reduce_physicality(2), 2)
        self.assertEqual(stats.physicality(), 8)

    def test_physicality_max_cap(self):
        stats = Stats(physicality=10)
        stats._physicality = 5
        self.assertEqual(stats.increase_physicality(6), 5)
        self.assertEqual(stats.physicality(), 10)

    def test_physicality_min_cap(self):
        stats = Stats(physicality=10)
        self.assertEqual(stats.reduce_physicality(11), 10)
        self.assertEqual(stats.physicality(), 0)

    def test_physicality_base_increase(self):
        stats = Stats(physicality=10)
        self.assertEqual(stats.increase_physicality_base(6), 6)
        self.assertEqual(stats.physicality_base(), 16)

    def test_physicality_base_reduce(self):
        stats = Stats(physicality=10)
        self.assertEqual(stats.physicality(), 10)
        self.assertEqual(stats.reduce_physicality_base(4), 4)
        self.assertEqual(stats.physicality_base(), 6)
        self.assertEqual(stats.physicality(), 6)

    def test_physicality_base_min_cap(self):
        stats = Stats(physicality=10)
        self.assertEqual(stats.physicality(), 10)
        self.assertEqual(stats.reduce_physicality_base(11), 10)
        self.assertEqual(stats.physicality_base(), 0)
        self.assertEqual(stats.physicality(), 0)

    def test_dexterity_increase(self):
        stats = Stats(dexterity=10)
        stats._dexterity = 5
        self.assertEqual(stats.increase_dexterity(2), 2)
        self.assertEqual(stats.dexterity(), 7)

    def test_dexterity_reduce(self):
        stats = Stats(dexterity=10)
        self.assertEqual(stats.reduce_dexterity(2), 2)
        self.assertEqual(stats.dexterity(), 8)

    def test_dexterity_max_cap(self):
        stats = Stats(dexterity=10)
        stats._dexterity = 5
        self.assertEqual(stats.increase_dexterity(6), 5)
        self.assertEqual(stats.dexterity(), 10)

    def test_dexterity_min_cap(self):
        stats = Stats(dexterity=10)
        self.assertEqual(stats.reduce_dexterity(11), 10)
        self.assertEqual(stats.dexterity(), 0)

    def test_dexterity_base_increase(self):
        stats = Stats(dexterity=10)
        self.assertEqual(stats.increase_dexterity_base(6), 6)
        self.assertEqual(stats.dexterity_base(), 16)

    def test_dexterity_base_reduce(self):
        stats = Stats(dexterity=10)
        self.assertEqual(stats.dexterity(), 10)
        self.assertEqual(stats.reduce_dexterity_base(4), 4)
        self.assertEqual(stats.dexterity_base(), 6)
        self.assertEqual(stats.dexterity(), 6)

    def test_dexterity_base_min_cap(self):
        stats = Stats(dexterity=10)
        self.assertEqual(stats.dexterity(), 10)
        self.assertEqual(stats.reduce_dexterity_base(11), 10)
        self.assertEqual(stats.dexterity_base(), 0)
        self.assertEqual(stats.dexterity(), 0)

    def test_experience(self):
        stats = Stats(experience=10)
        self.assertEqual(stats.experience(), 10)
        self.assertEqual(stats.increase_experience(5), 5)
        self.assertEqual(stats.experience(), 15)
