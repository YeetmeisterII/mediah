import unittest

from code.actions import NullAction
from code.creatures import Creature
from code.skills import Skill, HarshLanguage


class TestSkillMethods(unittest.TestCase):
    def test_use_action(self):
        skill = Skill()
        action = skill.use(Creature(), Creature())
        self.assertEqual(type(action), NullAction)


class TestHarshLanguageMethods(unittest.TestCase):
    def test_use_action_base_damage_using_social(self):
        harsh_language_skill = HarshLanguage(base_value=10, dice_quantity=0, dice_max=0)
        action = harsh_language_skill.use(Creature(social=5), Creature())
        self.assertEqual(action.damage(), 5)

    def test_use_action_executor(self):
        harsh_language_skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = harsh_language_skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.executor(), creature1)

    def test_use_action_target(self):
        harsh_language_skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = harsh_language_skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.target(), creature2)
