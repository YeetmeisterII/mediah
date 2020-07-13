from typing import List, Union, Tuple


class Response:
    """
    Sums up the result of an action.
    """

    def __init__(self, executor_name: str = None, target_name: str = None):
        self._executor = executor_name
        self._target = target_name

    def _convert_to_possessive_noun(self, proper_noun: str) -> str:
        """
        Takes a name and turns it into the possessive form e.g. John Doe -> John Doe's.
        :param proper_noun: The name to convert.
        :return: Possessive version of input noun.
        """
        if not proper_noun:
            raise ValueError("Cannot be an empty string.")
        return f"{proper_noun}'" if proper_noun[-1] == "s" else f"{proper_noun}'s"

    def result(self) -> List[str]:
        return []


class NullResponse(Response):
    """
    Response object used when an action has no outcome.
    """
    pass


class AttackResponse(Response):
    """
    The result of an attack action.
    """

    def __init__(self, executor_name: str, target_name: str, tool_name: str, damage: Union[str, int], outcome: str):
        super().__init__(executor_name=executor_name, target_name=target_name)
        self._result = self._create_result(executor_name=executor_name, target_name=target_name,
                                           tool_name=tool_name, damage=damage, outcome=outcome)

    def __call__(self, *args, **kwargs):
        return self._result

    def result(self) -> Tuple[str, str, str]:
        """
        :return: Tuple containing strings describing the result of an action.
        """
        return self._result

    def _create_result(self, executor_name: str, target_name: str, tool_name: str, damage: int,
                       outcome: str) -> Tuple[str, str, str]:
        """
        Create a tuple containing strings that describe the result of an action.
        :param executor_name: Name of object performing attack.
        :param target_name: Name of object attack was aimed at.
        :param tool_name: Name of item (may not be physical) that was used in performing the attack.
        :param damage: Damage dealt from the attack.
        :param outcome: Whether the attack was a critical hit, hit, miss or a critical miss.
        :return: Tuple of the result for user reading.
        """
        executor_name_possessive = self._convert_to_possessive_noun(executor_name)
        target_name_possessive = self._convert_to_possessive_noun(target_name)
        outcomes = {
            "critical_hit": f"Critical Hit! {executor_name_possessive} attack bypasses {target_name_possessive} "
                            f"defences.",
            "hit": f"{executor_name_possessive} attack lands on {target_name}.",
            "miss": f"{executor_name_possessive} attack misses {target_name}.",
            "critical_miss": f"Critical miss. {executor_name_possessive} attack fails expeditiously.",
        }

        return (f"{executor_name} attacks {target_name} with {tool_name}.", outcomes[outcome],
                f"{target_name} takes {damage} damage.")
