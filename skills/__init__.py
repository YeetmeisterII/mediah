import random

from mediah.attacks import Attack


class Skill:
    def __init__(self, dice_quantity: int = 0, dice_max: int = 0, base_value: int = 0,
                 skill_name: str = 'generic_skill'):
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._base_value = base_value
        self._name = skill_name
        self._type = 'generic'

    def name(self) -> str:
        return self._name

    def dice_quantity(self) -> int:
        return self._dice_quantity

    def dice_max(self) -> int:
        return self._dice_max

    def base_value(self) -> int:
        return self._base_value

    def type(self):
        return self._type

    def execute(self, executor: 'Creature') -> dict:
        pass


class OffensiveSkill(Skill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = 'offensive'

    def execute(self, executor: 'Creature') -> Attack:
        """
        Calculated the damage of the skill based on the quantity of dice, their max value and the base value.
        :param executor: The Creature performing the skill.
        :return: An Attack object.
        """
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return Attack(damage=damage)


class HarshLanguage(OffensiveSkill):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 4, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, **kwargs)
        self._name = 'Harsh Language'

    def execute(self, executor: 'Creature') -> Attack:
        """
        Calculated the damage of the skill based on the quantity of dice, their max value and the executor's charisma.
        :param executor: The Creature performing the skill.
        :return: An Attack object.
        """
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + executor.charisma()
        return Attack(damage=damage)


class FireBreath(OffensiveSkill):
    def __init__(self, dice_quantity: int = 2, dice_max: int = 12, **kwargs):
        super().__init__(**kwargs)
        self._name = 'Fire Breath'
