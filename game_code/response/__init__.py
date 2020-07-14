from typing import Union, Tuple

from lazy import lazy


class Response:
    """
    Sums up the result of an action.
    """

    def __init__(self, executor_name: str = None, target_name: str = None):
        self._executor_name = executor_name
        self._target_name = target_name

    def __call__(self, *args, **kwargs) -> Tuple[str, ...]:
        return self.result()

    def result(self) -> tuple:
        """
        :return: Tuple containing strings describing the result of an action.
        """
        return ()

    def _convert_to_possessive_noun(self, proper_noun: str) -> str:
        """
        Takes a name and turns it into the possessive form e.g. John Doe -> John Doe's.
        :param proper_noun: The name to convert.
        :return: Possessive version of input noun.
        """
        if not proper_noun:
            raise ValueError("Cannot be an empty string.")
        return f"{proper_noun}'" if proper_noun[-1] == "s" else f"{proper_noun}'s"


class NullResponse(Response):
    """
    Response object used when an action has no outcome.
    """
    pass


class AttackResponse(Response):
    """
    The result of an attack action.
    """

    def __init__(self, tool_name: str, damage: Union[str, int], outcome: str, **kwargs):
        super().__init__(**kwargs)
        self._tool_name = tool_name
        self._damage = damage
        self._outcome = outcome

    def result(self) -> Tuple[str, str, str]:
        """
        :return: Tuple containing strings describing the result of an action.
        """
        return self.__create_result

    @lazy
    def __create_result(self) -> Tuple[str, str, str]:
        """
        Create a tuple containing strings that describe the result of an action.
        :return: Tuple of the result for user reading.
        """
        executor_name_possessive = self._convert_to_possessive_noun(self._executor_name)
        target_name_possessive = self._convert_to_possessive_noun(self._target_name)
        outcomes = {
            "critical_hit": f"Critical Hit! {executor_name_possessive} attack bypasses {target_name_possessive} "
                            f"defences.",
            "hit": f"{executor_name_possessive} attack lands on {self._target_name}.",
            "miss": f"{executor_name_possessive} attack misses {self._target_name}.",
            "critical_miss": f"Critical miss. {executor_name_possessive} attack fails expeditiously.",
        }

        return (f"{self._executor_name} attacks {self._target_name} with {self._tool_name}.", outcomes[self._outcome],
                f"{self._target_name} takes {self._damage} damage.")


class BlockResponse(Response):
    """
    The result of an block action.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def result(self) -> Tuple[str]:
        """
        :return: Tuple containing strings describing the result of an action.
        """
        return self.__create_result

    @lazy
    def __create_result(self) -> Tuple[str]:
        """
        Create a tuple containing strings that describe the result of an action.
        :return: Tuple of the result for user reading.
        """
        return f"{self._executor_name} takes a defensive stance.",
