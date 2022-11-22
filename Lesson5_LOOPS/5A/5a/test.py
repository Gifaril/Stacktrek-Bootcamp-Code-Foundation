class Package:

    def __init__(self, weight, distance):
      self.p_weight = weight
      self.p_distance = distance

    @property
    def weight(self):
        if (isinstance(self.p_weight, int)):
            self.p_weight
        return float(format(self.p_weight, '.2f'))

    @weight.setter
    def weight(self, value):
        self.p_weight = value
        

    @property
    def distance(self):
        if (isinstance(self.p_distance, int)):
            return self.p_distance
        return float(format(self.p_distance, '.2f'))

    @distance.setter
    def distance(self, value):
        self.p_distance = value
        

    @property
    def shipping_fee(self):
        if (self.p_distance < 1):
          return 0
        if (self.p_distance < 100):
          return 45
        m = int(self.p_distance / 100)
        curr = m * 50
        add = (self.p_distance - (m*100)) * 1.50
        total = curr+add
        if (isinstance(total, int)):
          return total
        total = float(format(total, '.2f'))
        return total
        
      
    @property
    def added_shipping_tax(self):
        total = int(self.p_weight * 0.25)
        return total

    @property
    def total_shipping_fee(self):
        total = self.added_shipping_tax + self.shipping_fee
        if (isinstance(total, int)):
          return total
        total = float(format(total, '.2f'))
        return total
my_package = Package(5, 99)
my_package.weight = -1.5
my_package.distance = 0
print(my_package.weight)
print(my_package.distance)
print(my_package.shipping_fee)
print(my_package.added_shipping_tax)
print(my_package.total_shipping_fee)

