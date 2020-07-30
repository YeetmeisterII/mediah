"""
Library of weapons that can be used by creatures.
"""
import random

from game_code.actions import AttackAction
from game_code.creatures import Creature
from game_code.items import NonConsumableItem


class Weapon(NonConsumableItem):
    """
    Used to perform attacks. Is a holdable item.
    """
    _weapon_type = None
    _name_changed = False

    def __init__(self, base_value: int, dice_quantity: int, dice_max: int, **kwargs):
        super().__init__(**kwargs)
        self._base_value = base_value
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max

    def name(self) -> str:
        """
        :return: Name of weapon. Append weapon type onto name if the name has ben changed.
        """
        return f"{self._name} ({self._weapon_type})" if self._name_changed else self._name

    def has_name_changed(self) -> bool:
        """
        :return: Whether the weapon no longer has the default name.
        """
        return self._name_changed

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

    def use(self, executor: Creature, target: Creature) -> AttackAction:
        """
        Create attempted action upon the target when weapon is used.
        :param executor: Performer of the skill.
        :param target: Target of the skill.
        :return: Action to perform.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return AttackAction(executor=executor, target=target, damage=damage, hit_index=hit_index, tool_used=self)


class Unarmed(Weapon):
    """
    Default weapon for most creatures if no weapon is equipped.
    """
    _weapon_type = "Fist"

    def __init__(self, name: str = "Fist", **kwargs):
        super().__init__(name=name, **kwargs)
        self._name_changed = (self._name != "Fist")


class Sword(Weapon):
    """
    Orthodox weapon.
    """
    _weapon_type = "Sword"

    def __init__(self, name: str = "Sword", **kwargs):
        super().__init__(name=name, **kwargs)
        self._name_changed = (name != "Sword")


class Dagger(Weapon):
    """
    Orthodox weapon.
    """
    _weapon_type = "Dagger"

    def __init__(self, name: str = "Dagger", **kwargs):
        super().__init__(name=name, **kwargs)
        self._name_changed = (name != "Dagger")


class RockFist(Weapon):
    """
    Default racial weapon for Earth Elementals.
    """
    _weapon_type = "Rock Fist"

    def __init__(self, name: str = "Rock Fist", **kwargs):
        super().__init__(name=name, **kwargs)
        self._name_changed = (name != "Rock Fist")
