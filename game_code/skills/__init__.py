"""
Library containing the skills that can be learnt by Creatures.
"""
import random

from game_code.actions import AttackAction, NullAction
from game_code.creatures import Creature


class Skill:
    """
    Base skill class.
    """

    _name = None

    def __init__(self, dice_quantity: int, dice_max: int, base_value: int):
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._base_value = base_value

    def name(self) -> str:
        """
        :return: Name of skill.
        """
        return self._name

    def dice_quantity(self) -> int:
        """
        :return: Number of dice thrown when calculating the value of the skill's action.
        """
        return self._dice_quantity

    def dice_max(self) -> int:
        """
        :return: Max value a dice roll can be.
        """
        return self._dice_max

    def base_value(self) -> int:
        """
        :return: Constant value always added to the calculation of a skill's action.
        """
        return self._base_value

    def use(self, executor: Creature, target: Creature) -> NullAction:
        """
        Create attempted action upon the target when skill is used.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        """
        pass


class OffensiveSkill(Skill):
    """
    Base class for skills primarily used to deal damage.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, executor: Creature, target: Creature) -> AttackAction:
        """
        Calculate damage of skill based on quantity of dice, max value of the dice and the base value.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index, tool_used=self)


class HarshLanguage(OffensiveSkill):
    """
    Racial skill for Djinns. It uses the orthodox attack logic except the executors charisma is added to the damage
    instead of the base damage.
    """
    _name = "Harsh Language"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, executor: Creature, target: Creature) -> AttackAction:
        """
        Calculate damage of skill based on quantity of dice, max value of the dice and the executor's charisma.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + executor.stats().charisma()
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index, tool_used=self)


class FireBreath(OffensiveSkill):
    """
    Racial skill for Dragons.
    """
    _name = "Fire Breath"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
