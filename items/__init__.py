from mediah.actions import NullAction


class Item:
    def __init__(self, value: int = 0, weight: int = 0):
        self._value = value
        self._weight = weight

    def value(self) -> int:
        """
        :return: Worth of the item in gold.
        """
        return self._value

    def weight(self) -> int:
        """
        :return: Quantity of inventory weight allowance taken up by the item.
        """
        return self._weight

    def is_usable(self) -> bool:
        """
        :return: If the consumable can be used.
        """
        return True


class Consumable(Item):
    def __init__(self, remaining_uses: int = 1, **kwargs):
        super().__init__(**kwargs)
        self._remaining_uses = remaining_uses

    def is_usable(self) -> bool:
        """
        :return: If the consumable can be used.
        """
        return 0 < self._remaining_uses

    def remaining_uses(self) -> int:
        """
        :return: How many times the item can be used.
        """
        return self._remaining_uses

    def use(self, executor: "Creature", target: object) -> NullAction:
        # TODO: Add method to allow consumable to delete itself from it's inventory.
        """
        Create action to perform when used. Delete the consumable once it runs out of uses.
        :param executor: User of the item.
        :param target: Target of the item's action.
        :return: Action to perform.
        """
        self._remaining_uses -= 1
        return NullAction(executor=executor, target=target)
