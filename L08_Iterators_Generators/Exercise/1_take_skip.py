class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            result = self.step * self.counter
            self.counter += 1
            return result
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
#
# Create a class called take_skip. Upon initialization, it should receive a step (int) and
# a count (int). Implement the __iter__ and __next__ functions.
# The iterator should return the count numbers (starting from 0) with the given step.
#
# Output:
# 0
# 2
# 4
# 6
# 8
# 10