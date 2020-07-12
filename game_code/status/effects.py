from game_code.actions import NullAction


class Effect:
    _name = "Effect"

    def __init__(self, turns=1):
        self._turns = turns

    def name(self):
        return self._name

    def turns(self):
        return self._turns

    def end_turn(self, effected_creature: "Creature") -> "Action":
        self._turns -= 1
        return NullAction(executor=self._name, target=effected_creature, tool_used=self)


class Block(Effect):
    _name = "Blocking"
