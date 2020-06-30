class Action:
    """
    Sent when a creature attempts to interact with the world.
    """

    def __init__(self, executor, target):
        self._executor = executor
        self._target = target

    def executor(self) -> "Creature":
        """
        :return: Creature performing the action.

        """
        return self._executor

    def target(self) -> object:
        """
        :return: Object being acted upon.
        """
        return self._target


class NullAction(Action):
    """
    Sent as placeholder action comparable to NoneType for actions.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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
        :return: Damage dealt to target should the attack land.
        """
        return self._damage

    def hit_index(self) -> int:
        """
        :return: A number between 1 and 20 inclusive that is used to calculate if an attack lands.
        """
        return self._hit_index


class HealingAction(Action):
    """
    Sent when a creature attempts to heal another object.
    """

    def __init__(self, executor, target, healing_quantity):
        super().__init__(executor, target)
        self._healing_quantity = healing_quantity

    def healing_quantity(self) -> int:
        """
        :return: How much to heal to heal the target by.
        """
        return self._healing_quantity


class BlockAction(Action):
    """
    Sent when a creature decides to initiate a defensive stance.
    """

    def __init__(self, executor, target):
        super().__init__(executor, target)
