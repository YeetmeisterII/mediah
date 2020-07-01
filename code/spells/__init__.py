from mediah.actions import AttackAction, HealingAction, Action


class Spell:
    def __init__(self, cost: int = 0):
        self._mana_cost = cost

    def is_castable(self, caster: "Creature"):
        """
        Check whether spell can be cast.
        :param caster: Creature being checked.
        :return: If creature can cast spell.
        """
        return caster.magic_enabled() and (self._mana_cost <= caster.mana())

    def cast(self, executor: "Creature", target: object) -> Action:
        pass


class HealingSpell(Spell):
    def __init__(self, healing_quantity: int, **kwargs):
        super().__init__(**kwargs)
        self._healing_quantity = healing_quantity

    def cast(self, executor: "Creature", target: object) -> HealingAction:
        """
        Cast spell that attempts to heal target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Healing action.
        """
        return HealingAction(executor=executor, target=target, healing_quantity=self._healing_quantity)


class OffensiveSpell(Spell):
    def __init__(self, damage: int, **kwargs):
        super().__init__(**kwargs)
        self._damage = damage

    def cast(self, executor: "Creature", target: object) -> AttackAction:
        """
        Cast spell that attempts to deal damage to target.
        :param executor: Creature casting spell.
        :param target: Target of the spell.
        :return: Attack action.
        """
        return AttackAction(executor=executor, target=target, damage=self._damage)
