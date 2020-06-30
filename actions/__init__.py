class Action:
    """
    Sent when a creature attempts to interact with the world.
    """
    def __init__(self, executor, target):
        self._executor = executor
        self._target = target

    def executor(self) -> "Creature":
        return self._executor

    def target(self) -> object:
        return self._target


class AttackAction(Action):
    """
    Sent when a creature attempts an attack against another object.
    """
    def __init__(self, executor, target, damage, hit_index):
        super().__init__(executor, target)
        self._damage = damage
        self._hit_index = hit_index

    def damage(self) -> int:
        """
        Damage dealt to target should the attack land.
        :return: Int
        """
        return self._damage

    def hit_index(self) -> int:
        """
        A number between 1 and 20 inclusive that is used to calculate if an attack lands.
        :return: Int
        """
        return self._hit_index


class HealAction(Action):
    """
    Sent when a creature attempts to heal another object.
    """
    def __init__(self, executor, target, heal_quantity):
        super().__init__(executor, target)
        self._heal_quantity = heal_quantity

    def heal_quantity(self) -> int:
        """
        How much to heal to heal the target by.
        :return: Int
        """
        return self._heal_quantity


class BlockAction(Action):
    """
    Sent when a creature decides to initiate a defensive stance.
    """
    def __init__(self, executor, target):
        super().__init__(executor, target)
