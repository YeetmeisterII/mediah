from mediah.actions import Attack


class Spell:
    def __init__(self, name: str = "Unknown magic", cost: int = 0):
        self._name = name
        self._mana_cost = cost

    def is_castable(self, caster: "Creature"):
        if caster.magic_enabled() and (self._mana_cost <= caster.mana()):
            return True
        else:
            return False

    def cast(self, executor: "Creature", target: "Creature"):
        pass


class HealingSpell(Spell):
    def __init__(self, health: int = 0, **kwargs):
        super().__init__(**kwargs)
        self._health = health

    def cast(self, executor: "Creature", target: "Creature"):
        pass


class OffensiveSpell(Spell):
    def __init__(self, damage: int = 0, **kwargs):
        super().__init__(**kwargs)
        self._damage = damage

    def cast(self, executor: "Creature", target: "Creature"):
        return Attack(executor, target, self._damage)
