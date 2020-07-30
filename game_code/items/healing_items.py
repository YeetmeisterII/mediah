"""
Types of healing potions that can be used.
"""
from game_code.actions import HealingAction
from game_code.creatures import Creature
from game_code.items import ConsumableItem


class HealingPotion(ConsumableItem):
    """
    Base healing potion class.
    """
    _healing_quantity = None

    def __init__(self, value: int):
        super().__init__(name=self._name, value=value, remaining_uses=1, weight=1)

    def healing_quantity(self) -> int:
        """
        :return: Amount of health the potion can restore.
        """
        return self._healing_quantity

    def use(self, executor: Creature, target: Creature) -> HealingAction:
        """
        Attempt to heal the target creature.
        :param executor: Creature using the potion.
        :param target: Creature being healed by potion.
        :return: HealingAction instance.
        """
        self._remaining_uses -= 1
        return HealingAction(executor=executor, target=target, healing_quantity=self._healing_quantity, tool_used=self)


class LesserHealingPotion(HealingPotion):
    """
    Low-tier healing potion.
    """
    _healing_quantity = 10
    _name = "Lesser Healing Potion"

    def __init__(self):
        super().__init__(value=7)


class IntermediateHealingPotion(HealingPotion):
    """
    Mid-tier healing potion.
    """
    _healing_quantity = 20
    _name = "Intermediate Healing Potion"

    def __init__(self):
        super().__init__(value=16)


class GreaterHealingPotion(HealingPotion):
    """
    High-tier healing potion.
    """
    _healing_quantity = 30
    _name = "Greater Healing Potion"

    def __init__(self):
        super().__init__(value=30)
