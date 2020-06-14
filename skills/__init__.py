import random


class Skill:
    def __init__(self, dice_quantity: int = 0, dice_max: int = 0, base_value: int = 0, skill_name: str = 'generic_skill'):
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._base_value = base_value
        self._skill_name = skill_name
        self._type = 'generic'

    def execute(self, executer: 'Creature') -> dict:
        pass


class OffensiveSkill(Skill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = 'offensive'

    def execute(self, executer: 'Creature') -> dict:
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return {'damage': damage}


class HarshLanguage(OffensiveSkill):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 4, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, **kwargs)
        self._skill_name = 'Harsh Language'

    def execute(self, executer: 'Creature') -> dict:
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + executer.charisma()
        return {'damage': damage}


class FireBreath(OffensiveSkill):
    def __init__(self, dice_quantity: int = 2, dice_max: int = 12, **kwargs):
        super().__init__(**kwargs)
        self._skill_name = 'Fire Breath'
