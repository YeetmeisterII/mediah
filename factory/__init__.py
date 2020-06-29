from mediah import creatures, skills, weapons

WEAPONS = {
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

CREATURES = {
    "goblin": creatures.Goblin,
    "orc": creatures.Orc,
    "earth_elemental": creatures.EarthElemental,
    "djinn": creatures.Djinn,
    "dragon": creatures.Dragon,
    "human": creatures.Human,
}

DEFAULT_STATS = {
    "goblin": {"constitution": 10, "physicality": 5, "dexterity": 10, "gold_worth": 5, "experience_worth": 10},
    "orc": {"constitution": 15, "physicality": 13, "dexterity": 13, "gold_worth": 10, "experience_worth": 15},
    "earth_elemental": {"constitution": 5, "physicality": 16, "dexterity": 16, "experience_worth": 30},
    "djinn": {"constitution": 10, "physicality": 5, "dexterity": 16, "social": 17, "gold_worth": 30,
              "experience_worth": 15},
    "dragon": {"constitution": 30, "physicality": 18, "dexterity": 18, "gold": 100000000, "experience": 500},
    "human": {"constitution": 10, "physicality": 10, "dexterity": 10, "social": 10},
}


class Factory:
    pass


class CreatureFactory(Factory):
    @staticmethod
    def create_creature(creature: str, stats: dict = None):
        stats = {} if stats is None else stats
        return CREATURES[creature](**stats)

    def create_default_creature(self, creature_cls: str):
        creature = self.create_creature(creature_cls, DEFAULT_STATS[creature_cls])
        weapon = WeaponFactory.create_weapon(DEFAULT_WEAPONS[creature_cls])
        self.equip_creature(creature, weapon)
        return creature

    def create_default_creature_without_weapon(self, creature: str):
        creature_instance = self.create_creature(creature, DEFAULT_STATS[creature])
        return creature_instance

    @staticmethod
    def equip_creature(creature: creatures.Creature, weapon: weapons.Weapon):
        return creature.equip_weapon(weapon)


class WeaponFactory(Factory):
    @staticmethod
    def create_weapon(weapon: str, stats: dict = None):
        stats = {} if stats is None else stats
        return WEAPONS[weapon](**stats)
