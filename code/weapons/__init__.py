import random

from code.actions import AttackAction
from code.items import Item


class Weapon(Item):
    """
    Used to perform attacks. Is a holdable item.
    """

    def __init__(self, name: str = "default weapon", base_value: int = 0, dice_quantity: int = 0, dice_max: int = 0,
                 **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._name_changed = False if name == "default weapon" else True
        self._base_value = base_value
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._weapon_type = ''

    def name(self) -> str:
        """
        :return: Name of weapon. Append weapon type onto name if the name has ben changed.
        """
        return f"{self._name} ({self._weapon_type})" if self._name_changed else self._name

    def change_name(self, new_name: str) -> str:
        """
        Replace name of weapon and set name_changed to True.
        :param new_name: New weapon name when displayed.
        :return: New name of the weapon.
        """
        self._name = new_name
        self._name_changed = True
        return new_name

    def type(self) -> str:
        """
        :return: The type of weapon e.g. Sword.
        """
        return self._weapon_type

    def base_value(self) -> int:
        """
        :return: Constant value always added to the calculation of a skill's action.
        """
        return self._base_value

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

    def use(self, executor: "Creature", target: object) -> AttackAction:
        """
        Create attempted action upon the target when weapon is used.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index)


class Unarmed(Weapon):
    def __init__(self, name: str = "Fist", **kwargs):
        super().__init__(name, **kwargs)
        self._name_changed = False if name == "Fist" else True
        self._weapon_type = "Unarmed"


class Sword(Weapon):
    def __init__(self, name: str = "Sword", **kwargs):
        super().__init__(name, **kwargs)
        self._name_changed = False if name == "Sword" else True
        self._weapon_type = "Sword"


class Dagger(Weapon):
    def __init__(self, name: str = "Dagger", **kwargs):
        super().__init__(name, **kwargs)
        self._name_changed = False if name == "Dagger" else True
        self._weapon_type = "Dagger"


class RockFist(Weapon):
    def __init__(self, name: str = "Rock Fist", **kwargs):
        super().__init__(name, **kwargs)
        self._name_changed = False if name == "Rock Fist" else True
        self._weapon_type = "Rock Fist"
