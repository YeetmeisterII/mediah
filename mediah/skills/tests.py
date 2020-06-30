import unittest

from mediah.actions import NullAction, AttackAction
from mediah.creatures import Creature
from mediah.skills import Skill, OffensiveSkill, HarshLanguage


class TestSkillMethods(unittest.TestCase):
    def test_use_action(self):
        skill = Skill()
        action = skill.use(Creature(), Creature())
        self.assertEqual(type(action), NullAction)


class TestOffensiveSkillMethods(unittest.TestCase):
    def test_use_action(self):
        skill = OffensiveSkill()
        action = skill.use(Creature(), Creature())
        self.assertEqual(type(action), AttackAction)

    def test_use_action_base_damage(self):
        skill = OffensiveSkill(base_value=10, dice_max=0, dice_quantity=0)
        for i in range(50):
            action = skill.use(Creature(), Creature())
            self.assertEqual(action.damage(), 10)

    def test_use_action_rolled_damage_minimum(self):
        skill = OffensiveSkill(dice_max=1, dice_quantity=10, base_value=0)
        for i in range(50):
            action = skill.use(Creature(), Creature())
            self.assertEqual(action.damage(), 10)

    def test_use_action_rolled_damage_variable(self):
        skill = OffensiveSkill(dice_max=2, dice_quantity=10, base_value=0)
        min_message = "Minimum die value is ten. Therefore minimum possible damage must be 10."
        for i in range(50):
            action = skill.use(Creature(), Creature())
            damage = action.damage()
            self.assertGreaterEqual(damage, 10, msg=min_message)
            self.assertLessEqual(damage, 20)

    def test_use_action_executor(self):
        skill = OffensiveSkill()
        creature1 = Creature()
        creature2 = Creature()
        action = skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.executor(), creature1)

    def test_use_action_target(self):
        skill = OffensiveSkill()
        creature1 = Creature()
        creature2 = Creature()
        action = skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.target(), creature2)


class TestHarshLanguageMethods(unittest.TestCase):
    def test_use_action_base_damage_using_social(self):
        skill = HarshLanguage(base_value=1, dice_max=0, dice_quantity=0)
        for i in range(50):
            action = skill.use(Creature(social=5), Creature())
            self.assertEqual(action.damage(), 5)

    def test_use_action_executor(self):
        skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.executor(), creature1)

    def test_use_action_target(self):
        skill = HarshLanguage()
        creature1 = Creature()
        creature2 = Creature()
        action = skill.use(executor=creature1, target=creature2)
        self.assertEqual(action.target(), creature2)
