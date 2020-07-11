import unittest

from game_code.actions import NullAction
from game_code.creatures import Creature
from game_code.skills import Skill, HarshLanguage


class TestSkillMethods(unittest.TestCase):
    def test_use_action(self):
        skill = Skill()
        action = skill.use(Creature(), Creature())
        self.assertEqual(NullAction, type(action))


class TestHarshLanguageMethods(unittest.TestCase):
    def test_use_action_base_damage_using_social(self):
        harsh_language_skill = HarshLanguage(base_value=10, dice_quantity=0, dice_max=0)
        action = harsh_language_skill.use(Creature(social=5), Creature())
        self.assertEqual(5, action.damage())

    def test_use_action_executor(self):
        harsh_language_skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = harsh_language_skill.use(executor=creature1, target=creature2)
        self.assertEqual(creature1, action.executor())

    def test_use_action_target(self):
        harsh_language_skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = harsh_language_skill.use(executor=creature1, target=creature2)
        self.assertEqual(creature2, action.target())
