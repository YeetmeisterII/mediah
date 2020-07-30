"""
Factory constants used in the creation of objects.
"""
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
    "goblin": {
        "constitution": 10, "physicality": 5, "dexterity": 10, "gold_worth": 5, "experience_worth": 10,
        "magic_enabled": False
    },
    "orc": {
        "constitution": 15, "physicality": 13, "dexterity": 13, "gold_worth": 10, "experience_worth": 15,
        "magic_enabled": False
    },
    "earth_elemental": {"constitution": 5, "physicality": 16, "dexterity": 16, "experience_worth": 30},
    "djinn": {
        "constitution": 10, "physicality": 5, "dexterity": 16, "social": 17, "gold_worth": 30, "experience_worth": 15
    },
    "dragon": {
        "constitution": 30, "physicality": 18, "dexterity": 18, "gold_worth": 100000000, "experience_worth": 500,
        "magic_enabled": False
    },
    "human": {"constitution": 10, "physicality": 10, "dexterity": 10, "social": 10, "magic_enabled": False},
}

WEAPONS = {
    "unarmed": weapons.Unarmed,
    "sword": weapons.Sword,
    "dagger": weapons.Dagger,
    "rock_fist": weapons.RockFist,
    "fire_breath": skills.FireBreath,
    "harsh_language": skills.HarshLanguage,
}

DEFAULT_CREATURE_WEAPONS = {
    "goblin": "dagger",
    "orc": "sword",
    "earth_elemental": "rock_fist",
    "djinn": "harsh_language",
    "dragon": "fire_breath",
    "human": "sword",
}

DEFAULT_WEAPON_STATS = {
    "unarmed": {"base_value": 0, "dice_quantity": 1, "dice_max": 1, "value": 0, "weight": 0},
    "sword": {"base_value": 0, "dice_quantity": 1, "dice_max": 6, "value": 5, "weight": 4},
    "dagger": {"base_value": 0, "dice_quantity": 1, "dice_max": 3, "value": 2, "weight": 1},
    "rock_fist": {"base_value": 3, "dice_quantity": 1, "dice_max": 8, "value": 0, "weight": 0},
    "fire_breath": {"base_value": 0, "dice_quantity": 2, "dice_max": 12},
    "harsh_language": {"base_value": 0, "dice_quantity": 1, "dice_max": 4},
}
