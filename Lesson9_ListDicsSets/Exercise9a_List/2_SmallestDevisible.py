class NumberList:
    def __init__(self, numbers, factor):
        self.numbers = numbers
        self.factor = factor

    def find_smallest_divisible(self):
        if (self.factor == 0):
            return -1
        lowest = None
        for i in self.numbers:
            if i % self.factor == 0:
               if (lowest == None):
                   lowest = i
                   continue
               if (i < lowest):
                   lowest = i 
        if (lowest == None):
            return -1
        return lowest

numbers = [1, 2, 3, 8, 0, 21, 88]
numberList = NumberList(numbers, 0)
numberList.find_smallest_divisible()