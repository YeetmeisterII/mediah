"""
Library of all non-living physical entities excluding weapons.
"""
from typing import Union

from game_code.creatures import Creature


class Item:
    """
    Physical entities that are not living like Creatures.
    """

    def __init__(self, name: str, remaining_uses: Union[int, float], value: int, weight: int):
        self._name = name
        self._remaining_uses = remaining_uses
        self._value = value
        self._weight = weight

    def name(self) -> str:
        """
        :return: Name of the Item.
        """
        return self._name

    def value(self) -> int:
        """
        :return: Value of the item in gold.
        """
        return self._value

    def weight(self) -> int:
        """
        :return: Mass of the Item in arbitrary units.
        """
        return self._weight

    def is_usable(self) -> bool:
        """
        :return: If the consumable can be used.
        """
        return 0 < self._remaining_uses

    def remaining_uses(self) -> Union[int, float]:
        """
        :return: How many more times the item can be used.
        """
        return self._remaining_uses

    def use(self, executor: Creature, target: Creature):
        """
        Create action to perform when used. Delete the consumable once it runs out of uses.
        :param executor: User of the item.
        :param target: Target of the item's action.
        :return: Action to perform.
        """
        pass


class ConsumableItem(Item):
    """
    Item with a limited quantity of uses.
    """

    def __init__(self, remaining_uses: int, **kwargs):
        super().__init__(remaining_uses=remaining_uses, **kwargs)


class NonConsumableItem(Item):
    """
    Item with an unlimited quantity of uses.
    """

    def __init__(self, name: str, value: int, weight: int):
        super().__init__(name=name, value=value, weight=weight, remaining_uses=float("inf"))
