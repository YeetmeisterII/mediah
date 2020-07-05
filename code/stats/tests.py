import unittest

from code.stats import Stats


class TestStatsMethods(unittest.TestCase):
    def test_health_increase(self):
        stats = Stats(constitution=10)
        stats._health = 5
        self.assertEqual(2, stats.increase_health(2))
        self.assertEqual(7, stats.health())

    def test_health_reduce(self):
        stats = Stats(constitution=10)
        self.assertEqual(12, stats.reduce_health(12))
        self.assertEqual(-2, stats.health())

    def test_health_max_cap(self):
        stats = Stats(constitution=10)
        stats._health = 5
        self.assertEqual(stats.increase_health(6), 5)
        self.assertEqual(10, stats.health())

    def test_constitution_increase(self):
        stats = Stats(constitution=10)
        self.assertEqual(10, stats.increase_constitution(10))
        self.assertEqual(20, stats.constitution())

    def test_constitution_reduce(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.health(), 10)
        self.assertEqual(stats.reduce_constitution(4), 4)
        self.assertEqual(6, stats.constitution())
        self.assertEqual(6, stats.health())

    def test_constitution_min_cap(self):
        stats = Stats(constitution=10)
        self.assertEqual(stats.reduce_constitution(11), 10)
        self.assertEqual(0, stats.constitution())
        self.assertEqual(0, stats.health())

    def test_mana_increase(self):
        stats = Stats(magic_base=10)
        stats._mana = 5
        self.assertEqual(2, stats.increase_mana(2))
        self.assertEqual(7, stats.mana())

    def test_mana_reduce(self):
        stats = Stats(magic_base=10)
        self.assertEqual(2, stats.reduce_mana(2))
        self.assertEqual(8, stats.mana())

    def test_mana_max_cap(self):
        stats = Stats(magic_base=10)
        stats._mana = 5
        self.assertEqual(5, stats.increase_mana(6))
        self.assertEqual(10, stats.mana())

    def test_mana_min_cap(self):
        stats = Stats(magic_base=10)
        self.assertEqual(10, stats.reduce_mana(11))
        self.assertEqual(0, stats.mana())

    def test_magic_base_increase(self):
        stats = Stats(magic_base=10)
        self.assertEqual(6, stats.increase_magic_base(6))
        self.assertEqual(16, stats.magic_base())

    def test_magic_base_reduce(self):
        stats = Stats(magic_base=10)
        self.assertEqual(10, stats.mana())
        self.assertEqual(4, stats.reduce_magic_base(4))
        self.assertEqual(6, stats.magic_base())
        self.assertEqual(6, stats.mana())

    def test_magic_base_min_cap(self):
        stats = Stats(magic_base=10)
        self.assertEqual(10, stats.mana())
        self.assertEqual(10, stats.reduce_magic_base(11))
        self.assertEqual(0, stats.magic_base())
        self.assertEqual(0, stats.mana())

    def test_charisma_increase(self):
        stats = Stats(social=10)
        stats._charisma = 5
        self.assertEqual(2, stats.increase_charisma(2))
        self.assertEqual(7, stats.charisma())

    def test_charisma_reduce(self):
        stats = Stats(social=10)
        self.assertEqual(2, stats.reduce_charisma(2))
        self.assertEqual(8, stats.charisma())

    def test_charisma_max_cap(self):
        stats = Stats(social=10)
        stats._charisma = 5
        self.assertEqual(5, stats.increase_charisma(6))
        self.assertEqual(10, stats.charisma())

    def test_charisma_min_cap(self):
        stats = Stats(social=10)
        self.assertEqual(10, stats.reduce_charisma(11))
        self.assertEqual(0, stats.charisma())

    def test_social_increase(self):
        stats = Stats(social=10)
        self.assertEqual(6, stats.increase_social(6))
        self.assertEqual(16, stats.social())

    def test_social_reduce(self):
        stats = Stats(social=10)
        self.assertEqual(10, stats.charisma())
        self.assertEqual(4, stats.reduce_social(4))
        self.assertEqual(6, stats.social())
        self.assertEqual(6, stats.charisma())

    def test_social_min_cap(self):
        stats = Stats(social=10)
        self.assertEqual(10, stats.charisma())
        self.assertEqual(10, stats.reduce_social(11))
        self.assertEqual(0, stats.social())
        self.assertEqual(0, stats.charisma())

    def test_physicality_increase(self):
        stats = Stats(physicality=10)
        stats._physicality = 5
        self.assertEqual(2, stats.increase_physicality(2))
        self.assertEqual(7, stats.physicality())

    def test_physicality_reduce(self):
        stats = Stats(physicality=10)
        self.assertEqual(2, stats.reduce_physicality(2))
        self.assertEqual(8, stats.physicality())

    def test_physicality_max_cap(self):
        stats = Stats(physicality=10)
        stats._physicality = 5
        self.assertEqual(5, stats.increase_physicality(6))
        self.assertEqual(10, stats.physicality())

    def test_physicality_min_cap(self):
        stats = Stats(physicality=10)
        self.assertEqual(10, stats.reduce_physicality(11))
        self.assertEqual(0, stats.physicality())

    def test_physicality_base_increase(self):
        stats = Stats(physicality=10)
        self.assertEqual(6, stats.increase_physicality_base(6))
        self.assertEqual(16, stats.physicality_base())

    def test_physicality_base_reduce(self):
        stats = Stats(physicality=10)
        self.assertEqual(10, stats.physicality())
        self.assertEqual(4, stats.reduce_physicality_base(4))
        self.assertEqual(6, stats.physicality_base())
        self.assertEqual(6, stats.physicality())

    def test_physicality_base_min_cap(self):
        stats = Stats(physicality=10)
        self.assertEqual(10, stats.physicality())
        self.assertEqual(10, stats.reduce_physicality_base(11))
        self.assertEqual(0, stats.physicality_base())
        self.assertEqual(0, stats.physicality())

    def test_dexterity_increase(self):
        stats = Stats(dexterity=10)
        stats._dexterity = 5
        self.assertEqual(2, stats.increase_dexterity(2))
        self.assertEqual(7, stats.dexterity())

    def test_dexterity_reduce(self):
        stats = Stats(dexterity=10)
        self.assertEqual(2, stats.reduce_dexterity(2))
        self.assertEqual(8, stats.dexterity())

    def test_dexterity_max_cap(self):
        stats = Stats(dexterity=10)
        stats._dexterity = 5
        self.assertEqual(5, stats.increase_dexterity(6))
        self.assertEqual(10, stats.dexterity())

    def test_dexterity_min_cap(self):
        stats = Stats(dexterity=10)
        self.assertEqual(10, stats.reduce_dexterity(11))
        self.assertEqual(0, stats.dexterity())

    def test_dexterity_base_increase(self):
        stats = Stats(dexterity=10)
        self.assertEqual(6, stats.increase_dexterity_base(6))
        self.assertEqual(16, stats.dexterity_base())

    def test_dexterity_base_reduce(self):
        stats = Stats(dexterity=10)
        self.assertEqual(10, stats.dexterity())
        self.assertEqual(4, stats.reduce_dexterity_base(4))
        self.assertEqual(6, stats.dexterity_base())
        self.assertEqual(6, stats.dexterity())

    def test_dexterity_base_min_cap(self):
        stats = Stats(dexterity=10)
        self.assertEqual(10, stats.dexterity())
        self.assertEqual(10, stats.reduce_dexterity_base(11))
        self.assertEqual(0, stats.dexterity_base())
        self.assertEqual(0, stats.dexterity())

    def test_experience(self):
        stats = Stats(experience=10)
        self.assertEqual(10, stats.experience())
        self.assertEqual(5, stats.increase_experience(5))
        self.assertEqual(15, stats.experience())
