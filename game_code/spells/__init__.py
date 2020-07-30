"""
Library containing the spells that Creatures can learn to cast.
"""
import random

from game_code.actions import AttackAction, HealingAction
from game_code.creatures import Creature


class Spell:
    """
    Base spell class.
    """

    def __init__(self, cost: int):
        self._mana_cost = cost

    def is_usable(self, caster: Creature) -> bool:
        """
        Check whether spell can be cast.
        :param caster: Creature being checked.
        :return: If creature can cast spell.
        """
        return caster.stats().magic_enabled() and (self._mana_cost <= caster.stats().mana())

    def use(self, executor: Creature, target: Creature) -> None:
        """
        Create attempted action when spell is used.
        :param executor: Performer of the spell.
        :param target: Target of the spell.
        :return: Action to spell.
        """
        pass


class HealingSpell(Spell):
    """
    Base class for spells that heal Creatures.
    """

    def __init__(self, healing_quantity: int, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = healing_quantity

    def use(self, executor: Creature, target: Creature) -> HealingAction:
        """
        Cast spell that attempts to heal target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Healing action.
        """
        return HealingAction(executor=executor, target=target, healing_quantity=self._healing_quantity, tool_used=self)


class OffensiveSpell(Spell):
    """
    Base class for spells that deal damage.
    """

    def __init__(self, damage: int, **kwargs):
        super().__init__(**kwargs)
        self._damage = damage

    def use(self, executor: Creature, target: Creature) -> AttackAction:
        """
        Cast spell that attempts to deal damage to target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Attack action.
        """
        hit_index = random.randint(1, 20)
        return AttackAction(executor=executor, target=target, damage=self._damage, hit_index=hit_index, tool_used=self)
