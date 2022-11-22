class Counter:
    def __init__(self, number):
        self.number =number
        

    def numbers_divisible_by_three(self):
        myset = set()
        for i in range (self.number +1):
            if i % 3 == 0:
                myset.add(i)
        return myset
                 
    def odd_numbers(self):
        odd = set()
        for j in range (self.number):
            if j % 2 != 0:
                odd.add(j)
        return odd

    def even_numbers(self):
        even = set()
        for k in range (1, self.number +1):
           if k % 2 == 0:
                even.add(k)
        return even
    def even_numbers_intersection(self):
       even = self.even_numbers()
       odd = self.numbers_divisible_by_three()
       return even.intersection(odd)
        
    def odd_numbers_intersection(self):
        odd = self.odd_numbers()
        even = self.numbers_divisible_by_three()
        return odd.intersection(even)


counter = Counter(20)
print(counter.even_numbers())
print(counter.odd_numbers())
print(counter.even_numbers_intersection())
print(counter.odd_numbers_intersection())
