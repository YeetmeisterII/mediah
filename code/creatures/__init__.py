from code.stats import Stats


class Creature:
    """
    Living entity that all other living creatures are based on.
    """

    def __init__(self,
                 first_name: str = "Unnamed",
                 second_name: str = "",
                 race: str = "Unknown",
                 magic_base: int = 0,
                 constitution: int = 0,
                 physicality: int = 0,
                 dexterity: int = 0,
                 social: int = 0,
                 experience: int = 0,
                 weapon=None,
                 magic_enabled: bool = True,
                 gold_worth: int = 0,
                 experience_worth: int = 0):
        self._inventory = []
        self._first_name = first_name
        self._second_name = second_name
        self._race = race
        self._stats = Stats(constitution=constitution, physicality=physicality, dexterity=dexterity, social=social,
                            experience=experience, magic_enabled=magic_enabled, magic_base=magic_base)
        self._weapon = weapon
        self._gold_worth = gold_worth
        self._experience_worth = experience_worth

    def full_name(self):
        """
        :return: Full name of creature.
        """
        return f"{self._first_name} {self._second_name}" if self._second_name else self._first_name

    def first_name(self):
        """
        :return: First name of creature.
        """
        return self._first_name

    def second_name(self):
        """
        :return: Second name of creature.
        """
        return self._second_name

    def race(self):
        """
        :return: Race of creature.
        """
        return self._race

    def is_alive(self) -> bool:
        """
        :return: Whether the creature is alive.
        """
        return 0 < self._stats.health()

    def stats(self):
        return self._stats

    def weapon(self):
        """
        :return: Currently equipped weapon.
        """
        return self._weapon

    def gold_worth(self) -> int:
        """
        :return: Gold reward for killing a creature (is distinct from the gold that a creature has in their inventory).
        """
        return self._gold_worth

    def experience_worth(self) -> int:
        """
        :return: Experience reward for killing a creature (is distinct from the experience that a creature has
        accumulated).
        """
        return self._experience_worth

    # TODO: Refactor the equip weapon methods once an inventory object has been created.
    def equip_weapon(self, weapon: "Weapon") -> None:
        """
        Place the current weapon in the inventory and replace it with the weapon parameter.
        :param weapon: Weapon to equip.
        """
        self._store_weapon()
        self._grab_weapon(weapon)

    def _store_weapon(self) -> None:
        """
        Add current weapon to inventory, set weapon to None.
        """
        if self._weapon is not None:
            self._inventory.append(self._weapon)
        self._weapon = None

    def _grab_weapon(self, weapon: "Weapon") -> None:
        """
        Set new weapon field.
        :param weapon: New current weapon.
        """
        self._weapon = weapon

    # TODO: Figure out the logistics of how an attack will work and create Attack objects.
    def basic_attack(self):
        pass


class Goblin(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Goblin"


class Orc(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Orc"


class EarthElemental(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Earth Elemental"


class Djinn(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Djinn"


class Dragon(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Dragon"


class Human(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._race = "Human"
