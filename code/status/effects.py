from code.actions import NullAction


class Effect:
    def __init__(self, turns=1):
        self._turns = turns

    def turns(self):
        return self._turns

    def end_turn(self):
        self._turns -= 1
        return NullAction()


class Blocking(Effect):
    pass
