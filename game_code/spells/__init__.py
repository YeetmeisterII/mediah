import random

from game_code.actions import AttackAction, HealingAction, NullAction


class Spell:
    def __init__(self, cost: int = 0):
        self._mana_cost = cost

    def is_usable(self, caster: "Creature") -> bool:
        """
        Check whether spell can be cast.
        :param caster: Creature being checked.
        :return: If creature can cast spell.
        """
        return caster.stats().magic_enabled() and (self._mana_cost <= caster.stats().mana())

    def use(self, executor: "Creature", target: "Creature") -> NullAction:
        """
        Create attempted action when spell is used.
        :param executor: Performer of the spell.
        :param target: Target of the spell.
        :return: Action to spell.
        """
        return NullAction(executor=executor, target=target, tool_used=self)


class HealingSpell(Spell):
    def __init__(self, healing_quantity: int, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = healing_quantity

    def use(self, executor: "Creature", target: "Creature") -> HealingAction:
        """
        Cast spell that attempts to heal target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Healing action.
        """
        return HealingAction(executor=executor, target=target, healing_quantity=self._healing_quantity, tool_used=self)


class OffensiveSpell(Spell):
    def __init__(self, damage: int, **kwargs):
        super().__init__(**kwargs)
        self._damage = damage

    def use(self, executor: "Creature", target: "Creature") -> AttackAction:
        """
        Cast spell that attempts to deal damage to target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Attack action.
        """
        hit_index = random.randint(1, 20)
        return AttackAction(damage=self._damage, hit_index=hit_index)
