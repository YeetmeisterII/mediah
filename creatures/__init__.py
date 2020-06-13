from typing import Dict


class Creature:
    # TODO: Figure out a better name for the mana base than just magic_stat.
    def __init__(self,
                 first_name: str = 'Unnamed',
                 second_name: str = '',
                 race: str = 'Unknown',
                 magic_stat: int = 0,
                 constitution: int = 0,
                 physicality: int = 0,
                 dexterity: int = 0,
                 social: int = 0,
                 experience: int = 0,
                 weapon=None,
                 magic_enabled: bool = True,
                 gold_worth: int = 0,
                 experience_worth: int = 0):
        self._first_name = first_name
        self._second_name = second_name
        self._race = race
        self._constitution = self._health = constitution
        self._magic_stat = self._mana = magic_stat
        self._social = self._charisma = social
        self._physicality_base = self._physicality = physicality
        self._dexterity_base = self._dexterity = dexterity
        self._experience = experience
        self._weapon = weapon
        self._magic_enabled = magic_enabled
        self._gold_worth = gold_worth
        self._experience_worth = experience_worth

    def info(self) -> Dict[str, str]:
        return {
            'name': f'{self._first_name} {self._second_name}',
            'first_name': self._first_name,
            'second_name': self._second_name,
            'race': self._race,
        }

    def is_alive(self) -> bool:
        return 0 < self._health

    def health(self) -> int:
        return self._health

    def increase_health(self, amount: int) -> int:
        add = (self._constitution - self._health) if self._constitution < (self._health + amount) else amount
        self._health += add

        return add

    def reduce_health(self, amount: int) -> int:
        self._health -= amount
        return amount

    def constitution(self) -> int:
        return self._constitution

    def increase_constitution(self, amount) -> int:
        self._constitution += amount
        return amount

    def reduce_constitution(self, amount) -> int:
        reduce = self._constitution if self._constitution < amount else amount
        self._constitution -= reduce

        if self._constitution < self._health:
            self._health = self._constitution

        return reduce

    def mana(self) -> int:
        return self._mana

    def increase_mana(self, amount: int) -> int:
        add = (self._magic_stat - self._mana) if self._magic_stat < (self._mana + amount) else amount
        self._mana += add

        return add

    def reduce_mana(self, amount: int) -> int:
        reduce = self._mana if self._mana < amount else amount
        self._mana -= reduce

        return reduce

    def magic_stat(self) -> int:
        return self._magic_stat

    def increase_magic_stat(self, amount: int) -> int:
        self._magic_stat += amount
        return amount

    def reduce_magic_stat(self, amount: int) -> int:
        reduce = self._magic_stat if self._magic_stat < amount else amount
        self._magic_stat -= reduce

        if self._magic_stat < self._mana:
            self._mana = self._magic_stat

        return reduce

    def charisma(self) -> int:
        return self._charisma

    def increase_charisma(self, amount: int) -> int:
        add = (self._social - self._charisma) if self._social < (self._charisma + amount) else amount
        self._charisma += add

        return add

    def reduce_charisma(self, amount: int) -> int:
        reduce = self._charisma if self._charisma < amount else amount
        self._charisma -= reduce

        return reduce

    def social(self) -> int:
        return self._social

    def increase_social(self, amount: int) -> int:
        self._social += amount
        return amount

    def reduce_social(self, amount: int) -> int:
        reduce = self._social if self._social < amount else amount
        self._social -= reduce

        if self._social < self._charisma:
            self._charisma = self._social

        return reduce

    def physicality(self) -> int:
        return self._physicality

    def increase_physicality(self, amount: int) -> int:
        add = (self._physicality_base - self._physicality) if self._physicality_base < (
                self._physicality + amount) else amount
        self._physicality += add

        return add

    def reduce_physicality(self, amount: int) -> int:
        reduce = self._physicality if self._physicality < amount else amount
        self._physicality -= reduce

        return reduce

    def physicality_base(self) -> int:
        return self._physicality_base

    def increase_physicality_base(self, amount: int) -> int:
        self._physicality_base += amount
        return amount

    def reduce_physicality_base(self, amount: int) -> int:
        reduce = self._physicality_base if self._physicality_base < amount else amount
        self._physicality_base -= reduce

        if self._physicality_base < self._physicality:
            self._physicality = self._physicality_base

        return reduce

    def dexterity(self) -> int:
        return self._dexterity

    def increase_dexterity(self, amount: int) -> int:
        add = (self._dexterity_base - self._dexterity) if self._dexterity_base < (
                self._dexterity + amount) else amount
        self._dexterity += add

        return add

    def reduce_dexterity(self, amount: int) -> int:
        reduce = self._dexterity if self._dexterity < amount else amount
        self._dexterity -= reduce

        return reduce

    def dexterity_base(self) -> int:
        return self._dexterity_base

    def increase_dexterity_base(self, amount: int) -> int:
        self._dexterity_base += amount
        return amount

    def reduce_dexterity_base(self, amount: int) -> int:
        reduce = self._dexterity_base if self._dexterity_base < amount else amount
        self._dexterity_base -= reduce

        if self._dexterity_base < self._dexterity:
            self._dexterity = self._dexterity_base

        return reduce

    def experience(self) -> int:
        return self._experience

    def increase_experience(self, amount: int) -> int:
        self._experience += amount
        return amount

    def weapon(self):
        return self._weapon

    def gold_worth(self) -> int:
        return self._gold_worth

    def experience_worth(self) -> int:
        return self._experience_worth

    # TODO complete store_weapon method once inventory has been created.
    def _store_weapon(self):
        pass


# TODO: Add default weapons to the subclasses of Creature once weapons are added in
class Goblin(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 10,
            'physicality': 5,
            'dexterity': 10,
            'weapon': None,
            'gold_worth': 5,
            'experience_worth': 10,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Goblin'}
        super().__init__(**kwargs)


class Orc(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 15,
            'physicality': 13,
            'dexterity': 13,
            'weapon': None,
            'gold_worth': 10,
            'experience_worth': 15,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Orc'}
        super().__init__(**kwargs)


class EarthElemental(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 5,
            'physicality': 16,
            'dexterity': 16,
            'weapon': None,
            'experience_worth': 30,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Earth Elemental'}
        super().__init__(**kwargs)


class Djinn(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 10,
            'physicality': 5,
            'dexterity': 16,
            'social': 17,
            'weapon': None,
            'gold_worth': 30,
            'experience_worth': 15,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Djinn'}
        super().__init__()


class Dragon(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 30,
            'physicality': 18,
            'dexterity': 18,
            'gold': 100000000,
            'experience': 500,
            'weapon': None,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Dragon'}
        super().__init__(**kwargs)


class Human(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 10,
            'physicality': 10,
            'dexterity': 10,
            'social': 10,
            'weapon': None,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Human'}
        super().__init__(**kwargs)
