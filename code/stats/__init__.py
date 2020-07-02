class Stats:
    def __init__(self,
                 constitution: int = 0,
                 physicality: int = 0,
                 dexterity: int = 0,
                 social: int = 0,
                 experience: int = 0,
                 magic_base: int = 0,
                 magic_enabled: bool = True):
        self._constitution = self._health = constitution
        self._magic_base = self._mana = magic_base
        self._social = self._charisma = social
        self._physicality_base = self._physicality = physicality
        self._dexterity_base = self._dexterity = dexterity
        self._magic_enabled = magic_enabled
        self._experience = experience

    def magic_enabled(self):
        """
        :return: Whether the creature can cast magic spells.
        """
        return self._magic_enabled

    def health(self) -> int:
        """
        :return: Creature health.
        """
        return self._health

    def increase_health(self, amount: int) -> int:
        """
        Increases health to less than or equal constitution.
        :param amount: Quantity to increase health by.
        :return: Increase in health.
        """
        add = (self._constitution - self._health) if self._constitution < (self._health + amount) else amount
        self._health += add
        return add

    def reduce_health(self, amount: int) -> int:
        """
        Subtracts health.
        :param amount: Quantity to be subtracted from health.
        :return: Decrease in health.
        """
        self._health -= amount
        return amount

    def constitution(self) -> int:
        """
        :return: Creature constitution which is the base for health.
        """
        return self._constitution

    def increase_constitution(self, amount) -> int:
        """
        Increases the constitution of the creature.
        :param amount: Quantity to increase constitution by.
        :return: Increase in constitution.
        """
        self._constitution += amount
        return amount

    def reduce_constitution(self, amount) -> int:
        """
        Reduces constitution to a minimum of 0.
        Also reduces current health to equal constitution if constitution becomes less than current health.
        :param amount: Quantity to reduce constitution by.
        :return: Decrease in constitution.
        """
        reduce = self._constitution if self._constitution < amount else amount
        self._constitution -= reduce

        if self._constitution < self._health:
            self._health = self._constitution
        return reduce

    def mana(self) -> int:
        """
        :return: Creature mana.
        """
        return self._mana

    def increase_mana(self, amount: int) -> int:
        """
        Increases current mana to less than or equal magic_base.
        :param amount: Quantity to increase mana by.
        :return: Increase in mana.
        """
        add = (self._magic_base - self._mana) if self._magic_base < (self._mana + amount) else amount
        self._mana += add
        return add

    def reduce_mana(self, amount: int) -> int:
        """
        Reduces current mana to a minimum of 0.
        :param amount: Quantity to reduce mana by.
        :return: Decrease in mana.
        """
        reduce = self._mana if self._mana < amount else amount
        self._mana -= reduce
        return reduce

    def magic_base(self) -> int:
        """
        :return: Creature magic_base which is the base for mana.
        """
        return self._magic_base

    def increase_magic_base(self, amount: int) -> int:
        """
        Increases magic_base.
        :param amount: Quantity to increase magic_base by.
        :return: Increase in magic_base.
        """
        self._magic_base += amount
        return amount

    def reduce_magic_base(self, amount: int) -> int:
        """
        Reduces magic stat to a minimum of 0.
        Also reduces current mana to equal magic_base if magic_base becomes less than current mana.
        :param amount: Quantity to reduce magic_base by.
        :return: Decrease in magic_base.
        """
        reduce = self._magic_base if self._magic_base < amount else amount
        self._magic_base -= reduce

        if self._magic_base < self._mana:
            self._mana = self._magic_base
        return reduce

    def charisma(self) -> int:
        """
        :return: Current charisma of the creature.
        """
        return self._charisma

    def increase_charisma(self, amount: int) -> int:
        """
        Increases charisma to less than or equal social.
        :param amount: Quantity to increase charisma by.
        :return: Increase in charisma.
        """
        add = (self._social - self._charisma) if self._social < (self._charisma + amount) else amount
        self._charisma += add
        return add

    def reduce_charisma(self, amount: int) -> int:
        """
        Reduces charisma to a minimum of 0.
        :param amount: Quantity to decrease charisma by.
        :return: Decrease in charisma.
        """
        reduce = self._charisma if self._charisma < amount else amount
        self._charisma -= reduce
        return reduce

    def social(self) -> int:
        """
        :return: Creature social which is the base for charisma.
        """
        return self._social

    def increase_social(self, amount: int) -> int:
        """
        Increases social.
        :param amount: Quantity to increase social by.
        :return: Increase in social.
        """
        self._social += amount
        return amount

    def reduce_social(self, amount: int) -> int:
        """
        Reduces social to a minimum of 0.
        Also reduces charisma to equal social if social becomes less than current charisma.
        :param amount: Quantity to reduce social by.
        :return: Decrease in social.
        """
        reduce = self._social if self._social < amount else amount
        self._social -= reduce

        if self._social < self._charisma:
            self._charisma = self._social
        return reduce

    def physicality(self) -> int:
        """
        :return: Creature physicality.
        """
        return self._physicality

    def increase_physicality(self, amount: int) -> int:
        """
        Increases physicality to less than or equal physicality_base.
        :param amount: Quantity to increase physicality by.
        :return: Increase in physicality.
        """
        if self._physicality_base < (self._physicality + amount):
            add = (self._physicality_base - self._physicality)
        else:
            add = amount
        self._physicality += add
        return add

    def reduce_physicality(self, amount: int) -> int:
        """
        Reduces physicality to a minimum of 0.
        :param amount: Quantity to decrease physicality by.
        :return: Decrease in physicality.
        """
        reduce = self._physicality if self._physicality < amount else amount
        self._physicality -= reduce
        return reduce

    def physicality_base(self) -> int:
        """
        :return: Creature physicality is based on this value.
        """
        return self._physicality_base

    def increase_physicality_base(self, amount: int) -> int:
        """
        Increases physicality_base.
        :param amount: Quantity to increase physicality_base by.
        :return: Increase in physicality_base.
        """
        self._physicality_base += amount
        return amount

    def reduce_physicality_base(self, amount: int) -> int:
        """
        Reduces physicality_base to a minimum of 0.
        Also reduces physicality to equal physicality_base if physicality_base becomes less than current physicality.
        :param amount: Quantity to reduce physicality_base by.
        :return: Decrease in physicality_base.
        """
        reduce = self._physicality_base if self._physicality_base < amount else amount
        self._physicality_base -= reduce

        if self._physicality_base < self._physicality:
            self._physicality = self._physicality_base
        return reduce

    def dexterity(self) -> int:
        """
        :return: Creature dexterity.
        """
        return self._dexterity

    def increase_dexterity(self, amount: int) -> int:
        """
        Increases dexterity to less than or equal dexterity_base.
        :param amount: Quantity to increase dexterity by.
        :return: Increase in dexterity.
        """
        add = (self._dexterity_base - self._dexterity) if self._dexterity_base < (
                self._dexterity + amount) else amount
        self._dexterity += add
        return add

    def reduce_dexterity(self, amount: int) -> int:
        """
        Reduces dexterity to a minimum of 0.
        :param amount: Quantity to decrease dexterity by.
        :return: Decrease in dexterity.
        """
        reduce = self._dexterity if self._dexterity < amount else amount
        self._dexterity -= reduce
        return reduce

    def dexterity_base(self) -> int:
        """
        :return: Creature dexterity is based on this value.
        """
        return self._dexterity_base

    def increase_dexterity_base(self, amount: int) -> int:
        """
        Increases dexterity_base.
        :param amount: Quantity to increase dexterity_base by.
        :return: Increase in dexterity_base.
        """
        self._dexterity_base += amount
        return amount

    def reduce_dexterity_base(self, amount: int) -> int:
        """
        Reduces dexterity_base to a minimum of 0.
        Also reduces dexterity to equal dexterity_base if dexterity_base becomes less than current dexterity.
        :param amount: Quantity to reduce dexterity_base by.
        :return: Decrease in dexterity_base.
        """
        reduce = self._dexterity_base if self._dexterity_base < amount else amount
        self._dexterity_base -= reduce

        if self._dexterity_base < self._dexterity:
            self._dexterity = self._dexterity_base

        return reduce

    def experience(self) -> int:
        """
        :return: Accumulated experience of the creature (is distinct from the experience_worth of a creature
        accumulated).
        """
        return self._experience

    def increase_experience(self, amount: int) -> int:
        """
        Increases experience.
        :param amount: Quantity to increase dexterity by.
        :return: Increase in experience.
        """
        self._experience += amount
        return amount
