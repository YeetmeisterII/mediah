from typing import List, Union


class Response:
    """
    Sums up the result of an action.
    """

    def __init__(self, executor: "Creature", target: object, medium: Union[str, int, None],
                 outcome: Union[str, int, None], cause: Union[str, int, None]):
        self._executor = executor
        self._target = target
        self.medium = medium
        self._outcome = outcome
        self._cause = cause

    def result(self) -> List[str]:
        return []


class AttackResponse(Response):
    """
    The result of an attack action.
    """

    def __init__(self, executor: "Creature", target: object, outcome: int, cause: str):
        super().__init__(executor, target, None, outcome, cause)

    def result(self) -> List[str]:
        executor_name = self._executor.full_name()
        target_name = self._target.full_name()

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


class NullResponse(Response):
    def result(self) -> List[str]:
        return []
