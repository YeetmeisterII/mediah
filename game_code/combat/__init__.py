import time
from typing import Tuple, List, Union

from game_code.ui import combat


class CombatEncounter:
    def __init__(self, player: "Creature", enemy: "Creature"):
        self._player = player
        self._enemy = enemy
        self._ui = combat.CombatUserInterface(player=player, enemy=enemy)

    def __call__(self, *args, **kwargs):
        return self.main()

    def main(self):
        self._ui.encounter_start()

        while self._player.is_alive() and self._enemy.is_alive():
            self._ui.start_turn()

            creature_actions = (self._player_action(), self._enemy_action())
            creature_responses = self._perform_actions(creature_actions)
            time.sleep(0.5)
            self._ui.output_responses(creature_responses)

            effect_actions = self._status_actions()
            effect_responses = self._perform_actions(effect_actions)
            self._ui.output_responses(effect_responses)

            self._ui.end_turn()

    def _player_action(self) -> "Action":
        """

        :return:
        """
        player_choice = self._ui.ask_player_for_action()
        choices = {"attack": self._player_attack,
                   "block": self._player_block}
        return choices[player_choice]()

    # TODO: Temporary logic within this method to allow for the process as a whole to be tested.
    def _enemy_action(self) -> "Action":
        """
        :return: Generate computer controlled creature's next action.
        """
        return self._enemy.attack(self._player)

    def _player_attack(self) -> "AttackAction":
        """
        :return: AttackAction instance aimed at the player enemy.
        """
        return self._player.attack(target=self._enemy)

    def _player_block(self) -> "BlockAction":
        """
        :return: BlockAction instance allowing the player to block.
        """
        return self._player.block()

    def _perform_actions(self, actions: Union[List["Action"], Tuple["Action", ...]]) -> Tuple["Response", ...]:
        """
        Order Actions based on priority. Then execute all Action instances in order an receive a Response object for
        each one.
        :param actions: Action instances to execute.
        :return: Response instances to give information on the outcome of the Actions.
        """
        sorted_actions = sorted(actions, key=lambda action: action.priority())
        return tuple([action() for action in sorted_actions])

    def _status_actions(self) -> Tuple[List["Response"], List["Response"]]:
        """
        :return: Tuple of Response instances detailing the how each creature has been affect by the effects in their
        status at the end of a turn.
        """
        return *self._player.end_combat_turn(), *self._enemy.end_combat_turn()
