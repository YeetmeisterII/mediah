from game_code.response import AttackResponse, NullResponse


class Action:
    """
    Sent when a creature attempts to interact with the world.
    """

    def __init__(self, executor: "Creature", target: "Creature", tool_used):
        self._executor = executor
        self._target = target
        self._tool_used = tool_used

    def __call__(self) -> NullResponse:
        return self.main()

    def main(self) -> NullResponse:
        """
        Calculate and perform the action.
        :return: A NullResponse object that has no information.
        """
        return NullResponse()

    def executor(self) -> "Creature":
        """
        :return: Creature performing the action.
        """
        return self._executor

    def target(self) -> "Creature":
        """
        :return: Object being acted upon.
        """
        return self._target

    def tool_used(self):
        return self._tool_used


class NullAction(Action):
    """
    Sent as placeholder action comparable to NoneType for actions.
    """


class AttackAction(Action):
    """
    Sent when a creature attempts an attack against another object.
    """

    def __init__(self, damage, hit_index, **kwargs):
        super().__init__(**kwargs)
        self._damage = damage
        self._hit_index = hit_index

    def main(self) -> AttackResponse:
        """
        Calculate the whether the attack hit and how much damage was dealt.
        :return: AttackResponse object with information what happen in text format.
        """
        attack_points = self._hit_index + self._executor.stats().physicality()
        target_dexterity = self._target.stats().dexterity()
        defense_points = 2 * target_dexterity if self._target.status().is_blocking() else target_dexterity

        if self._hit_index == 20:
            damage = self._damage
            outcome = "critical_hit"
        elif self._hit_index == 1:
            damage = 0
            outcome = "critical_miss"
        elif defense_points < attack_points:
            damage = self._damage
            outcome = "hit"
        else:
            damage = 0
            outcome = "miss"

        return AttackResponse(executor_name=self._executor.full_name(), target_name=self._target.full_name(),
                              tool_name=self._tool_used.name(), damage=damage, outcome=outcome)

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


# TODO: Implement healing response for healing actions.
class HealingAction(Action):
    """
    Sent when a creature attempts to heal another object.
    """

    def __init__(self, healing_quantity, **kwargs):
        super().__init__(**kwargs)
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

    def __init__(self, tool_used=None, **kwargs):
        super().__init__(tool_used=tool_used, **kwargs)
