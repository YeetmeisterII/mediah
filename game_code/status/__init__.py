"""
Library housing the logic of the Status class and Effect classes.
A creature's Status instance is used to manage the state of a creature, such as whether or not it is blocking.
The Effect classes are used to give a Status and by extension a creature status effects.
"""
from typing import List, Type

from game_code.creatures import Creature
from game_code.response import Response
from game_code.status.effects import Block, Effect


class Status:
    """
    Holds the status effects of a creature. Is used to obtain state information about a creature.
    """

    def __init__(self):
        self._effects = []

    def __contains__(self, effect_type: Type[Effect]) -> bool:
        """
        Check whether the creature is affected by an instance of a class of effect.
        :param effect_type: Class object of an effect.
        :return:
        """
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

    def add_effect(self, effect: Effect) -> None:
        """
        :param effect: Effect to apply to creature.
        """
        self._effects.append(effect)

    def remove_effect(self, effect: Effect) -> None:
        """
        :param effect: Effect or remove from creature
        """
        self._effects.remove(effect)

    def end_turn(self, parent_creature: Creature) -> List[Response]:
        """
        Get Response objects that are created at the end of a turn from all effects.
        :param parent_creature: Creature the Status object is managing.
        :return: List of Response objects.
        """
        return [self._end_turn_effect(effect, parent_creature) for effect in self._effects]

    def _end_turn_effect(self, effect: Effect, parent_creature: Creature) -> Response:
        """
        Performs the end turn method on an effect, then checks if the effect should be removed from the list of effects.
        :param effect: Effect to get response from.
        :param parent_creature: Creature the Status object is managing.
        :return:
        """
        action = effect.end_turn(parent_creature)
        if effect.turns() < 1:
            self._effects.remove(effect)
        return action
