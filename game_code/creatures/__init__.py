"""
The living entities of the game.
"""
from game_code.stats import Stats


class Creature:
    """
    Living entity that all other living creatures are based on.
    """
    _race = None

    def __init__(self, first_name: str, second_name: str, stats, status, weapon):
        self._first_name = first_name
        self._second_name = second_name
        self._stats = stats
        self._status = status
        self._weapon = weapon
        self._inventory = []

    def full_name(self) -> str:
        """
        :return: Full name of creature.
        """
        return f"{self._first_name} {self._second_name}" if self._second_name else self._first_name

    def first_name(self) -> str:
        """
        :return: First name of creature.
        """
        return self._first_name

    def second_name(self) -> str:
        """
        :return: Second name of creature.
        """
        return self._second_name

    def race(self) -> str:
        """
        :return: Race of creature.
        """
        return self._race

    def is_alive(self) -> bool:
        """
        :return: Whether the creature is alive.
        """
        return 0 < self._stats.health()

    def stats(self) -> Stats:
        """
        :return: Stats object of the creature.
        """
        return self._stats

    def status(self) -> "Status":
        """
        :return: Status object of the creature.
        """
        return self._status

    def weapon(self):
        """
        :return: Currently equipped weapon.
        """
        return self._weapon

    # TODO: Refactor the equip weapon  once an inventory object has been created.
    def equip_weapon(self, weapon) -> None:
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

    def _grab_weapon(self, weapon) -> None:
        """
        Set new weapon field.
        :param weapon: New current weapon.
        """
        self._weapon = weapon


class Goblin(Creature):
    """
    Goblin creature.
    """
    _race = "Goblin"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Orc(Creature):
    """
    Orc creature.
    """
    _race = "Orc"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EarthElemental(Creature):
    """
    Earth Elemental creature. They have a racial skill - Rock Fist.
    """
    _race = "Earth Elemental"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Djinn(Creature):
    """
    Djinn creature. They have a racial skill - Harsh Language.
    """
    _race = "Djinn"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Dragon(Creature):
    """
    Dragon creature. They have a racial skill - Fire Breath.
    """
    _race = "Dragon"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Human(Creature):
    """
    Human creature. Likely to be the player character.
    """
    _race = "Human"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
