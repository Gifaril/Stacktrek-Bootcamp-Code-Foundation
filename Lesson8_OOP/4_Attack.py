class Hero:
    def __init__(self):
        self._name = "Duelle"
        self._max_health = 1000
        self._current_health = self._max_health
        self._attack_power = 50

    @property
    def name(self):
        return self._name

    @property
    def max_health(self):
        return self._max_health

    @property
    def current_health(self):
        return self._current_health

    @property
    def attack_power(self):
        return self._attack_power


class Monster:

    def __init__(self, name, max_health, attack_power, hero):
         self._name = name
         self._max_health = max_health
         self._current_health = self._max_health
         self._attack_power = attack_power
         self.hero = hero


    def attack(self):
        pass
        

    def defend(self):
       pass