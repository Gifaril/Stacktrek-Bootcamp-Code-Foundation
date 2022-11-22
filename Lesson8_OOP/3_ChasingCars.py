class Car:

    def __init__(self, brand_name, kilometers, liters):
        self.c_brand_name = brand_name
        self.c_kilometers = kilometers
        self.c_liters = liters
        
    def calculate_mpg(self):
        miles = self.c_kilometers * 0.6214
        gallons = 0.264172 * self.c_liters
        return miles / gallons

    def calculate_rate_of_gas(self, price):
        # insert code
        pass