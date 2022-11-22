class Package:

    def __init__(self, weight, distance):
        self._weight = weight
        self._distance = distance

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
        self.added_shipping_tax = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
        self.shipping_fee = value

    @property
    def shipping_fee(self):
        return self._shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, distance):
        if distance < 2:
            self._shipping_fee = 0
        elif distance < 100:
            self._shipping_fee = 45
        else:
            mile_price = (distance // 100) * 50
            extra = (distance % 100) * 1.50
            self._shipping_fee = mile_price + extra

    @property
    def added_shipping_tax(self):
        return self._added_shipping_tax

    @added_shipping_tax.setter
    def added_shipping_tax(self, weight):
        if weight >= 1:
            tax_amount = weight * 0.25
            self._added_shipping_tax = tax_amount
        else:
            self._added_shipping_tax = 0

    @property
    def total_shipping_fee(self):
        self._total_shipping_fee = self.shipping_fee + self.added_shipping_tax

        return round(self._total_shipping_fee, 2)