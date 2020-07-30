"""
All tests for the stats library.
"""
import unittest

from game_code.stats import Stats


class TestStats(unittest.TestCase):
    def test_health_increase(self):
        stats = Stats()
        stats._constitution = 10
        stats._health = 5
        self.assertEqual(2, stats.increase_health(2))
        self.assertEqual(7, stats._health)

    def test_health_reduce(self):
        stats = Stats()
        stats._health = 5
        self.assertEqual(7, stats.reduce_health(7))
        self.assertEqual(-2, stats._health)

    def test_health_max_cap(self):
        stats = Stats(constitution=10)
        stats._health = 5
        self.assertEqual(stats.increase_health(6), 5)
        self.assertEqual(10, stats._health)

    def test_constitution_increase(self):
        stats = Stats()
        stats._constitution = 5
        self.assertEqual(6, stats.increase_constitution(6))
        self.assertEqual(11, stats._constitution)

    def test_constitution_reduce(self):
        stats = Stats()
        stats._constitution = 5
        stats._health = 5
        self.assertEqual(4, stats.reduce_constitution(4))
        self.assertEqual(1, stats._constitution)
        self.assertEqual(1, stats._health)

    def test_constitution_min_cap(self):
        stats = Stats()
        stats._constitution = 5
        self.assertEqual(5, stats.reduce_constitution(6))
        self.assertEqual(0, stats._constitution)
        self.assertEqual(0, stats._health)

    def test_mana_increase(self):
        stats = Stats()
        stats._magic_base = 10
        stats._mana = 5
        self.assertEqual(2, stats.increase_mana(2))
        self.assertEqual(7, stats._mana)

    def test_mana_reduce(self):
        stats = Stats()
        stats._mana = 5
        self.assertEqual(2, stats.reduce_mana(2))
        self.assertEqual(3, stats._mana)

    def test_mana_max_cap(self):
        stats = Stats()
        stats._magic_base = 10
        stats._mana = 5
        self.assertEqual(5, stats.increase_mana(6))
        self.assertEqual(10, stats._mana)

    def test_mana_min_cap(self):
        stats = Stats()
        stats._mana = 5
        self.assertEqual(5, stats.reduce_mana(11))
        self.assertEqual(0, stats._mana)

    def test_magic_base_increase(self):
        stats = Stats()
        stats._magic_base = 10
        self.assertEqual(6, stats.increase_magic_base(6))
        self.assertEqual(16, stats._magic_base)

    def test_magic_base_reduce(self):
        stats = Stats()
        stats._magic_base = 10
        stats._mana = 10
        self.assertEqual(4, stats.reduce_magic_base(4))
        self.assertEqual(6, stats._magic_base)
        self.assertEqual(6, stats._mana)

    def test_magic_base_min_cap(self):
        stats = Stats()
        stats._magic_base = 10
        stats._mana = 10
        self.assertEqual(10, stats.reduce_magic_base(11))
        self.assertEqual(0, stats._magic_base)
        self.assertEqual(0, stats._mana)

    def test_charisma_increase(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 5
        self.assertEqual(2, stats.increase_charisma(2))
        self.assertEqual(7, stats._charisma)

    def test_charisma_reduce(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 5
        self.assertEqual(2, stats.reduce_charisma(2))
        self.assertEqual(3, stats._charisma)

    def test_charisma_max_cap(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 5
        self.assertEqual(5, stats.increase_charisma(6))
        self.assertEqual(10, stats._charisma)

    def test_charisma_min_cap(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 10
        self.assertEqual(10, stats.reduce_charisma(11))
        self.assertEqual(0, stats._charisma)

    def test_social_increase(self):
        stats = Stats()
        stats._social = 10
        self.assertEqual(6, stats.increase_social(6))
        self.assertEqual(16, stats._social)

    def test_social_reduce(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 10
        self.assertEqual(4, stats.reduce_social(4))
        self.assertEqual(6, stats._social)
        self.assertEqual(6, stats._charisma)

    def test_social_min_cap(self):
        stats = Stats()
        stats._social = 10
        stats._charisma = 5
        self.assertEqual(10, stats.reduce_social(11))
        self.assertEqual(0, stats._social)
        self.assertEqual(0, stats._charisma)

    def test_physicality_increase(self):
        stats = Stats()
        stats._physicality_base = 10
        stats._physicality = 5
        self.assertEqual(2, stats.increase_physicality(2))
        self.assertEqual(7, stats._physicality)

    def test_physicality_reduce(self):
        stats = Stats()
        stats._physicality = 5
        self.assertEqual(2, stats.reduce_physicality(2))
        self.assertEqual(3, stats._physicality)

    def test_physicality_max_cap(self):
        stats = Stats()
        stats._physicality_base = 10
        stats._physicality = 5
        self.assertEqual(5, stats.increase_physicality(6))
        self.assertEqual(10, stats._physicality)

    def test_physicality_min_cap(self):
        stats = Stats()
        stats._physicality = 5
        self.assertEqual(5, stats.reduce_physicality(11))
        self.assertEqual(0, stats._physicality)

    def test_physicality_base_increase(self):
        stats = Stats()
        stats._physicality_base = 10
        self.assertEqual(6, stats.increase_physicality_base(6))
        self.assertEqual(16, stats.physicality_base())

    def test_physicality_base_reduce(self):
        stats = Stats()
        stats._physicality_base = 10
        stats._physicality = 10
        self.assertEqual(4, stats.reduce_physicality_base(4))
        self.assertEqual(6, stats._physicality_base)
        self.assertEqual(6, stats._physicality)

    def test_physicality_base_min_cap(self):
        stats = Stats()
        stats._physicality_base = 10
        stats._physicality = 5
        self.assertEqual(10, stats.reduce_physicality_base(11))
        self.assertEqual(0, stats._physicality_base)
        self.assertEqual(0, stats._physicality)

    def test_dexterity_increase(self):
        stats = Stats()
        stats._dexterity_base = 10
        stats._dexterity = 5
        self.assertEqual(2, stats.increase_dexterity(2))
        self.assertEqual(7, stats._dexterity)

    def test_dexterity_reduce(self):
        stats = Stats()
        stats._dexterity = 5
        self.assertEqual(2, stats.reduce_dexterity(2))
        self.assertEqual(3, stats._dexterity)

    def test_dexterity_max_cap(self):
        stats = Stats()
        stats._dexterity_base = 10
        stats._dexterity = 5
        self.assertEqual(5, stats.increase_dexterity(6))
        self.assertEqual(10, stats._dexterity)

    def test_dexterity_min_cap(self):
        stats = Stats()
        stats._dexterity = 5
        self.assertEqual(5, stats.reduce_dexterity(11))
        self.assertEqual(0, stats._dexterity)

    def test_dexterity_base_increase(self):
        stats = Stats()
        stats._dexterity_base = 10
        self.assertEqual(6, stats.increase_dexterity_base(6))
        self.assertEqual(16, stats._dexterity_base)

    def test_dexterity_base_reduce(self):
        stats = Stats()
        stats._dexterity_base = 10
        stats._dexterity = 10
        self.assertEqual(4, stats.reduce_dexterity_base(4))
        self.assertEqual(6, stats._dexterity_base)
        self.assertEqual(6, stats._dexterity)

    def test_dexterity_base_min_cap(self):
        stats = Stats()
        stats._dexterity_base = 10
        stats._dexterity = 5
        self.assertEqual(10, stats.reduce_dexterity_base(11))
        self.assertEqual(0, stats._dexterity_base)
        self.assertEqual(0, stats._dexterity)

    def test_increase_experience(self):
        stats = Stats()
        stats._experience = 10
        self.assertEqual(5, stats.increase_experience(5))
        self.assertEqual(15, stats._experience)
