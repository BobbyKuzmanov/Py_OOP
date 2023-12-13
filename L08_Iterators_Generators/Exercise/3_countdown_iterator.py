class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

# Solution from teacher

# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= 0:
#             num = self.count
#             self.count -= 1
#             return num
#         else:
#             raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement
# the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.
#
# Output:
# 10 9 8 7 6 5 4 3 2 1 0