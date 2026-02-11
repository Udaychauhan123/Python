class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

numbers = [10, 20, 30, 40, 50]
for num in MyIterator(numbers):
    print(num)
