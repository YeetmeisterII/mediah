""":str
Response classes used to inform the player the consequence of actions that creatures have taken.
"""
from typing import Tuple, Union


class Response:
    """
    Returned after calling an action.
    """

    def __init__(
            self, executor_name: str = None, target_name: str = None, tool_name: str = None, damage: int = None,
            outcome: str = None):
        self._executor_name = executor_name
        self._target_name = target_name
        self._tool_name = tool_name
        self._damage = damage
        self._outcome = outcome

    def __call__(self):
        return self._result()

    def _result(self) -> None:
        """
        Convert the information of an action's outcome into player readable strings detailing what happened and why.
        """
        pass

    # TODO: Move this method to a dedicated string editing class.
    def _to_possessive_noun(self, proper_noun: str) -> str:
        """
        Takes a name and turns it into the possessive form e.g. John Doe -> John Doe's.
        :param proper_noun: The name to convert.
        :return: Possessive version of input noun.
        """
        if not proper_noun:
            raise ValueError("Cannot be an empty string.")
        return f"{proper_noun}'" + ("s" * (proper_noun[-1] != "s"))


class NullResponse(Response):
    """
    Response used when the action has no outcome or does not need to be displayed.
    """

    def _result(self) -> tuple:
        """
        :return: Empty tuple.
        """
        return tuple()


class AttackResponse(Response):
    """
    The result of an attack action.
    """

    def __init__(self, executor_name: str, target_name: str, tool_name: str, damage: Union[str, int], outcome: str):
        super().__init__(
            executor_name=executor_name, target_name=target_name, tool_name=tool_name, damage=damage, outcome=outcome
        )

    def _result(self) -> Tuple[str, str, str]:
        """
        Create tuple containing three strings.
        In order they are they describe:
        1. Who attacked and with what tool.
        2. Whether the attack hit or missed.
        3. How much damage was dealt.
        :return: Tuple of strings detailing the outcome of the attack.
        """
        attempted_action = f"{self._executor_name} attacks {self._target_name} with {self._tool_name}."
        damage_dealt = f"{self._target_name} takes {self._damage} damage."

        executor_name_possessive = self._to_possessive_noun(self._executor_name)
        target_name_possessive = self._to_possessive_noun(self._target_name)

        potential_explanations = {
            "critical_hit": f"Critical Hit! {executor_name_possessive} attack bypasses {target_name_possessive} "
                            f"defences.",
            "hit": f"{executor_name_possessive} attack lands on {self._target_name}.",
            "miss": f"{executor_name_possessive} attack misses {self._target_name}.",
            "critical_miss": f"Critical miss. {executor_name_possessive} attack fails expeditiously.",
        }
        explanation = potential_explanations[self._outcome]
        return attempted_action, explanation, damage_dealt
