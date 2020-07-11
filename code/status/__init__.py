from code.status.effects import Blocking, Effect


class Status:
    def __init__(self):
        self._status_effects = []

    def __contains__(self, item):
        return item in map(type, self._status_effects)

    def is_blocking(self):
        return Blocking in self

    def add(self, effect: Effect):
        self._status_effects.append(effect)

    def end_turn(self):
        pass

    def _effect_end_turn(self, effect: Effect):
        return effect.end_turn()
