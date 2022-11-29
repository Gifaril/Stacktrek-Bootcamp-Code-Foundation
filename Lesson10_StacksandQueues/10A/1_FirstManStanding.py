class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def add(self, element):
        self.arr.append(element)

    def remove(self):
        self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def display(self):
        return self.arr[0:self.size]
