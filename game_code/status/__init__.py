from typing import List

from game_code.status.effects import Block


class Status:
    def __init__(self):
        self._effects = []

    def __contains__(self, effect_type):
        return effect_type in map(type, self._effects)

    def is_blocking(self):
        return Block in self

    def add_effect(self, effect: "Effect"):
        self._effects.append(effect)

    def remove_effect(self, effect: "Effect"):
        self._effects.remove(effect)

    def end_turn(self, self_creature: "Creature") -> List["Response"]:
        return [self._end_turn_effect(effect, self_creature) for effect in self._effects]

    def _end_turn_effect(self, effect: "Effect", self_creature: "Creature") -> "Response":
        action = effect.end_turn(self_creature)
        if effect.turns() < 1:
            self._effects.remove(effect)
        return action
