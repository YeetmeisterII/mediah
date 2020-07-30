"""
Library contains Action classes used for creatures to affect the world.
"""
from game_code.creatures import Creature
from game_code.response import NullResponse, AttackResponse


class Action:
    """
    Base Action class. When a Creature instance wants to affect the world in some way they will use an action instance.
    It calculates the outcome of their action and carries out changes caused by the action.
    """

    def __init__(
            self, executor: Creature = None, target: Creature = None, tool_used=None, damage: int = None,
            hit_index: int = None, healing_quantity: int = None):
        self._executor = executor
        self._target = target
        self._tool_used = tool_used
        self._damage = damage
        self._hit_index = hit_index
        self._healing_quantity = healing_quantity

    def __call__(self):
        return self.main()

    def main(self) -> None:
        """
        Logic to calculate the outcome of an action and performs it.
        Example: Figure out if an attack landed and deduct the relevant health from the target of the attack.
        """
        pass

    def executor(self) -> Creature:
        """
        :return: Creature performing the action.
        """
        return self._executor

    def target(self) -> Creature:
        """
        :return: Creature targeted by the action.
        """
        return self._target

    def tool_used(self):
        """
        :return: Weapon, Skill, Item or other that was used as a medium for the action.
        """
        return self._tool_used

    def damage(self) -> int:
        """
        :return: Potential damage dealt to deal to target.
        """
        return self._damage

    def hit_index(self) -> int:
        """
        :return: Number between 1 and 20 inclusive used to calculate if an attack lands.
        """
        return self._hit_index

    def healing_quantity(self) -> int:
        """
        :return: Potential quantity to heal target by.
        """
        return self._healing_quantity


class NullAction(Action):
    """
    Action used when no action is taken.
    """

    def __init__(self):
        super().__init__()

    def main(self) -> NullResponse:
        """
        :return: NullResponse instance with no data.
        """
        return NullResponse()


class AttackAction(Action):
    """
    Action used when a Creature attacks a Creature.
    """

    def __init__(self, executor: Creature, target: Creature, hit_index: int, damage: int, tool_used):
        super().__init__(executor=executor, target=target, hit_index=hit_index, damage=damage, tool_used=tool_used)

    def main(self) -> AttackResponse:
        # TODO: Implement reduction of target health if attack lands.
        """
        Calculate the whether the attack hit and how much damage was dealt.
        :return: AttackResponse object with information what happen in text format.
        """
        attack_points = self._hit_index + self._executor.stats().physicality()
        target_dexterity = self._target.stats().dexterity()
        defense_points = (self._target.status().is_blocking() + 1) * target_dexterity

        if self._hit_index == 20:
            outcome = "critical_hit"
            damage = self._damage
        elif self._hit_index == 1:
            outcome = "critical_miss"
            damage = 0
        elif defense_points < attack_points:
            outcome = "hit"
            damage = self._damage
        else:
            outcome = "miss"
            damage = 0

        return AttackResponse(
            executor_name=self._executor.full_name(), target_name=self._target.full_name(),
            tool_name=self._tool_used.name(), damage=damage, outcome=outcome
        )


# TODO: Implement healing response for healing actions.
class HealingAction(Action):
    """
    Action used when a Creature attempts to heal a creature.
    """

    def __init__(self, executor: Creature, target: Creature, healing_quantity: int, tool_used):
        super().__init__(executor=executor, target=target, healing_quantity=healing_quantity, tool_used=tool_used)

    def main(self) -> None:
        # TODO: Implement method
        pass


class BlockAction(Action):
    """
    Action used when a Creature attempts to block on their turn.
    """

    def __init__(self, executor: Creature):
        super().__init__(executor=executor, target=executor)

    def main(self) -> None:
        # TODO: Implement method
        pass
