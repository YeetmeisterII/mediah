import unittest

from code.actions import NullAction, HealingAction
from code.creatures import Creature
from code.spells import Spell, HealingSpell


class TestSpellMethods(unittest.TestCase):
    def test_is_usable(self):
        spell = Spell(cost=1)
        spell_casting_creature = Creature(magic_enabled=True, magic_base=1000)
        self.assertEqual(True, spell.is_usable(spell_casting_creature))

    def test_not_usable(self):
        spell = Spell(cost=1)
        non_spell_casting_creature = Creature(magic_enabled=False, magic_base=0)
        self.assertEqual(False, spell.is_usable(non_spell_casting_creature))

    def test_use_action_type(self):
        spell = Spell()
        action = spell.use(Creature(), Creature())
        self.assertEqual(NullAction, type(action))


class TestHealingSpellMethods(unittest.TestCase):
    def test_use_action_type(self):
        healing_spell = HealingSpell(healing_quantity=0)
        action = healing_spell.use(Creature(), Creature())
        self.assertEqual(HealingAction, type(action))

    def test_use_action_healing_quantity(self):
        healing_spell = HealingSpell(healing_quantity=5)
        action = healing_spell.use(Creature(), Creature())
        self.assertEqual(5, action.healing_quantity())

    def test_use_action_executor(self):
        healing_spell = HealingSpell(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_spell.use(executor=creature1, target=creature2)
        self.assertEqual(creature1, action.executor())

    def test_use_action_target(self):
        healing_spell = HealingSpell(healing_quantity=0)
        creature1 = Creature()
        creature2 = Creature()
        action = healing_spell.use(executor=creature1, target=creature2)
        self.assertEqual(creature2, action.target())
