"""
Library contains the data used to dynamically create game objects.
"""
from typing import Dict, Union

from game_code import creatures, weapons
from game_code.stats import Stats
from game_code.status import Status
from . import constants as const


class Factory:
    """
    Dynamic creation of game objects such as Creatures and Weapons.
    """

    def create_status(self):
        """
        :return: Status instance. 
        """
        return Status()

    def create_stats_instance(self, creature_class: str, stat_values: Dict[str, Union[int, bool]] = None):
        """
        Create a Stats instance.
        :param creature_class: Race of the creature the Stats instance will be used in.
        :param stat_values: Optional stat values. If stat_values are not passed or are None then default values for the
        Creature's race will be used.
        :return: Stats instance.
        """
        if stat_values is None:
            stat_values = const.DEFAULT_CREATURE_STATS[creature_class]
        return Stats(**stat_values)

    def create_weapon(self, weapon_class: str, name: str = None, stat_values: Dict[str, int] = None) -> weapons.Weapon:
        """
        Create a Weapon instance.
        :param weapon_class: Type of weapon to create. Example: 'sword'
        :param name: Optional name of the weapon.
        :param stat_values: Optional weapon stats. If stat_values are not passed or is None then default values for the
        weapon type will be used.
        :return: Weapon instance.
        """
        weapon_type = const.WEAPONS[weapon_class]
        if stat_values is None:
            stat_values = const.DEFAULT_WEAPON_STATS[weapon_class]

        if name is None:
            weapon = weapon_type(**stat_values)
        else:
            weapon = weapon_type(name=name, **stat_values)
        return weapon

    def create_creature(
            self, creature_class: str, first_name: str, second_name: str,
            stat_values: Dict[str, Union[int, bool]] = None) -> creatures.Creature:
        """
        Create an unarmed creature.
        :param creature_class: Race of the creature being created.
        :param first_name: First name of the creature being created.
        :param second_name: Second name of the creature being created.
        :param stat_values: Optional stat values for the creature. If stat_values are not passed or is None then
        default stat values for the race will be used.
        :return: Creature Instance.
        """
        stats = self.create_stats_instance(creature_class, stat_values)
        status = self.create_status()
        creature_type = const.CREATURES[creature_class]
        weapon = self.create_weapon(weapon_class="unarmed")
        return creature_type(first_name=first_name, second_name=second_name, stats=stats, status=status, weapon=weapon)

    def create_creature_with_weapon(
            self, creature_class: str, first_name: str, second_name: str, creature_stat_values: dict = None,
            weapon_class: str = None, weapon_stat_values: Dict[str, Union[int, bool]] = None) -> creatures.Creature:
        """
        Create a Creature instance with a weapon.
        :param creature_class: Race of the creature being created.
        :param first_name: First name of the creature being created.
        :param second_name: Second name of the creature being created.
        :param creature_stat_values: Optional stat values for the creature. If not passed default values for the race
        will be used.
        :param weapon_class: Optional type of weapon to create. If not passed default weapon for the race will be 
        created.
        :param weapon_stat_values: Optional weapon stats. If not passed default stats for the weapon type will be used.
        :return: Creature instance.
        """
        if weapon_class is None:
            weapon_class = const.DEFAULT_CREATURE_WEAPONS[creature_class]
        if weapon_stat_values is None:
            weapon_stat_values = const.DEFAULT_WEAPON_STATS[weapon_class]

        stats = self.create_stats_instance(creature_class, creature_stat_values)
        status = self.create_status()

        weapon = self.create_weapon(weapon_class, weapon_stat_values)
        creature_type = const.CREATURES[creature_class]
        creature = creature_type(
            first_name=first_name, second_name=second_name, stats=stats, status=status, weapon=weapon
        )
        creature.equip_weapon(weapon)
        return creature
