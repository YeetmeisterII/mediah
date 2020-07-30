"""
Status effect classes.
"""
from game_code.actions import NullAction
from game_code.creatures import Creature


class Effect:
    """
    Base Effect class. Used to give creatures status effects.
    """
    _name = "Effect"

    def __init__(self, turns=1):
        self._turns = turns

    def name(self) -> str:
        """
        :return: Name of the effect.
        """
        return self._name

    def turns(self) -> int:
        """
        :return: How many more turns the effect will last.
        """
        return self._turns

    def end_turn(self) -> None:
        """
        :return: The action that needs to take place due to the effect.
        """
        pass


class Block(Effect):
    """
    Status effect for when a creature is currently blocking.
    """
    _name = "Blocking"

    def end_turn(self, parent_creature: Creature) -> NullAction:
        """
        :param parent_creature: Creature being effected by the status effect.
        :return: NullAction instance.
        """
        return NullAction()
