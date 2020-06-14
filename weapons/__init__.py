import random
from typing import Dict


class Weapon:
    def __init__(self,
                 name: str = 'Hurty Thingy', weapon_type: str = '', base_damage: int = 0, dice_quantity: int = 0,
                 dice_max: int = 0):
        self._name = name
        self._name_changed = False if name == '' else True
        self._weapon_type = weapon_type
        self._base_value = base_damage
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max

    def name(self) -> str:
        """
        Returns the name of the weapon. If the weapon name has been changed from the default, the weapon type will be
        appended to the end.
        :return: Name of weapon.
        """
        name = f'{self._name} ({self._weapon_type})' if self._name_changed else self._name
        return name

    def change_name(self, new_name: str) -> str:
        self._name = new_name
        return new_name

    def type(self):
        return self._weapon_type

    def base_value(self) -> int:
        return self._base_value

    def dice_quantity(self) -> int:
        return self._dice_quantity

    def dice_faces(self) -> int:
        return self._dice_max

    def execute(self, executor: 'Creature') -> Dict[str, int]:
        """
        Calculated the damage of the weapon based on the quantity of dice, their max value and the base value.
        :param executor: The Creature performing the attack.
        :return: Dictionary containing the calculated damage.
        """
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return {'damage': damage}


class Unarmed(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 1, name: str = 'Fist', **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name=name, **kwargs)
        self._name_changed = False if name == 'Fist' else True
        self._weapon_type = 'Unarmed'


class Sword(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 6, name: str = 'Sword', **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name=name, **kwargs)
        self._name_changed = False if name == 'Sword' else True
        self._weapon_type = 'Sword'


class Dagger(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 3, name: str = 'Dagger', **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name=name, **kwargs)
        self._name_changed = False if name == 'Dagger' else True
        self._weapon_type = 'Dagger'


class RockFist(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max: int = 8, base_value: int = 3, name: str = 'Rock Fist',
                 **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, base_damage=base_value, name=name, **kwargs)
        self._name_changed = False if name == 'Rock Fist' else True
        self._weapon_type = 'Rock Fist'
