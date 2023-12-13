class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = len(iter_obj) - 1
        self.end = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.end:
            raise StopIteration
        current_index = self.index
        self.index -= 1
        return self.iter_obj[current_index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# Create a class called reverse_iter which should receive an iterable upon initialization. Implement
# the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
