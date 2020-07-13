from typing import List

from game_code.status.effects import Block, Effect


class Status:
    def __init__(self):
        self._effects = []

    def __contains__(self, effect_type):
        return effect_type in map(type, self._effects)

    def effects(self) -> List[Effect]:
        """
        :return: List of all current effects on creature.
        """
        return self._effects

    def is_blocking(self) -> bool:
        """
        :return: Whether the creature is currently blocking.
        """
        return Block in self

    def add_effect(self, effect: "Effect") -> None:
        """
        :param effect: Effect to apply to creature.
        """
        self._effects.append(effect)

    def remove_effect(self, effect: "Effect") -> None:
        """
        :param effect: Effect or remove from creature
        """
        self._effects.remove(effect)

    def end_turn(self, self_creature: "Creature") -> List["Response"]:
        """
        Get Response objects that are created at the end of a turn from all effects.
        :param self_creature: Creature the Status object is managing.
        :return: List of Response objects.
        """
        return [self._end_turn_effect(effect, self_creature) for effect in self._effects]

    def _end_turn_effect(self, effect: "Effect", self_creature: "Creature") -> "Response":
        """
        Performs the end turn method on an effect, then checks if the effect should be removed from the list of effects.
        :param effect: Effect to get response from.
        :param self_creature: Creature the Status object is managing.
        :return:
        """
        action = effect.end_turn(self_creature)
        if effect.turns() < 1:
            self._effects.remove(effect)
        return action
