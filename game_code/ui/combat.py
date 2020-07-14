from typing import Union, List, Tuple

from game_code.ui import UserInterface


class CombatUserInterface(UserInterface):

    def __init__(self, enemy: "Creature", **kwargs):
        super().__init__(**kwargs)
        self._enemy = enemy

    def encounter_start(self) -> None:
        """
        Message telling the player what creature they are entering an encounter with.
        """
        print(f"You have encountered {self._enemy.full_name()}, {self._prefix_a_or_an(self._enemy.race())}.\n")

    def start_turn(self):
        for creature in (self._player, self._enemy):
            output = [
                creature.full_name(),
                f"Health: {creature.stats().health()} / {creature.stats().constitution()}",
                f"Weapon: {creature.weapon().name()}"
            ]
            print("\n".join(output) + "\n")

    def end_turn(self):
        self._separator()

    def ask_player_for_action(self) -> str:
        while True:
            print(f"1. Attack with {self._player.weapon().name()}.\n"
                  f"2. Attempt to block.\n")
            choice = self._input_int(input_range=(1, 3))
            return ["attack", "block"][choice - 1]

    def _response_results(self, responses: Union[List["Response"], Tuple["Response", ...]]) -> Union[
        List["Response"], Tuple["Response", ...]]:
        return tuple()
