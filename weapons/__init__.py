import random

from mediah.creatures import Creature


class Weapon:
    def __init__(self,
                 user: Creature = Creature(), name: str = 'Hurty Thingy', weapon_type: str = '', base_damage: int = 0,
                 dice_quantity: int = 0, dice_max: int = 0):
        self._name = name
        self._name_changed = False if name == '' else True
        self._user = user
        self._weapon_type = weapon_type
        self._base_damage = base_damage
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max

    def name(self) -> str:
        name = f'{self._name} ({self._weapon_type})' if self._name_changed else self._name
        return name

    def change_name(self, new_name: str) -> str:
        self._name = new_name
        return new_name

    def change_user(self, new_user: Creature) -> Creature:
        self._user = new_user
        return new_user

    def type(self):
        return self._weapon_type

    def base_damage(self) -> int:
        return self._base_damage

    def dice_quantity(self) -> int:
        return self._dice_quantity

    def dice_faces(self) -> int:
        return self._dice_max

    def execute(self) -> int:
        return sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity)) + self._base_damage


class Unarmed(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max=1, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name='Fist', **kwargs)
        self._weapon_type = 'Unarmed'


class Sword(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max=6, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name='Sword', **kwargs)
        self._weapon_type = 'Sword'


class Dagger(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max=3, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, name='Dagger', **kwargs)
        self._weapon_type = 'Dagger'


class RockFist(Weapon):
    def __init__(self, dice_quantity: int = 1, dice_max=8, base_damage=3, **kwargs):
        super().__init__(dice_quantity=dice_quantity, dice_max=dice_max, base_damage=3, name='Rock Fist', **kwargs)
        self._weapon_type = 'Rock Fist'


