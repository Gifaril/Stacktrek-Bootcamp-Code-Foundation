class MasterCheffy:
    def __init__(self):
        self.l = []

    def store_leftover(self, leftover):
        self.l.append(leftover)
    def get_leftovers(self):
        return self.l

    def get_ingredients(self, quantity):
        test = self.l
        self.l = test[quantity:]
        return test[0:quantity]