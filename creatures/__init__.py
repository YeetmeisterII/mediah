from typing import Dict

from mediah import weapons, skills


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
                 weapon=weapons.Unarmed(),
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
        """
        Increases the health up to the health cap equal to constitution.
        :param amount: How much health can be added.
        :return: How much health was actually added.
        """
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
        """
        Reduces constitution down to a minimum of 0. If constitution drops below current health then reduce current
        health to match it.
        :param amount: How much constitution can be reduced by.
        :return: How much constitution was actually reduced by.
        """
        reduce = self._constitution if self._constitution < amount else amount
        self._constitution -= reduce

        if self._constitution < self._health:
            self._health = self._constitution

        return reduce

    def mana(self) -> int:
        return self._mana

    def increase_mana(self, amount: int) -> int:
        """
        Increases the mana up to the mana cap equal to magic stat.
        :param amount: How much mana can be added.
        :return: How much mana was actually added.
        """
        add = (self._magic_stat - self._mana) if self._magic_stat < (self._mana + amount) else amount
        self._mana += add

        return add

    def reduce_mana(self, amount: int) -> int:
        """
        Reduces mana down to a minimum of 0.
        :param amount: How much mana can be reduced by.
        :return: How much mana was actually reduced by.
        """
        reduce = self._mana if self._mana < amount else amount
        self._mana -= reduce

        return reduce

    def magic_stat(self) -> int:
        return self._magic_stat

    def increase_magic_stat(self, amount: int) -> int:
        self._magic_stat += amount
        return amount

    def reduce_magic_stat(self, amount: int) -> int:
        """
        Reduces magic stat down to a minimum of 0. If magic stat drops below current mana then reduce current
        mana to match it.
        :param amount: How much magic stat can be reduced by.
        :return: How much magic stat was actually reduced by.
        """
        reduce = self._magic_stat if self._magic_stat < amount else amount
        self._magic_stat -= reduce

        if self._magic_stat < self._mana:
            self._mana = self._magic_stat

        return reduce

    def charisma(self) -> int:
        return self._charisma

    def increase_charisma(self, amount: int) -> int:
        """
        Increases the charisma up to the cap equal to social.
        :param amount: How much charisma can be added.
        :return: How much charisma was actually added.
        """
        add = (self._social - self._charisma) if self._social < (self._charisma + amount) else amount
        self._charisma += add

        return add

    def reduce_charisma(self, amount: int) -> int:
        """
        Reduces charisma down to a minimum of 0.
        :param amount: How much charisma can be reduced by.
        :return: How much charisma was actually reduced by.
        """
        reduce = self._charisma if self._charisma < amount else amount
        self._charisma -= reduce

        return reduce

    def social(self) -> int:
        return self._social

    def increase_social(self, amount: int) -> int:
        self._social += amount
        return amount

    def reduce_social(self, amount: int) -> int:
        """
        Reduces social down to a minimum of 0. If social drops below current charisma then reduce current charisma
        to match it.
        :param amount: How much social can be reduced by.
        :return: How much social was actually reduced by.
        """
        reduce = self._social if self._social < amount else amount
        self._social -= reduce

        if self._social < self._charisma:
            self._charisma = self._social

        return reduce

    def physicality(self) -> int:
        return self._physicality

    def increase_physicality(self, amount: int) -> int:
        """
        Increases the physicality up to the cap equal to physicality_base.
        :param amount: How much physicality can be added.
        :return: How much physicality was actually added.
        """
        add = (self._physicality_base - self._physicality) if self._physicality_base < (
                self._physicality + amount) else amount
        self._physicality += add

        return add

    def reduce_physicality(self, amount: int) -> int:
        """
        Reduces physicality down to a minimum of 0.
        :param amount: How much physicality can be reduced by.
        :return: How much physicality was actually reduced by.
        """
        reduce = self._physicality if self._physicality < amount else amount
        self._physicality -= reduce

        return reduce

    def physicality_base(self) -> int:
        return self._physicality_base

    def increase_physicality_base(self, amount: int) -> int:
        self._physicality_base += amount
        return amount

    def reduce_physicality_base(self, amount: int) -> int:
        """
        Reduces physicality_base down to a minimum of 0. If physicality_base drops below current physicality then
        reduce current physicality to match it.
        :param amount: How much physicality_base can be reduced by.
        :return: How much physicality_base was actually reduced by.
        """
        reduce = self._physicality_base if self._physicality_base < amount else amount
        self._physicality_base -= reduce

        if self._physicality_base < self._physicality:
            self._physicality = self._physicality_base

        return reduce

    def dexterity(self) -> int:
        return self._dexterity

    def increase_dexterity(self, amount: int) -> int:
        """
        Increases the dexterity up to the cap equal to dexterity_base.
        :param amount: How much dexterity can be added.
        :return: How much dexterity was actually added.
        """
        add = (self._dexterity_base - self._dexterity) if self._dexterity_base < (
                self._dexterity + amount) else amount
        self._dexterity += add

        return add

    def reduce_dexterity(self, amount: int) -> int:
        """
        Reduces dexterity down to a minimum of 0.
        :param amount: How much dexterity can be reduced by.
        :return: How much dexterity was actually reduced by.
        """
        reduce = self._dexterity if self._dexterity < amount else amount
        self._dexterity -= reduce

        return reduce

    def dexterity_base(self) -> int:
        return self._dexterity_base

    def increase_dexterity_base(self, amount: int) -> int:
        self._dexterity_base += amount
        return amount

    def reduce_dexterity_base(self, amount: int) -> int:
        """
        Reduces dexterity_base down to a minimum of 0. If dexterity_base drops below current dexterity then reduce
        current dexterity to match it.
        :param amount: How much dexterity_base can be reduced by.
        :return: How much dexterity_base was actually reduced by.
        """
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

    # TODO: Complete store_weapon method once inventory has been created.
    def _store_weapon(self):
        pass

    # TODO: Figure out the logistics of how an attack will work and create Attack objects.
    def attack(self, action):
        pass


class Goblin(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 10,
            'physicality': 5,
            'dexterity': 10,
            'weapon': weapons.Dagger(),
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
            'weapon': weapons.Sword(),
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
            'weapon': weapons.RockFist(),
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
            # TODO: Create the ability for creatures to have skills and stop using them as if they're weapons
            'weapon': skills.HarshLanguage(),
            'gold_worth': 30,
            'experience_worth': 15,
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Djinn'}
        super().__init__(**kwargs)


class Dragon(Creature):
    def __init__(self, **kwargs):
        default_values = {
            'constitution': 30,
            'physicality': 18,
            'dexterity': 18,
            # TODO: Create the ability for creatures to have skills and stop using them as if they're weapons
            'weapon': skills.FireBreath(),
            'gold': 100000000,
            'experience': 500,
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
            'weapon': weapons.Sword(),
        }
        # Doing this will mean kwargs uses the default values but will override them if specified.
        kwargs = {**default_values, **kwargs, 'race': 'Human'}
        super().__init__(**kwargs)
