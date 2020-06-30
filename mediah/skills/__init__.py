import random

from mediah.actions import AttackAction, Action, NullAction


class Skill:
    def __init__(self, dice_quantity: int = 0, dice_max: int = 0, base_value: int = 0, skill_name: str = "skill"):
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._base_value = base_value
        self._name = skill_name

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

    def use(self, executor: "Creature", target: object) -> Action:
        """
        Create attempted action upon the target when skill is used.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        return NullAction(executor=executor, target=target)


class OffensiveSkill(Skill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, executor: "Creature", target: object) -> AttackAction:
        """
        Calculate damage of skill based on quantity of dice, max value of the dice and the base value.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index)


class HarshLanguage(OffensiveSkill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._name = "Harsh Language"

    def use(self, executor: "Creature", target: object) -> AttackAction:
        """
        Calculate damage of skill based on quantity of dice, max value of the dice and the executor's charisma.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + executor.charisma()
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index)


class FireBreath(OffensiveSkill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._name = "Fire Breath"
