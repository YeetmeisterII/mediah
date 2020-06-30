import random

from mediah.actions import AttackAction


class Weapon:
    def __init__(self, name: str = "Hurty stick", base_value: int = 0, dice_quantity: int = 0, dice_max: int = 0):
        self._name = name
        self._name_changed = False if name == "" else True
        self._base_value = base_value
        self._dice_quantity = dice_quantity
        self._dice_max = dice_max
        self._weapon_type = ''

    def name(self) -> str:
        """
        Returns the name of the weapon. If the weapon name has been changed from the default, the weapon type will be
        appended to the end.
        :return: Name of weapon.
        """
        name = f"{self._name} ({self._weapon_type})" if self._name_changed else self._name
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

    def use(self, executor: "Creature", target: "Creature") -> AttackAction:
        """
        Calculated the damage of the weapon based on the quantity of dice, their max value and the base value.
        :param executor: The Creature performing the attack.
        :param target: Object that receives the attack.
        :return: An Attack object.
        """
        hit_index = random.randint(1, 20)
        rolled_damage = sum(random.randint(1, self._dice_max) for roll in range(self._dice_quantity))
        damage = rolled_damage + self._base_value
        return AttackAction(executor, target, damage, hit_index)


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
