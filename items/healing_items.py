from mediah.actions import HealingAction
from mediah.items import Consumable


class HealingPotion(Consumable):
    def __init__(self, healing_quantity, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = healing_quantity

    def healing_quantity(self) -> int:
        """
        :return: Amount of health the potion can restore.
        """
        return self._healing_quantity

    def use(self, executor: "Creature", target: object) -> HealingAction:
        """
        Create action to perform when used. Delete the potion once it runs out of uses.
        :param executor: User of the item.
        :param target: Target of the item's action.
        :return: Healing action.
        """
        self._remaining_uses -= 1
        return HealingAction(executor=executor, target=target, healing_quantity=self._healing_quantity)


class LesserHealingPotion(HealingPotion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = 10


class IntermediateHealingPotion(HealingPotion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = 20


class GreaterHealingPotion(HealingPotion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = 30
