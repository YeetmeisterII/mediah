class Action:
    def __init__(self, executor, target):
        self._executor = executor
        self._target = target

    def executor(self) -> 'Creature':
        return self._executor

    def target(self) -> object:
        return self._target


class AttackAction(Action):
    def __init__(self, executor, target, damage, hit_index):
        super().__init__(executor, target)
        self._damage = damage
        self._hit_index = hit_index

    def damage(self) -> int:
        return self._damage

    def hit_index(self) -> int:
        return self._hit_index


class HealAction(Action):
    def __init__(self, executor, target, heal_quantity):
        super().__init__(executor, target)
        self._heal_quantity = heal_quantity

    def heal_quantity(self) -> int:
        return self._heal_quantity


class BlockAction(Action):
    def __init__(self, executor, target):
        super().__init__(executor, target)
