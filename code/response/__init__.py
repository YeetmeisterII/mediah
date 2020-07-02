from typing import List, Union


class Response:
    """
    Sums up the result of an action.
    """

    def __init__(self, executor: "Creature", target: object, reason: Union[str, int, None],
                 outcome: Union[str, int, None], cause: Union[str, int, None]):
        self._executor = executor
        self._target = target
        self._reason = reason
        self._outcome = outcome
        self._cause = cause

    def result(self) -> List[str]:
        return [f"{self._reason}. {self._outcome} because {self._cause}."]


class AttackResponse(Response):
    """
    The result of an attack action.
    """

    def __init__(self, executor: "Creature", target: object, outcome: int, cause: str):
        super().__init__(executor, target, None, outcome, cause)

    def result(self) -> List[str]:
        executor_name = self._executor.name() if self._executor.second_name() else self._executor.first_name()
        target_name = self._target.name() if self._target.second_name() else self._target.first_name()

        causes = {
            "critical_hit": "Critical Hit! Attack bypasses defence.",
            "hit": f"{executor_name} lands attack on {target_name}.",
            "miss": f"{executor_name} misses attack on {target_name}.",
            "critical_miss": f"Critical miss. Attack on {target_name} fails expeditiously.",
        }

        reason = f"{executor_name} attacks {target_name}."
        cause = causes[self._cause]
        outcome = f"{target_name} takes {self._outcome} damage."
        return [reason, cause, outcome]
