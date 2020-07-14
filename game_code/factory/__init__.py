from typing import Dict

from game_code import creatures, weapons, skills

CREATURES = {
    "goblin": creatures.Goblin,
    "orc": creatures.Orc,
    "earth_elemental": creatures.EarthElemental,
    "djinn": creatures.Djinn,
    "dragon": creatures.Dragon,
    "human": creatures.Human,
}

DEFAULT_CREATURE_STATS = {
    "goblin": {"constitution": 10, "physicality": 5, "dexterity": 10, "gold_worth": 5, "experience_worth": 10},
    "orc": {"constitution": 15, "physicality": 13, "dexterity": 13, "gold_worth": 10, "experience_worth": 15},
    "earth_elemental": {"constitution": 5, "physicality": 16, "dexterity": 16, "experience_worth": 30},
    "djinn": {"constitution": 10, "physicality": 5, "dexterity": 16, "social": 17, "gold_worth": 30,
              "experience_worth": 15},
    "dragon": {"constitution": 30, "physicality": 18, "dexterity": 18, "gold_worth": 100000000,
               "experience_worth": 500},
    "human": {"constitution": 10, "physicality": 10, "dexterity": 10, "social": 10},
}

WEAPONS = {
    "unarmed": weapons.Unarmed,
    "sword": weapons.Sword,
    "dagger": weapons.Dagger,
    "rock_fist": weapons.RockFist,
    "fire_breath": skills.FireBreath,
    "harsh_language": skills.HarshLanguage,
}

DEFAULT_WEAPONS = {
    "goblin": "dagger",
    "orc": "sword",
    "earth_elemental": "rock_fist",
    "djinn": "harsh_language",
    "dragon": "fire_breath",
    "human": "sword",
}

DEFAULT_WEAPON_STATS = {
    "unarmed": {"name": "Fist", "base_value": 0, "dice_quantity": 1, "dice_max": 1},
    "sword": {"name": "Sword", "base_value": 0, "dice_quantity": 1, "dice_max": 6},
    "dagger": {"name": "Dagger", "base_value": 0, "dice_quantity": 1, "dice_max": 3},
    "rock_fist": {"name": "Rock Fist", "base_value": 3, "dice_quantity": 1, "dice_max": 8},
    "fire_breath": {"base_value": 0, "dice_quantity": 2, "dice_max": 12},
    "harsh_language": {"base_value": 0, "dice_quantity": 1, "dice_max": 4},
}


class Factory:
    def create_creature(self, creature_cls: str, stats: dict = None, first_name: str = None,
                        second_name: str = None) -> creatures.Creature:
        """
        Instantiate a creature, use default class specific values if no stats are passed.
        :param creature_cls: Class to instantiate.
        :param stats: Keyword values to be passed when instantiating.
        :param first_name: First name for the creature.
        :param second_name: Second name for the creature.
        :return: Instantiated creature.
        """
        stats = DEFAULT_CREATURE_STATS[creature_cls] if stats is None else stats
        return CREATURES[creature_cls](first_name=first_name, second_name=None, **stats)

    def create_creature_with_weapon(self, creature_cls: str, weapon_cls: str = None,
                                    creature_stats: Dict[str, int] = None,
                                    weapon_stats: Dict[str, int] = None,
                                    first_name: str = None,
                                    second_name: str = None) -> creatures.Creature:
        """
        Instantiate a creature with a weapon, use default class specific values for the creature and weapon if no stats
        to use are passed.
        :param creature_cls: Class of creature to instantiate.
        :param creature_stats: Keyword values to be passed when instantiating creature.
        :param weapon_cls: Class of weapon to give the creature.
        :param weapon_stats: Keyword values to be passed when instantiating the weapon.
        :param first_name: First name for the creature.
        :param second_name: Second name for the creature.
        :return: Instantiated creature with weapon equipped.
        """
        weapon_cls = DEFAULT_WEAPONS[creature_cls] if weapon_cls is None else weapon_cls
        creature = self.create_creature(creature_cls, creature_stats, first_name=first_name, second_name=None)
        weapon = self.create_weapon(weapon_cls, weapon_stats)
        self.equip_creature(creature, weapon)
        return creature

    def create_weapon(self, weapon_cls: str, stats: dict = None) -> weapons.Weapon:
        """
        Instantiate a weapon, use default class values if no stats are passed.
        :param weapon_cls: Class of weapon to instantiate.
        :param stats: Keyword values to be passed when instantiating.
        :return: Instantiated weapon.
        """
        stats = DEFAULT_WEAPON_STATS[weapon_cls] if stats is None else stats
        return WEAPONS[weapon_cls](**stats)

    def equip_creature(self, creature: "Creature", weapon: "Weapon") -> weapons.Weapon:
        """
        Equip creature with weapon.
        :param creature: Creature to equip.
        :param weapon: Weapon to be equipped.
        :return: Creature with weapon.
        """
        creature.equip_weapon(weapon)
        return creature
